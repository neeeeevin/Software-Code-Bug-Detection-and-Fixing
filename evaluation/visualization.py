import plotly.express as px
import pandas as pd

def generate_bug_visualization(error_counts):
    """Generates a bar chart for detected errors."""
    if not error_counts:
        return px.bar(title="No Errors Detected", labels={"x": "Bug Type", "y": "Occurrences"})
    
    df = pd.DataFrame(list(error_counts.items()), columns=["Bug Type", "Occurrences"])
    fig = px.bar(df, x="Bug Type", y="Occurrences", title="Bug Type Frequency (Detected Errors)")
    
    return fig
