# 📊 Bug Visualization Module

Easily visualize the frequency of different types of bugs detected in Python code using this helper function.

---

## 🚀 Usage

### 1️⃣ Import the Visualization Function

```python
from bug_visualization import generate_bug_visualization
```

### 2️⃣ Example Usage

```python
error_counts = {
    "Syntax Error": 3,
    "Type Error": 2,
    "ZeroDivision Error": 1
}

fig = generate_bug_visualization(error_counts)
fig.show()
```

---

## ✅ Example Output

The function generates a bar chart like the one below:

| Bug Type           | Occurrences |
|--------------------|-------------|
| Syntax Error       | 3           |
| Type Error         | 2           |
| ZeroDivision Error | 1           |

📈 Each error type is displayed with its frequency, making it easy to understand the nature of issues in the code.

---

## 📌 Handling No Errors

If no errors are detected (`error_counts` is empty), the function automatically returns a placeholder chart labeled **"No Errors"** to prevent rendering issues.

---

## 🛠️ How It Works

- Converts the `error_counts` dictionary into a Pandas DataFrame.
- Uses **Plotly Express** (`px.bar`) to create a clean, interactive bar chart.
- Automatically configures chart labels, titles, and themes for readability.
