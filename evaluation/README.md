🚀 Usage

1️⃣ Import the Visualization Function

from bug_visualization import generate_bug_visualization

2️⃣ Example Usage

error_counts = {
    "Syntax Error": 3,
    "Type Error": 2,
    "ZeroDivision Error": 1
}

fig = generate_bug_visualization(error_counts)
fig.show()

3️⃣ Example Output
The script generates a bar chart like this:
📊 Bug Type Frequency (Detected Errors)







+-------------------+---------------+
| Bug Type         | Occurrences   |
+-------------------+---------------+
| Syntax Error     | 3             |
| Type Error      | 2             |
| ZeroDivision Error | 1             |
+-------------------+---------------+


















📌 Handling No Errors
If no errors are detected, the function returns an empty chart labeled "No Errors Detected."

🛠️ How It Works
Converts the error_counts dictionary into a Pandas DataFrame

Uses Plotly Express (px.bar) to create a bar chart

Automatically adjusts chart labels and titles
