# 🐞 AI Bug Detector 🚀  

An interactive **AI-powered Python debugger** that detects and visualizes bugs in your code.  

---

## 📌 Features  
✅ **AI-powered bug detection** using `transformers`  
✅ **Interactive Gradio UI** for easy debugging  
✅ **Real-time bug visualization** with `plotly`  
✅ **Fast and efficient** debugging with LRU caching  

---

## 🛠️ Installation  

### 🔹 Step 1: Install Dependencies  
Ensure you have Python 3.8+ and install the required libraries:  
```bash
pip install torch transformers gradio plotly pandas

🚀 Usage
1️⃣ Run the Application

python app.py

2️⃣ Interact with the UI

Enter Python code in the text box

Click "Debug Code" to analyze

View the debugging output and error visualization

🖼️ Example UI:

+--------------------------------------+
|   🐞 AI Bug Detector 🚀              |
|--------------------------------------|
|  Enter Your Code [Python]            |
|  [ Code Editor ]                     |
|                                      |
|  [ Debug Code Button ]               |
|--------------------------------------|
| Debugging Output                     |
| [ Error Messages ]                    |
|--------------------------------------|
| Bug Type Analysis (Graph)            |
+--------------------------------------+

🛠️ How It Works
Uses transformers to analyze the given Python code

Detects common error types (SyntaxError, TypeError, etc.)

Generates a bar chart with plotly to visualize bug frequency

Built using Gradio for a user-friendly debugging experience
