import plotly.graph_objs as go
from plotly.offline import init_notebook_mode,plot
import pandas as pd

import plotly.graph_objs as go
init_notebook_mode(connected=True)

file = '2014_World_Power_Consumption'
df = pd.read_csv(file)

data = dict(type='choropleth',
            locations=df['Country'],
            colorscale='Picnic',
            locationmode='country names',
            text=df['Text'],
            z=['Power Consumption KWH'],
            colorbar={'title':'Power Consumption in KWH'})

layout = dict(title = '2014 Global Power Consumption',
            geo = dict(showframe = False,
        projection = {'type':'robinson'}))


choro1 = go.Figure(data=[data], layout=layout)
plot(choro1)