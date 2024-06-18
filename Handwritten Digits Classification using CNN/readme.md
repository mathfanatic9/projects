# Handwritten Digits Classification with ANN and CNN

## Overview
This project aims to classify handwritten digits using Artificial Neural Networks (ANN) and Convolutional Neural Networks (CNN) with the MNIST dataset.

## Dataset
The MNIST dataset contains 70,000 images of handwritten digits, each of 28x28 pixel resolution. The dataset is split into 60,000 training images and 10,000 test images.

## Models
- **ANN Model**: A simple neural network with one input layer, two hidden layers, and one output layer.
- **CNN Model**: A convolutional neural network with convolutional layers, max pooling, and dense layers.

## Training
The models are trained using the training set with normalized pixel values ranging between 0 and 1. The ANN model is trained for 25 epochs, and the CNN model for 5 epochs.

## Evaluation
The models' performance is evaluated using the test set. The accuracy and loss metrics are plotted to assess the models' learning progress.

## Results
The CNN model outperforms the ANN model, achieving an accuracy of over 98%, demonstrating its effectiveness in classifying handwritten digits.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request.
