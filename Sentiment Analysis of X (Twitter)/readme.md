# Sentiment Analysis of Tweets 

This project aims to perform sentiment analysis on tweets from the X platform (previously known as Twitter) using machine learning techniques. The dataset used is the Sentiment140 dataset from Kaggle.

### Steps

1. **Data Collection:** The Sentiment140 dataset is downloaded from Kaggle using the Kaggle API.
2. **Data Preprocessing:**
   - The tweets are extracted from the downloaded zip file.
   - The dataset is loaded into a pandas DataFrame and preprocessed:
     - Column names are assigned.
     - Missing values are checked.
     - Target labels are converted to binary (0 for negative, 1 for positive).
     - Stemming is applied to reduce words to their root form.
3. **Feature Extraction:**
   - The preprocessed tweets are converted to numerical data using TF-IDF vectorization.
4. **Model Training:**
   - The dataset is split into training and testing sets.
   - A logistic regression model is trained on the training data.
5. **Evaluation:**
   - The trained model is evaluated on the testing data using accuracy score.

### Dependencies

- Python 3
- Libraries: numpy, pandas, re, nltk, sklearn

### Results

- The accuracy score of the trained model on the testing data is 77.8%.
