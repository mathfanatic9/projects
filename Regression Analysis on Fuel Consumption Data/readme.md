# Regression Analysis on Fuel Consumption Data
 
## 1) Simple Linear Regression Analysis on Fuel Consumption Data

### Overview
This project focuses on analyzing fuel consumption data to predict carbon dioxide emissions of vehicles. The dataset contains model-specific fuel consumption ratings and estimated CO2 emissions for new light-duty vehicles for retail sale in Canada.

### Dataset
The dataset, `FuelConsumption.csv`, is a fuel consumption dataset which contains model-specific fuel consumption ratings and estimated carbon dioxide emissions for new light-duty vehicles for retail sale in Canada. It is obtained from http://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64 and includes the following attributes:
- **MODELYEAR**: e.g., 2014
- **MAKE**: e.g., Acura
- **MODEL**: e.g., ILX
- **VEHICLE CLASS**: e.g., SUV
- **ENGINE SIZE**: e.g., 4.7
- **CYLINDERS**: e.g., 6
- **TRANSMISSION**: e.g., A6
- **FUEL CONSUMPTION** in various metrics (L/100 km)
- **CO2 EMISSIONS** (g/km)

### Usage
Perform data loading, exploration, visualization, model training, and evaluation.

### Model
The project utilizes a simple linear regression model to understand the relationship between engine size and CO2 emissions.

### Evaluation
The model's performance is evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared score.

## 2) Multiple Linear Regression Analysis

## Overview
This project involves the implementation of a Multiple Linear Regression model using scikit-learn to predict CO2 emissions based on various vehicle characteristics.

### Dataset
The dataset includes the following attributes:
- `ENGINESIZE`
- `CYLINDERS`
- `FUELCONSUMPTION_CITY`
- `FUELCONSUMPTION_HWY`
- `FUELCONSUMPTION_COMB`
- `CO2EMISSIONS`
  
### Objectives
- Utilize scikit-learn for Multiple Linear Regression.
- Train and test a model with the provided dataset.
- Understand the impact of different features on CO2 emissions.

### Model Training and Evaluation
The model is trained using 80% of the data and tested with the remaining 20%. The performance is evaluated using Mean Squared Error (MSE) and Variance score.

### Results
The model demonstrates how different features can predict the CO2 emissions with a certain level of accuracy.

