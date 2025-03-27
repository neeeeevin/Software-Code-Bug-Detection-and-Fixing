import gradio as gr
from debug import debug_code
from visualization import generate_bug_visualization

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 🐞 AI Bug Detector 🚀 \n### Enter Python code below to debug.")
    
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

if __name__ == "__main__":
    demo.launch()
