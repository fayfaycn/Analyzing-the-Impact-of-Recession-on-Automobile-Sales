# Analyzing-the-Impact-of-Recession-on-Automobile-Sales
Data visualization with Python(IBM) final project:Part 1 will give you the opportunity to demonstrate your plotting and visualization skills and Part 2 is about creating and customizing dashboards.  Part 1 : Analyzing the wildfire activities in Australia Part 2 : Dashboard to display charts based on selected Region and Year
Data Description
This wildfire dataset contains data on fire activities in Australia starting from 2005. Additional information can be found here.
The dataset includes the following variables:

Region: the 7 regions
Date: in UTC and provide the data for 24 hours ahead
Estimated_fire_area: daily sum of estimated fire area for presumed vegetation fires with a confidence > 75% for a each region in km2
Mean_estimated_fire_brightness: daily mean (by flagged fire pixels(=count)) of estimated fire brightness for presumed vegetation fires with a confidence level > 75% in Kelvin
Mean_estimated_fire_radiative_power: daily mean of estimated radiative power for presumed vegetation fires with a confidence level > 75% for a given region in megawatts
Mean_confidence: daily mean of confidence for presumed vegetation fires with a confidence level > 75%
Std_confidence: standard deviation of estimated fire radiative power in megawatts
Var_confidence: Variance of estimated fire radiative power in megawatts
Count: daily numbers of pixels for presumed vegetation fires with a confidence level of larger than 75% for a given region
Replaced: Indicates with an Y whether the data has been replaced with standard quality data when they are available (usually with a 2-3 month lag). Replaced data has a slightly higher quality in terms of locations
Part 1 : Analyzing the wildfire activities in Australia
Objective:
The objective of this part of the Practice Assignment is to analyze and visualize the wildfire activities in Australia using the provided dataset. You will explore patterns and trends, and create visualizations to gain insights into the behavior of wildfires in different regions of Australia.

In this lab you will create visualizations using Matplotlib, Seaborn, Pandas and Folium.

Tasks to be performed
TASK 1.1: To understand the change in average estimated fire area over time using pandas to plot the line chart.

TASK 1.2 To plot the estimated fire area over month

TASK 1.3 Use the functionality of seaborn to develop a barplot, to find the insights on the distribution of mean estimated fire brightness across the regions

TASK 1.4 Develop a pie chart and find the portion of count of pixels for presumed vegetation fires vary across regions

TASK 1.5 Customize the previous pie plot for a better visual representation

TASK 1.6 Use Matplotlib to develop a histogram of the mean estimated fire brightness

TASK 1.7 Use the functionality of seaborn and pass region as hue, to understand the distribution of estimated fire brightness across regions

TASK 1.8 Develop a scatter plot to find the correlation between mean estimated fire radiative power and mean confidence level

TASK 1.9 Mark all seven regions affected by wildfires, on the Map of Australia using Folium

Part 2 : Dashboard to display charts based on selected Region and Year
Objective:
The objective of this part of the practice assignment is to create dashboards to contain your plots and charts.

In this lab you will create dashboards using Dash and Plotly and then add user-interactions to your dashboards.

You will be required to create a dashboard wherein the user can select the Region and the Year. Based on the selection, the dashboard will display the following two charts:-

Pie Chart on Monthly Average Estimated Fire Area
Bar Chart on Monthly Average Count of Pixels for Presumed Vegetation Fires
Tasks to be performed
TASK 2.1 Add title to the dashboard

TASK 2.2 Add the radio items and a dropdown right below the first inner division

TASK 2.3 Add two empty divisions for output inside the next inner division

TASK 2.4 Add the Ouput and input components inside the app.callback decorator

TASK 2.5 Add the callback function

