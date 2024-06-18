# Wine Quality Prediction using ML Models

### Overview
This project aims to predict the quality of wine based on various physicochemical features using machine learning models.

### Dataset
The dataset used is `wine quality dataset.csv`, which includes fundamental features affecting wine quality.

### Preprocessing
Data preprocessing steps include:
- Handling null values.
- Feature selection based on correlation.
- Data normalization using `MinMaxScaler`.

### Model Training
Several models were trained, including Logistic Regression, XGBoost, and SVC. Model performance was evaluated using ROC AUC scores.

### Results
The XGBoost classifier showed a high training accuracy, while Logistic Regression and SVC performed better on validation data.

### License
This project is open-sourced under the MIT license.
