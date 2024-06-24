import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

# create resnet model, include weights from imagenet
model = ResNet50(weights='imagenet', include_top=False, input_shape=(224,224,3))
model.trainable = False

# add top layer
model = tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])

from PIL import Image
import numpy as np
from numpy.linalg import norm
import os

def extract_features(img_path, model):
    img = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    result = model.predict(preprocessed_img).flatten()
    normalized_result = result/norm(result)

    return normalized_result

filenames=[]
for file in os.listdir('images'):
    filenames.append(os.path.join('images', file))

feature_list =[] #2D list
from tqdm import tqdm
for file in tqdm(filenames):
    feature_list.append(extract_features(file,model))

import pickle
pickle.dump(feature_list, open('embeddings.pkl', 'wb'))
pickle.dump(filenames, open('filenames.pkl', 'wb'))









