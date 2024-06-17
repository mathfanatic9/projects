# Handwritten Digits Classification using CNN

## Overview:
This project involves the classification of handwritten digits using a Convolutional Neural Network (CNN) model. The model is trained and evaluated on the MNIST dataset, which consists of 60,000 training images and 10,000 test images of handwritten digits.

Model Architecture:
The CNN model consists of an input layer, a convolutional layer with 30 filters of size 3x3, a max pooling layer, a flattening layer, and two dense layers. The final dense layer uses a sigmoid activation function to output the classification probabilities for each digit class.

Training:
The model is compiled with the Adam optimizer and sparse categorical crossentropy loss function. It is trained for 5 epochs, achieving an accuracy of approximately 99.49% on the training set.

Evaluation:
Upon evaluation on the test set, the model achieves an accuracy of 98.59%, demonstrating its effectiveness in classifying handwritten digits.

Usage:
To use this model, ensure you have TensorFlow and Keras installed. Load the MNIST dataset, preprocess the data by normalizing and reshaping it, and then compile and fit the model as described in the code snippets provided.
