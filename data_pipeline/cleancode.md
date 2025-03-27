# 🧹 Code Cleaner  

This script (`clean_code.py`) **removes unnecessary whitespace and comments** from Python code to improve readability and efficiency.  

---

## 📌 Features  
✅ **Removes comments (`# this is a comment`)**  
✅ **Trims extra spaces and newlines**  
✅ **Keeps the code clean and compact**  

🚀 Usage
1️⃣ Import the Script
from clean_code import clean_code

2️⃣ Provide the Code for Cleaning
code_snippet = '''
# This function adds two numbers
def add(a, b):  
    return a + b  # Return sum
'''

cleaned_code = clean_code(code_snippet)
print(cleaned_code)

3️⃣ Output Example
def add(a, b): return a + b
🛠️ How It Works
🔍 Cleaning Process
Removes all # comments

Replaces multiple spaces/newlines with a single space

Returns a clean and compact version of the code


📊 Use Cases
Preprocessing code before debugging

Reducing clutter for AI-based bug detection

Enhancing readability for machine learning models

