# Fake News Classifier Using Bidirectional LSTM

## Overview
This project aims to build a Fake News Classifier using a Bidirectional Long Short-Term Memory (LSTM) model. The classifier is trained to distinguish between fake and real news articles based on their content.

## Dataset
The dataset used for this project contains news articles labeled as fake or real. It includes the following columns:
- `id`: Unique identifier for each article
- `title`: Title of the article
- `author`: Author of the article
- `text`: Full text of the article
- `label`: Label indicating whether the article is fake (1) or real (0)

## Steps
1. **Data Preprocessing**:
   - Drop missing values
   - Extract independent (`X`) and dependent (`y`) features
   - Tokenize and clean the text data
   - Create a corpus of stemmed words

2. **Model Building**:
   - Define the vocabulary size
   - Convert text data to one-hot representations
   - Pad sequences to ensure uniform input length
   - Build a Bidirectional LSTM model using TensorFlow and Keras
   - Compile and train the model

3. **Evaluation**:
   - Evaluate the model's performance using precision, recall, and F1-score
   - Generate a classification report

## Requirements
- Python 3.x
- Pandas
- NumPy
- TensorFlow
- Keras
- NLTK

## Results
The model achieves a high accuracy in classifying news articles as fake or real. Detailed evaluation metrics are provided in the notebook.

