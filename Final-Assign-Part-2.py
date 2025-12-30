#!/usr/bin/env python
# coding: utf-8

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/d51iMGfp_t0QpO30Lym-dw/automobile-sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Statistics Dashboard"

#---------------------------------------------------------------------------------
# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]
# List of years 
year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------
# Create the layout of the app
app.layout = html.Div([
    #TASK 2.1 Add title to the dashboard
    html.H1("Automobile Sales Statistics Dashboard",
            style={'textAlign': 'center', 
                   'color': '#503D36',
                   'font-size': 24,
                   'margin-bottom': '30px'}),
    
    #TASK 2.2: Add two dropdown menus with proper styling
    html.Div([
        html.Div([
            html.Label("Select Statistics:", 
                       style={'font-weight': 'bold', 'font-size': '18px', 'margin-bottom': '5px'}),
            dcc.Dropdown(
                id='dropdown-statistics',
                options=dropdown_options,
                value='Select Statistics',
                placeholder='Select a report type',
                style={'width': '100%', 
                       'padding': '10px', 
                       'font-size': '16px',
                       'border-radius': '5px',
                       'border': '1px solid #ccc'}
            )
        ], style={'width': '48%', 'display': 'inline-block', 'margin-right': '4%', 'vertical-align': 'top'}),
        
        html.Div([
            html.Label("Select Year:", 
                       style={'font-weight': 'bold', 'font-size': '18px', 'margin-bottom': '5px'}),
            dcc.Dropdown(
                id='select-year',
                options=[{'label': str(i), 'value': i} for i in year_list],
                value='Select-year',
                placeholder='Select-year',
                style={'width': '100%', 
                       'padding': '10px', 
                       'font-size': '16px',
                       'border-radius': '5px',
                       'border': '1px solid #ccc'}
            )
        ], style={'width': '48%', 'display': 'inline-block', 'vertical-align': 'top'})
    ], style={'padding': '20px', 
              'background-color': '#f9f9f9', 
              'border-radius': '10px',
              'margin-bottom': '30px',
              'box-shadow': '0 2px 4px rgba(0,0,0,0.1)'}),
    
    #TASK 2.3: Add a division for output display with proper grid styling
    html.Div(id='output-container', 
             className='chart-grid',
             style={'display': 'grid',
                    'grid-template-columns': '1fr 1fr',
                    'gap': '20px',
                    'padding': '20px'})
])

#TASK 2.4: Creating Callbacks
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value'))

def update_input_container(selected_statistics):
    if selected_statistics == 'Yearly Statistics': 
        return False  # Enable dropdown
    else: 
        return True   # Disable dropdown

# Callback for plotting
# Define the callback function to update the output container based on the selected statistics
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'), 
     Input(component_id='select-year', component_property='value')])

def update_output_container(selected_statistics, input_year):
    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
        #TASK 2.5: Create and display graphs for Recession Report Statistics

        #Plot 1 Automobile sales fluctuate over Recession Period (year wise)
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
                x='Year',
                y='Automobile_Sales',
                title="Average Automobile Sales Fluctuation over Recession Period",
                height=400))

        #Plot 2 Calculate the average number of vehicles sold by vehicle type       
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(
            figure=px.bar(average_sales,
                x='Vehicle_Type',
                y='Automobile_Sales',
                title="Average Number of Vehicles Sold by Vehicle Type",
                height=400))

        # Plot 3 Pie chart for total expenditure share by vehicle type during recessions
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(exp_rec,
                values='Advertising_Expenditure',
                names='Vehicle_Type',
                title="Total Expenditure Share by Vehicle Type During Recessions",
                height=400))

        # Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
        unemp_data = recession_data.groupby(['Vehicle_Type', 'unemployment_rate'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(
            figure=px.bar(unemp_data,
                x='unemployment_rate',
                y='Automobile_Sales',
                color='Vehicle_Type',
                labels={'unemployment_rate': 'Unemployment Rate', 
                        'Automobile_Sales': 'Average Automobile Sales'},
                title='Effect of Unemployment Rate on Vehicle Type and Sales',
                height=400))

        return [
            html.Div(R_chart1, style={'grid-column': '1', 'grid-row': '1'}),
            html.Div(R_chart2, style={'grid-column': '2', 'grid-row': '1'}),
            html.Div(R_chart3, style={'grid-column': '1', 'grid-row': '2'}),
            html.Div(R_chart4, style={'grid-column': '2', 'grid-row': '2'})
        ]

    # TASK 2.6: Create and display graphs for Yearly Report Statistics
    elif (input_year and selected_statistics == 'Yearly Statistics'):
        yearly_data = data[data['Year'] == input_year]
        
        # Plot 1: Yearly Automobile sales using line chart for the whole period.
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(
            figure=px.line(yas,
                x='Year',
                y='Automobile_Sales',
                title="Yearly Automobile Sales",
                height=400))
            
        # Plot 2 Total Monthly Automobile sales using line chart.
        mas = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        # Ensure proper month ordering
        month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        mas['Month'] = pd.Categorical(mas['Month'], categories=month_order, ordered=True)
        mas = mas.sort_values('Month')
        
        Y_chart2 = dcc.Graph(
            figure=px.line(mas,
                x='Month',
                y='Automobile_Sales',
                title=f'Total Monthly Automobile Sales in {input_year}',
                height=400))

        # Plot 3 bar chart for average number of vehicles sold during the given year
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(
            figure=px.bar(avr_vdata,
                x='Vehicle_Type',
                y='Automobile_Sales',
                title=f'Average Vehicles Sold by Vehicle Type in {input_year}',
                height=400))

        # Plot 4 Total Advertisement Expenditure for each vehicle using pie chart
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(exp_data,
                values='Advertising_Expenditure',
                names='Vehicle_Type',
                title=f'Total Advertisement Expenditure for Each Vehicle in {input_year}',
                height=400))

        return [
            html.Div(Y_chart1, style={'grid-column': '1', 'grid-row': '1'}),
            html.Div(Y_chart2, style={'grid-column': '2', 'grid-row': '1'}),
            html.Div(Y_chart3, style={'grid-column': '1', 'grid-row': '2'}),
            html.Div(Y_chart4, style={'grid-column': '2', 'grid-row': '2'})
        ]
    
    else:
        return html.Div("Please select a report type and/or year to view statistics.",
                       style={'textAlign': 'center', 
                              'padding': '50px',
                              'font-size': '18px',
                              'color': '#666',
                              'grid-column': '1 / span 2'})

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True, port=8051)