# Stock Prediction using LSTM Recurrent Neural Network

### Overview
This project aims to predict stock prices using a Long Short-Term Memory (LSTM) Recurrent Neural Network (RNN). The model is trained on historical stock price data and is capable of making predictions based on patterns observed in the past.

### Data Preprocessing
- Data is scaled using MinMaxScaler to normalize the values within a range of 0 to 1.
- A data structure with 60 timesteps is created, which means the RNN will use the past 60 days' stock prices to predict the next day's price.

### Model Architecture
- The RNN model is built using the Sequential API from TensorFlow's Keras.
- It consists of multiple LSTM layers with Dropout regularization to prevent overfitting.
- The final layer is a Dense layer with a single unit to output the predicted stock price.

### Training
- The model is compiled with the 'adam' optimizer and 'mean_squared_error' loss function.
- It is trained for 100 epochs with a batch size of 32.

### Prediction and Visualization
- The trained model is used to predict stock prices for the year 2017.
- Predictions are visualized alongside the actual stock prices for comparison.

### License
This project is open-sourced under the MIT license.
