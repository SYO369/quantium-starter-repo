import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go

# Load the data
df = pd.read_csv('formatted_sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Visualizer"),
    
    html.Div([
        html.Label("Select Region:"),
        dcc.RadioItems(
            id='region-selector',
            options=[
                {'label': ' North', 'value': 'north'},
                {'label': ' South', 'value': 'south'},
                {'label': ' East', 'value': 'east'},
                {'label': ' West', 'value': 'west'},
            ],
            value='north',
            inline=True,
            style={'marginBottom': '20px'}
        ),
    ], style={'marginBottom': '30px'}),
    
    dcc.Graph(id='sales-chart'),
])


@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    filtered_df = df[df['Region'] == selected_region].copy()
    filtered_df = filtered_df.sort_values('Date')
    
    # Group by date and sum sales
    daily_sales = filtered_df.groupby('Date')['Sales'].sum().reset_index()
    
    fig = go.Figure(data=[
        go.Bar(
            x=daily_sales['Date'],
            y=daily_sales['Sales'],
            marker_color='#1f77b4'
        )
    ])
    
    fig.update_layout(
        title=f'Daily Sales - {selected_region.capitalize()} Region',
        xaxis_title='Date',
        yaxis_title='Sales ($)',
        hovermode='x unified',
        height=500
    )
    
    return fig


if __name__ == '__main__':
    app.run()
