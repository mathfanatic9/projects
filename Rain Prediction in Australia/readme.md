# Rain Prediction in Australia

This project aims to predict if it will rain tomorrow in various locations across Australia using historical weather data. The dataset is sourced from the Australian Government's Bureau of Meteorology.

### About the Data
The dataset contains daily weather observations from 2008 to 2017, including metrics such as temperature, rainfall, humidity, and wind speed. The target variable is `RainTomorrow`, indicating whether it will rain the next day.

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
The models were evaluated based on their performance metrics. The Logistic Regression model achieved the highest accuracy score of 83.82%. It performed the best overall with the highest accuracy and F1-Score. KNN also showed strong performance with a high accuracy score.

### License
This project is licensed under the MIT License.
