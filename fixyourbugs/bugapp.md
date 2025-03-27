# 🐞 AI Bug Detector 🚀  

This application is an AI-powered **Python code bug detection and debugging assistant** using **Qwen2.5-Coder-1.5B-Instruct**. It identifies errors in Python scripts and suggests fixes using deep learning models.  

## 📌 Features  
- **Automatic Bug Detection**: Identifies syntax, logic, runtime, and other common Python errors.  
- **AI-Powered Fixes**: Uses a transformer model to suggest corrections.  
- **LRU Caching**: Speeds up debugging by storing recent results.  
- **Error Visualization**: Generates bar charts for detected errors.  
- **Gradio UI**: Provides an interactive interface for debugging Python scripts.  

## 📂 Project Structure  
- `app.py` → Main script for running the AI bug detection system.  
- `ai_models/` → Model files and training scripts.  
- `requirements.txt` → List of dependencies to install before running the app.  
- `README.md` → Documentation for the application.  

## 🚀 Installation  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/neeeeevin/Software-Code-Bug-Detection-and-Fixing.git
cd Software-Code-Bug-Detection-and-Fixing

2️⃣ Install Dependencies


pip install -r requirements.txt

3️⃣ Run the Application

python app.py


🛠 How It Works
Enter Python Code in the text editor.

Click "Debug Code" to analyze and detect bugs.

View the Debugging Output and AI-suggested fixes.

Check Error Visualization to see the most common error types.

🖼️ Example Output

Syntax Error at Line 3: Unexpected Indentation
Suggested Fix: Adjust the indentation of the block at line 3.


📜 License
This project is licensed under the MIT License.

