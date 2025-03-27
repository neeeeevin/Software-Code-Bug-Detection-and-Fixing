# Hugging Face Deployment Guide

## Overview
This guide provides a step-by-step approach to deploying the **Software Code Bug Detection & Fixing** model on Hugging Face Spaces. The model utilizes `Qwen/Qwen2.5-Coder-1.5B-Instruct` and is manually installed for both local and cloud-based execution.

---

## 1. Setting Up a Hugging Face Space

### Step 1: Create a Space
1. Go to [Hugging Face Spaces](https://huggingface.co/spaces) and click on **Create a new Space**.
2. Choose **Gradio** as the SDK.
3. Set the Space to **Public** (or Private if required).
4. Clone the repository to your local system.

### Step 2: Define Dependencies
Inside the Space, create a `requirements.txt` file and add the following dependencies:

```txt
transformers
torch
gradio
plotly
p pandas
huggingface_hub
```

Additionally, include a `runtime.txt` file to specify the Python version:

```txt
python-3.10
```

---

## 2. Deployment on Hugging Face Spaces

### Step 1: Upload Project Files
Ensure the following files are added to your Hugging Face repository:
- `app.py` (Main Gradio application script)
- `requirements.txt` (Dependencies)
- `runtime.txt` (Python version)
- `model/` (Pretrained model files if manually uploaded)

### Step 2: Modify `app.py` for Hugging Face
Ensure `app.py` includes:
```python
import torch
import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "Qwen/Qwen2.5-Coder-1.5B-Instruct"

def load_model():
    device = "cpu"  # Free tier supports only CPU
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float32)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    return model, tokenizer, device
```

> **Note:** Free-tier CPUs on Hugging Face Spaces are slow. Expect longer inference times.

---

## 3. Local Deployment
For local execution, ensure you have a GPU for faster processing. Install dependencies and run:

```bash
pip install -r requirements.txt
python app.py
```

If using CUDA-enabled GPUs, modify the script:
```python
device = "cuda" if torch.cuda.is_available() else "cpu"
```

---

## 4. Execution Time Considerations
| Environment  | Expected Execution Time |
|-------------|-----------------------|
| **Hugging Face (Free CPU)** | Slow (~30-60s per request) |
| **Local CPU** | Moderate (~15-30s per request) |
| **Local GPU** | Fast (~2-5s per request) |

---

## 5. Integration with Hugging Face API
For further integration, you can use the **Hugging Face Inference API** to test the model:

```python
from huggingface_hub import InferenceClient
client = InferenceClient(model="your-huggingface-space-name")
response = client.text_generation("def factorial(n):")
print(response)
```

---

## 6. Troubleshooting & Logs
- If the model doesn't load, ensure enough memory is available.
- Monitor logs on Hugging Face Spaces UI under the **Logs** tab.
- If execution times are too slow, consider upgrading to a **paid** GPU Space.

---

## Conclusion
By following these steps, you can successfully deploy the **Software Code Bug Detection & Fixing** model on Hugging Face Spaces and optimize it for local execution as needed. 🚀

