# 📊 Data Collection for Error Analysis  

This script (`datacollection.py`) extracts **error types from debugging output** and counts their occurrences using **regular expressions**. It is part of a larger **AI-powered bug detection** project.  

---

## 📌 Features  
✅ **Detects common Python errors** (SyntaxError, TypeError, etc.)  
✅ **Uses regex patterns for efficient error matching**  
✅ **Counts occurrences of different error types**  
✅ **Stores results in a dictionary for further analysis**  



 Usage

1️⃣ Import the Script


from datacollection import detect_errors

2️⃣ Provide Debugging Output


debug_output = """
Traceback (most recent call last):
  File "script.py", line 2, in <module>
    print(1/0)
ZeroDivisionError: division by zero
"""

error_counts = detect_errors(debug_output)
print(error_counts)

3️⃣ Output Example


{
    "ZeroDivision Error": 1
}


🛠️ How It Works
🔍 Error Detection
The script scans debugging logs for common Python errors using regex patterns.

🔢 Counting Errors
It maintains a count of detected errors in a dictionary for easy analysis.

📊 Future Integration
These counts can be used for visualization (e.g., Plotly charts) in the AI debugging interface.
