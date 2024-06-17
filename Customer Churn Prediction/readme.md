# Customer Exit Prediction from Bank using ANN 

### Project Overview
This project involves the development of an Artificial Neural Network (ANN) to predict whether a customer will leave the bank or not. It includes data preprocessing, creation of dummy variables, feature scaling, and model training using Keras.

### Data Preprocessing
- The dataset is imported using pandas.
- Dummy variables are created for categorical features 'Geography' and 'Gender'.
- Feature matrix `X` and target vector `y` are prepared from the processed dataset.

### Model Architecture
- The ANN consists of an input layer with 8 features, two hidden layers with 6 neurons each, and an output layer with 1 neuron.
- Activation functions used are ReLU for hidden layers and sigmoid for the output layer.
- The model is compiled with the Adam optimizer and binary cross-entropy loss function.

### Training
The model is trained on the preprocessed training set for 100 epochs with a batch size of 10.

### Evaluation
- Predictions are made on the test set, and a confusion matrix is created using seaborn for better visualization.
- The accuracy score is calculated to evaluate the model's performance.
- Classification report is provided to understand precision, recall, and F1-score for each class.

### License
This project is open-sourced under the MIT license.
