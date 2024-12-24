## Overview
This project aims to predict loan defaults using various machine learning algorithms. The dataset used for this project contains information about borrowers and their loan details. The goal is to build a model that can accurately predict whether a borrower will default on their loan.

## Dataset
The dataset includes the following features:
- **Id**: Unique identifier for each borrower.
- **Age**: Age of the borrower.
- **Income**: Annual income of the borrower.
- **Home**: Home ownership status (RENT, OWN, MORTGAGE, OTHER).
- **Emp_length**: Length of employment in years.
- **Intent**: Purpose of the loan (PERSONAL, EDUCATION, MEDICAL, VENTURE, HOMEIMPROVEMENT, DEBTCONSOLIDATION).
- **Amount**: Loan amount.
- **Rate**: Interest rate of the loan.
- **Status**: Loan status (0 for non-default, 1 for default).
- **Percent_income**: Percentage of income used for loan repayment.
- **Default**: Target variable (1 for default, 0 otherwise).
- **Cred_length**: Length of credit history in years.

## Exploratory Data Analysis (EDA)
The EDA includes:
- Checking for missing values.
- Analyzing the distribution of the `Default` variable.
- Visualizing the distribution of features like Age, Income, Loan Amount, Interest Rate, Home Ownership, and Loan Intent.
- Analyzing the relationship between features and the target variable `Default`.

## Data Preprocessing
- Handling missing values using SimpleImputer.
- Encoding categorical variables using one-hot encoding.
- Scaling numerical features using StandardScaler.
- Applying SMOTE to handle class imbalance.

## Models
The following machine learning models are used:
- **Logistic Regression**
- **Decision Tree**
- **Random Forest**
- **Gradient Boosting**
- **Support Vector Machine (SVM)**
- **K-Nearest Neighbors (KNN)**

## Results
- **Logistic Regression**: High accuracy in detecting defaults.
- **Decision Tree**: Good performance with interpretable results.
- **Random Forest**: Robust model with high accuracy.
- **Gradient Boosting**: High accuracy with good generalization.
- **SVM**: Effective in high-dimensional spaces.
- **KNN**: Simple and effective for small datasets.

## Conclusion
The Logistic Regression model performed the best in predicting loan defaults, with high accuracy and good generalization. Further improvements can be made by tuning hyperparameters or using more advanced models.

