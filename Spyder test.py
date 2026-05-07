import pandas as pd
import plotly.graph_objects as go

# 1. Define your variables/data
data = {
    "Step": ["Starting Cash", "Sales", "Refunds", "Marketing", "Salaries", "Net Cash"],
    "Amount": [100, 50, -10, -20, -30, 0], # Net Cash 0 is placeholder for 'total'
    "Measure": ["relative", "relative", "relative", "relative", "relative", "total"]
}

df = pd.DataFrame(data)

# 2. Display the Table
print("--- Financial Data Table ---")
print(df.to_string(index=0+False))

# 3. Create the Waterfall Chart
fig = go.Figure(go.Waterfall(
    name = "Cash Flow",
    orientation = "v",
    measure = df["Measure"],
    x = df["Step"],
    textposition = "outside",
    text = [f"{x:+}" if m == "relative" else f"Total: {x}" for x, m in zip(df["Amount"], df["Measure"])],
    y = df["Amount"],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
    increasing = {"marker":{"color": "#2ca02c"}}, # Green for gains
    decreasing = {"marker":{"color": "#d62728"}}, # Red for losses
    totals = {"marker":{"color": "#1f77b4"}}      # Blue for total
))

fig.update_layout(
    title = "Monthly Cash Flow Analysis",
    showlegend = False,
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.show()

#test comment in spyder
#test comment in spyder 2


