import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

# Load the extracted data
df = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Statistics Dashboard"

# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]
suppress_callback_exceptions = True
# List of years
year_list = [i for i in range(1980, 2024, 1)]

# Create the layout of the app
app.layout = html.Div([
    # Add title to the dashboard
    html.H1("Automobile Sales Statistics Dashboard",  # May include style for title
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': '24px'}
            ),

    # Add two dropdown menus
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=[
                {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
            ],
            placeholder='Select a report type',
            value='Select Statistics',
            style={'width': '80%', 'padding': '3px', 'fontSize': '20px', 'textAlignLast': 'center'}
        )
    ]),

    # Dropdown for year selection
    html.Div([
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            placeholder='Select a year',
            style={'width': '80%', 'padding': '3px', 'fontSize': '20px', 'textAlignLast': 'center'}),
        html.Div([
            html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),
        ]), ])
])


@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'),
     Input(component_id='select-year', component_property='value')]
)
def update_output_container(selected_statistics, input_year):
    if selected_statistics == 'Recession Period Statistics':
        recession_data = df[df['Recession'] == 1]
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec,
                           x='Year',
                           y='Automobile_Sales',
                           title="Automobile Sales Fluctuation Over Recession Period")
        )
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(
            figure=px.bar(average_sales,
                          x='Vehicle_Type',
                          y='Automobile_Sales',
                          title="Average Vehicles Sold by Vehicle Type During Recession",
                          color_discrete_sequence=['orange'])
        )
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(exp_rec,
                          values='Advertising_Expenditure',
                          names='Vehicle_Type',
                          title="Expenditure Share by Vehicle Type During Recession")
        )
        unemployment_data = recession_data.groupby('Vehicle_Type')['unemployment_rate'].mean().reset_index()
        R_chart4 = dcc.Graph(
            figure=px.bar(unemployment_data,
                          x='Vehicle_Type',
                          y='unemployment_rate',
                          title="Effect of Unemployment Rate on Vehicle Type During Recession")
        )
        return html.Div([
            html.Div([R_chart1, R_chart2], style={'display': 'flex', 'flex-direction': 'row'}),
            html.Div([R_chart3, R_chart4], style={'display': 'flex', 'flex-direction': 'row'})
        ], style={'display': 'flex', 'flex-direction': 'column'})

    elif (input_year and selected_statistics == 'Yearly Statistics'):
        yearly_data = df[df['Year'] == input_year]
        yas = df.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(
            figure=px.line(yas,
                           x='Year',
                           y='Automobile_Sales',
                           title="Yearly Automobile Sales Over Time")
        )
        monthly_sales = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(
            figure=px.line(monthly_sales,
                           x='Month',
                           y='Automobile_Sales',
                           title="Total Monthly Automobile Sales for the Year {}".format(input_year),
                           color_discrete_sequence=['orange'])
        )
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(
            figure=px.bar(avr_vdata,
                          x='Vehicle_Type',
                          y='Automobile_Sales',
                          title="Average Vehicles Sold by Vehicle Type in the year {}".format(input_year))
        )
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(exp_data,
                          values='Advertising_Expenditure',
                          names='Vehicle_Type',
                          title="Advertisement Expenditure by Vehicle Type for the Year {}".format(input_year))
        )
        return html.Div([
            html.Div([Y_chart1, Y_chart2], style={'display': 'flex', 'flex-direction': 'row'}),
            html.Div([Y_chart3, Y_chart4], style={'display': 'flex', 'flex-direction': 'row'})
        ], style={'display': 'flex', 'flex-direction': 'column'})

    else:
        return None


if __name__ == '__main__':
    app.run_server(debug=True)
