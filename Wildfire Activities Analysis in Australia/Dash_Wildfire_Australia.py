import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update
import datetime as dt

# Create app
app = dash.Dash(__name__)

# Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True

# Read the wildfire data into pandas dataframe
df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv')

# Extract year and month from the date column
df['Month'] = pd.to_datetime(df['Date']).dt.month_name()
df['Year'] = pd.to_datetime(df['Date']).dt.year

# Layout Section of Dash
app.layout = html.Div(children=[
    html.H1('Australia Wildfire Dashboard'),

    html.Div([
        # Adding dropdown helper text for Selected Drive wheels
        html.Div([
            html.H2('Select Region:'),

            # Radio items to select the region
            dcc.RadioItems([{"label": "New South Wales", "value": "NSW"},
                            {"label": "Northern Territory", "value": "NT"},
                            {"label": "Queensland", "value": "QL"},
                            {"label": "South Australia", "value": "SA"},
                            {"label": "Tasmania", "value": "TA"},
                            {"label": "Victoria", "value": "VI"},
                            {"label": "Western Australia", "value": "WA"}],
                           value="NSW", id='region-radio', inline=True)
        ]),

        # Dropdown to select year
        html.Div([
            html.H2('Select Year:', style={'margin-top': '20px'}),
            dcc.Dropdown(id='year-dropdown',
                         options=[{'label': year, 'value': year} for year in df['Year'].unique()],
                         value=df['Year'].min())
        ]),

        # Adding 2 inner divisions for 2 output graphs
        html.Div([
            html.Div([], id='output-pie'),
            html.Div([], id='output-bar')
        ], style={'display': 'flex', 'justify-content': 'space-around'})
    ])
])

# Place to add @app.callback Decorator
@app.callback([Output(component_id='output-pie', component_property='children'),
               Output(component_id='output-bar', component_property='children')],
              [Input(component_id='region-radio', component_property='value'),
               Input(component_id='year-dropdown', component_property='value')])

# Place to define the callback function
def reg_year_display(input_region, input_year):
    # Data
    region_data = df[df['Region'] == input_region]
    y_r_data = region_data[region_data['Year'] == input_year]

    # Plot one - Monthly Average Estimated Fire Area
    est_data = y_r_data.groupby('Month')['Estimated_fire_area'].mean().reset_index()
    fig1 = px.pie(est_data, names='Month', values='Estimated_fire_area',
                  title="{} : Monthly Average Estimated Fire Area in year {}".format(input_region, input_year))

    # Plot two - Monthly Average Count of Pixels for Presumed Vegetation Fires
    veg_data = y_r_data.groupby('Month')['Count'].mean().reset_index()
    fig2 = px.bar(veg_data, x='Month', y='Count',
                  title='{} : Average Count of Pixels for Presumed Vegetation Fires in year {}'.format(input_region, input_year))

    return [dcc.Graph(figure=fig1), dcc.Graph(figure=fig2)]

if __name__ == '__main__':
    app.run_server()
