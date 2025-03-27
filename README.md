# 🐞 Software Code Bug Detection & Fixing 🚀

## Overview
This project is an **AI-powered debugging tool** that analyzes Python code for errors and provides insightful debugging suggestions. It utilizes the **Qwen2.5-Coder-1.5B-Instruct** model for detecting syntax, logic, and runtime errors, offering an interactive **Gradio UI** for real-time debugging and visualization.

## 🔹 Features
- **AI Debugging**: Detects and analyzes Python code issues with deep learning.
- **Error Categorization**: Identifies common errors such as SyntaxError, TypeError, and more.
- **LRU Caching**: Implements Least Recently Used (LRU) caching for optimized performance.
- **Bug Visualization**: Generates interactive charts using **Plotly** for error distribution analysis.
- **Gradio Web Interface**: Provides an easy-to-use, no-code debugging environment.
- **Manually Installed Model**: The AI model is manually installed instead of using direct APIs.

## 🏗️ Project Documentation
### 📌 Architectural Design
This system follows a modular architecture that includes:
- **Code Processing Layer**: Handles input parsing, debugging, and error detection.
- **AI Model Layer**: Utilizes `Qwen2.5-Coder-1.5B-Instruct` to analyze code.
- **Data Visualization Layer**: Uses **Plotly** to generate bug reports.
- **User Interface**: Implemented using **Gradio** for seamless interaction.

### 📌 Data Pipeline
- **Data Collection Scripts**: Scripts to gather sample error-prone Python code for testing.
- **Preprocessing Modules**: Cleans and formats code input for AI analysis.
- **Data Storage Solution**: Utilizes an **LRU cache** for efficient response times.

### 📌 AI Models
- **Transformer-based Model**: `Qwen2.5-Coder-1.5B-Instruct` manually installed.
- **Tokenization and Generation**: Uses Hugging Face's `AutoTokenizer` and `AutoModelForCausalLM`.

### 📌 Evaluation Metrics & Test Results
- **Error Detection Accuracy**: Benchmarked using predefined test cases.
- **Latency Analysis**:
  - **Hugging Face Space** (Free CPU): Takes longer due to hardware constraints.
  - **Local CPU Execution**: High computation time.
  - **Local GPU Execution**: Significantly faster performance.

### 📌 Integration & Deployment
- **Hugging Face Space**: [Check out the live demo here!](<https://huggingface.co/spaces/neviiiiii/fixyourbugs>)
- **Deployment Scripts**: Automates model loading and debugging execution.
- **Docker Support**: Can be containerized for cloud-based deployment.


```

## 🚀 Getting Started
### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/software-bug-detection.git
   cd software-bug-detection
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Gradio interface**:
   ```bash
   python app.py
   ```
[ dont forget the requirements ]

## 🛠️ Future Enhancements
- Add support for debugging additional programming languages.
- Implement real-time debugging suggestions with auto-fix options.
- Optimize performance with more efficient model quantization techniques.

---
### 📢 Note: Execution Time Variations
- **Hugging Face Space (Free CPU)**: May experience delays due to limited compute resources.
- **Local CPU Execution**: Slower than GPU, but functional for basic debugging.
- **Local GPU Execution**: Offers the best performance for real-time debugging.

🚀 **Try it now and enhance your debugging workflow!**

