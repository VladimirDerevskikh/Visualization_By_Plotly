# Importing required modules
from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd

# Reading data on trips from the cell that contains the Empire State Building
df = pd.read_csv('ESB_trips_2.csv', index_col=['hour'], parse_dates=['hour'])


# Setting parameters for the time series graph and interactive display controls

# Create figure
fig = go.Figure()

fig.add_trace(
    go.Scatter(x=list(df.index), y=list(df['1231'])))

# Set title
fig.update_layout(
    title_text="Number of Trips from ESB Area"
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

# Drawing the figure
plot(fig, filename = 'Number of Trips from ESB Cell Visualization.html')
