import torch
import gradio as gr
import plotly.express as px
import pandas as pd
import re
from collections import defaultdict, OrderedDict
from transformers import AutoModelForCausalLM, AutoTokenizer

# Model Config
MODEL_NAME = "Qwen/Qwen2.5-Coder-1.5B-Instruct"

def load_model():
    """Load the AI model for debugging."""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float32,  # Ensure CPU compatibility
    ).to(device)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    return model, tokenizer, device

# Load model & tokenizer
model, tokenizer, device = load_model()

# LRU Cache Implementation
class LRUCache:
    def _init_(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key: str):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)  # Mark as recently used
        return self.cache[key]
    
    def put(self, key: str, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used
        self.cache[key] = value

# Initialize Cache
lru_cache = LRUCache(capacity=10)

def debug_code(input_text):
    """Debugs the given Python code."""
    cached_result = lru_cache.get(input_text)
    if cached_result:
        return cached_result
    
    try:
        # Preprocess input
        messages = [
            {"role": "system", "content": "You are an AI-powered code debugging assistant."},
            {"role": "user", "content": input_text}
        ]
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        model_inputs = tokenizer([text], return_tensors="pt").to(device)

        with torch.no_grad():
            generated_ids = model.generate(**model_inputs, max_new_tokens=512)

        generated_tokens = generated_ids[0][model_inputs.input_ids.size(1):]
        output = tokenizer.decode(generated_tokens, skip_special_tokens=True)
        
        # Detect Errors
        error_counts = detect_errors(output)

        # Store in cache
        lru_cache.put(input_text, (output, error_counts))
        
        return output, error_counts
    except Exception as e:
        return f"Error in debugging: {str(e)}", {}

def detect_errors(debug_output):
    """Detects common error types in Python code."""
    error_patterns = {
        "Syntax Error": r"syntax\s?error|SyntaxError",
        "Logic Error": r"logic\s?error",
        "Runtime Error": r"runtime\s?error|RuntimeError",
        "Indentation Error": r"indentation\s?error|IndentationError",
        "Type Error": r"type\s?error|TypeError",
        "Name Error": r"name\s?error|NameError",
        "Index Error": r"index\s?error|IndexError",
        "Key Error": r"key\s?error|KeyError",
        "Attribute Error": r"attribute\s?error|AttributeError",
        "ZeroDivision Error": r"zero\s?division\s?error|ZeroDivisionError",
        "Import Error": r"import\s?error|ImportError",
        "ModuleNotFound Error": r"module\s?not\s?found\s?error|ModuleNotFoundError",
        "Value Error": r"value\s?error|ValueError",
    }
    
    error_counts = defaultdict(int)
    
    # Convert output to lowercase for better error detection
    debug_output_lower = debug_output.lower()

    for error_type, pattern in error_patterns.items():
        matches = re.findall(pattern, debug_output_lower, re.IGNORECASE)
        error_counts[error_type] += len(matches)

    return dict(error_counts)

def generate_bug_visualization(error_counts):
    """Generates a bar chart for detected errors."""
    if not error_counts:
        # Ensure at least an empty plot is returned to avoid rendering issues
        df = pd.DataFrame({"Bug Type": ["No Errors"], "Occurrences": [0]})
    else:
        df = pd.DataFrame(list(error_counts.items()), columns=["Bug Type", "Occurrences"])

    fig = px.bar(
        df,
        x="Bug Type",
        y="Occurrences",
        title="Bug Type Frequency (Detected Errors)",
        color="Bug Type",
        text_auto=True
    )
    
    fig.update_layout(
        xaxis_title="Error Type",
        yaxis_title="Number of Occurrences",
        template="plotly_dark",
        height=500
    )

    return fig

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# AI Bug Detector  \n### Enter Python code below to debug.")
    
    with gr.Row():
        code_input = gr.Code(label="Enter Your Code", language="python", lines=10)
        debug_button = gr.Button("Debug Code", variant="primary")
    
    with gr.Row():
        output_box = gr.Textbox(label="Debugging Output", lines=15, interactive=False)
    
    bug_chart = gr.Plot(label="Bug Type Analysis")
    
    def process_code(input_text):
        debug_output, error_counts = debug_code(input_text)
        return debug_output, generate_bug_visualization(error_counts)
    
    debug_button.click(fn=process_code, inputs=code_input, outputs=[output_box, bug_chart])

if _name_ == "_main_":
    demo.launch(share=True)