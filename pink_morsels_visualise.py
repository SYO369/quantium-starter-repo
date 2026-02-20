import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go

# Load the data
df = pd.read_csv('formatted_sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Pink Morsel Visualizer",
        id='app-header'
        ),

    html.Div([
        html.Label("Select Region:"),
        dcc.RadioItems(
            id='region-selector',
            options=[
                {'label': ' North', 'value': 'north'},
                {'label': ' South', 'value': 'south'},
                {'label': ' East', 'value': 'east'},
                {'label': ' West', 'value': 'west'},
                {'label': 'All', 'value': 'all'},
            ],
            value='north',
            inline=True,
            className='radio-items'
        ),
    ], className='controls'),

    html.Div([
        html.Div(dcc.Graph(id='sales-chart'), className='chart-wrapper')
    ], className='card'),

], className='app-container')


@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df.copy()
    else:
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
        template='plotly_white',
        title=dict(text=f'Daily Sales - {selected_region.capitalize()} Region', x=0.01, xanchor='left', font=dict(size=18, color='#0f172a')),
        xaxis_title='Date',
        yaxis_title='Sales ($)',
        hovermode='x unified',
        height=520,
        font=dict(family='Inter, Arial, sans-serif', size=12, color='#0f172a'),
        plot_bgcolor='white',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=60, r=24, t=70, b=60),
        bargap=0.15
    )
    fig.update_traces(marker=dict(color='#ff6f91', line=dict(color='#e85a78', width=0.5)))
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(gridcolor='rgba(15,23,42,0.06)', zeroline=False)
    
    return fig


if __name__ == '__main__':
    app.run(debug=True)
