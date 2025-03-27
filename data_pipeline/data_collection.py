import re
from collections import defaultdict

def detect_errors(debug_output):
    """Detects common error types in Python code."""
    error_patterns = {
        "Syntax Error": r"SyntaxError",
        "Logic Error": r"logic error",
        "Runtime Error": r"RuntimeError",
        "Indentation Error": r"IndentationError",
        "Type Error": r"TypeError",
        "Name Error": r"NameError",
        "Index Error": r"IndexError",
        "Key Error": r"KeyError",
        "Attribute Error": r"AttributeError",
        "ZeroDivision Error": r"ZeroDivisionError",
        "Import Error": r"ImportError",
        "ModuleNotFound Error": r"ModuleNotFoundError",
        "Value Error": r"ValueError",
    }
    
    error_counts = defaultdict(int)
    
    for error_type, pattern in error_patterns.items():
        matches = re.findall(pattern, debug_output, re.IGNORECASE)
        error_counts[error_type] += len(matches)

    return dict(error_counts)
