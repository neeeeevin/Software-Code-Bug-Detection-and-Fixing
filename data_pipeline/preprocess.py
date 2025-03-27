import re

def clean_code(code):
    """Removes unnecessary whitespace and comments from the input code."""
    code = re.sub(r"#.*", "", code)  # Remove comments
    code = re.sub(r"\s+", " ", code).strip()  # Remove extra whitespace
    return code
