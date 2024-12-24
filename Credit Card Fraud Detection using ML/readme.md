## Overview
This project aims to detect fraudulent credit card transactions using various machine learning algorithms. The dataset used for this project contains transactions made by European cardholders in September 2013. The dataset is highly unbalanced, with only 0.172% of transactions being fraudulent.

## Dataset
The dataset includes the following features:
- **Time**: The seconds elapsed between each transaction and the first transaction in the dataset.
- **V1, V2, ..., V28**: Principal components obtained using PCA.
- **Amount**: The transaction amount.
- **Class**: The response variable (1 for fraud, 0 otherwise).

## Dependencies
- Python 3
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

## Exploratory Data Analysis (EDA)
The EDA includes:
- Checking for missing values.
- Analyzing the distribution of the `Class` variable.
- Visualizing the amount per transaction by class.
- Analyzing the time of transaction vs. amount by class.

## Outlier Detection Methods
The following outlier detection methods are used:
- **Isolation Forest**
- **Local Outlier Factor**
- **Support Vector Machine**

## Results
- **Isolation Forest** detected 73 errors with an accuracy of 99.74%.
- **Local Outlier Factor** detected 97 errors with an accuracy of 99.65%.
- **Support Vector Machine** detected 8516 errors with an accuracy of 70.09%.

## Conclusion
The Isolation Forest method performed the best in detecting fraudulent transactions, with an accuracy of 99.74%. Further improvements can be made by increasing the sample size or using deep learning algorithms.

## Acknowledgements
The dataset was collected and analyzed during a research collaboration between Worldline and the Machine Learning Group (http://mlg.ulb.ac.be) of ULB (Université Libre de Bruxelles).

## References
- [Worldline and ULB Collaboration](https://www.researchgate.net/project/Fraud-detection-5)
- [DefeatFraud Project](https://www.researchgate.net/project/Fraud-detection-5)



