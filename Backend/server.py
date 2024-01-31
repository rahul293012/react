import pandas as pd

data = pd.read_csv("dataset.csv")

def downsample_data(data, threshold):

    step = len(data) // threshold

    downsampled_data = data.iloc[::step, :]

    return downsampled_data

threshold = 1000

downsampled_data = downsample_data(data, threshold)

print(downsampled_data.head())

import plotly.graph_objs as go
from plotly.subplots import make_subplots

fig = make_subplots()

fig.add_trace(go.Scatter(x=downsampled_data['Timestamp'], y=downsampled_data['Profit Percentage'], mode='lines', name='Profit Percentage'))

fig.update_layout(title='Profit Percentage vs Time', xaxis_title='Time', yaxis_title='Profit Percentage')

fig.show()
