# Fashion Recommendation System

### Overview
The Fashion Recommendation System is designed to provide similar fashion images based on a user-uploaded image. It leverages pre-trained deep learning models for feature extraction and K-Nearest Neighbors (KNN) for similarity search. Users can upload an image, and the system will recommend visually similar fashion items from the dataset which includes many categories such as shoes, hats, swimming caps, balls, bags, shorts, t-shirts, gym wear, water bottles, home wear, churidars, sarees and handbags.

### Project Components

1. **Feature Extraction (app.py):**
   - Loads a pre-trained ResNet50 model pre-trained on ImageNet.
   - Removes the top layer and adds a GlobalMaxPooling2D layer.
   - Processes input images (located in the 'images' folder) and extracts features.
   - Normalizes the feature vectors.
   - Saves the feature vectors and corresponding filenames as pickle files ('embeddings.pkl' and 'filenames.pkl').

2. **Similarity Search (test.py):**
   - Loads the saved feature vectors and filenames.
   - Loads the ResNet50 model.
   - Preprocesses a test image and extracts its features.
   - Computes the normalized feature vector for the test image.
   - Uses KNN to find the 5 most similar images.
   - Displays the similar images using OpenCV.

3. **Web Application (main.py):**
   - Utilizes Streamlit to create a user-friendly interface.
   - Allows users to upload an image.
   - Extracts features from the uploaded image.
   - Recommends visually similar fashion items.
   - Displays the recommendations alongside the uploaded image.

### Conclusion
Users can view the recommendations alongside their uploaded image. The system can be further enhanced by incorporating user feedback, fine-tuning hyperparameters, and expanding the dataset.
