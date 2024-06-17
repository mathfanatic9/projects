# Chest X-Ray Image Prediction Using Deep Learning

### Overview
This project applies deep learning to medical science, aiming to predict pneumonia from chest X-ray images. The dataset is sourced from Kaggle and contains images categorized as Pneumonia or Normal.

### Dataset
1. Source: Kaggle (Paul Mooney)
2. Content: 5,863 X-Ray images (JPEG), 2 categories (Pneumonia/Normal)
3. URL: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

### Model
The model is built using the VGG16 architecture, leveraging transfer learning with weights from ImageNet. It is trained to classify images into two categories: Normal and Pneumonia.

### Usage
1. Download the dataset from Kaggle.
2. Load the data and preprocess it using the provided code.
3. Initialize the VGG16 model with pre-trained ImageNet weights.
4. Compile and fit the model using the training set.
5. Evaluate the model's performance on the test set.

### Results
The model achieved an accuracy of 91% on the validation set, indicating its effectiveness in classifying chest X-ray images for pneumonia detection.
