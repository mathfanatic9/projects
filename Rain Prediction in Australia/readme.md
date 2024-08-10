# Rain Prediction in Australia

This project aims to predict if it will rain tomorrow in various locations across Australia using historical weather data. 

### About the Data
The dataset is sourced from the Australian Government's Bureau of Meteorology and the latest data can be gathered from http://www.bom.gov.au/climate/dwo/. The dataset to be used has extra columns like 'RainToday' and our target is 'RainTomorrow', which was gathered from the Rattle at https://bitbucket.org/kayontoga/rattle/src/master/data/weatherAUS.RData. Overall it contains daily weather observations from 2008 to 2017, including metrics such as temperature, rainfall, humidity, and wind speed. The target variable is `RainTomorrow`, indicating whether or not it will rain the next day.The weatherAUS.csv dataset includes the following fields with the column definitions gathered from http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml:

| **Field**       | **Description**                                  | **Unit**         | **Type**   |
|-----------------|--------------------------------------------------|------------------|------------|
| Date            | Date of the Observation in YYYY-MM-DD            | Date             | object     |
| Location        | Location of the Observation                      | Location         | object     |
| MinTemp         | Minimum temperature                              | Celsius          | float      |
| MaxTemp         | Maximum temperature                              | Celsius          | float      |
| Rainfall        | Amount of rainfall                               | Millimeters      | float      |
| Evaporation     | Amount of evaporation                            | Millimeters      | float      |
| Sunshine        | Amount of bright sunshine                        | hours            | float      |
| WindGustDir     | Direction of the strongest gust                  | Compass Points   | object     |
| WindGustSpeed   | Speed of the strongest gust                      | Kilometers/Hour  | object     |
| WindDir9am      | Wind direction averaged of 10 minutes prior to 9am| Compass Points   | object     |
| WindDir3pm      | Wind direction averaged of 10 minutes prior to 3pm| Compass Points   | object     |
| WindSpeed9am    | Wind speed averaged of 10 minutes prior to 9am   | Kilometers/Hour  | float      |
| WindSpeed3pm    | Wind speed averaged of 10 minutes prior to 3pm   | Kilometers/Hour  | float      |
| Humidity9am     | Humidity at 9am                                  | Percent          | float      |
| Humidity3pm     | Humidity at 3pm                                  | Percent          | float      |
| Pressure9am     | Atmospheric pressure reduced to mean sea level at 9am | Hectopascal | float      |
| Pressure3pm     | Atmospheric pressure reduced to mean sea level at 3pm | Hectopascal | float      |
| Cloud9am        | Fraction of the sky obscured by cloud at 9am     | Eights           | float      |
| Cloud3pm        | Fraction of the sky obscured by cloud at 3pm     | Eights           | float      |
| Temp9am         | Temperature at 9am                               | Celsius          | float      |
| Temp3pm         | Temperature at 3pm                               | Celsius          | float      |
| RainToday       | If there was rain today                          | Yes/No           | object     |
| RainTomorrow    | If there is rain tomorrow                        | Yes/No           | float      |

### Models and Evaluation
The following classification algorithms were used:
- **Linear Regression**
- **K-Nearest Neighbors (KNN)**
- **Decision Tree**
- **Logistic Regression**
- **Support Vector Machine (SVM)**

Evaluation metrics include:
- **Accuracy Score**
- **Jaccard Index**
- **F1-Score**
- **Log Loss** (for Logistic Regression)
- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **R2-Score**

### Results
The models were evaluated based on their performance metrics. The Logistic Regression seems to be the most effective model for this dataset.

### License
This project is licensed under the MIT License.
