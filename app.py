import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import json
import gdown

# Google Drive file IDs
MODEL_FILE_ID = '1-BAD6lGU2i8QzK3GeKi78uOw0cVApaNv'  # Actual model file ID
CLASS_INDICES_FILE_ID = '10F32kdZtjZg44MNYtHt827dje_cuQNyI'  # Actual class indices file ID

# Download files from Google Drive
gdown.download(f'https://drive.google.com/uc?id={MODEL_FILE_ID}', 'Plant_Disease_Prediction_System.h5', quiet=False)
gdown.download(f'https://drive.google.com/uc?id={CLASS_INDICES_FILE_ID}', 'class_indices.json', quiet=False)

# Load the trained model
model = load_model('Plant_Disease_Prediction_System.h5')

# Load class names from the JSON file
with open('class_indices.json') as f:
    class_names = json.load(f)

# Define the Streamlit app
st.set_page_config(
    page_title="Plant Disease Prediction",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🌿 Plant Disease Prediction 🌿")
st.markdown(
    '''
    <style>
    .main {
        background-color: #f0f2f6;
    }
    h1 {
        color: #4CAF50;
        text-align: center;
    }
    .custom-upload-text {
        color: black !important;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# Custom CSS for the uploader text
st.markdown(
    '''
    <style>
    .stFileUploader label {
        color: black !important;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

st.write('<span class="custom-upload-text">Upload an image to classify</span>', unsafe_allow_html=True)

uploaded_file = st.file_uploader('Choose an image...', type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess the image to fit the model input requirements
    size = (150, 150)  # Set the desired image size
    image = ImageOps.fit(image, size, Image.LANCZOS)
    image_array = np.asarray(image)
    image_array = np.expand_dims(image_array, axis=0)  # Create batch dimension
    image_array = image_array / 255.0  # Normalize the image

    # Make prediction
    prediction = model.predict(image_array)
    predicted_class = class_names[str(np.argmax(prediction))]
    confidence = np.max(prediction)

    st.markdown(f'<div style="background-color:#0f0f0f;padding:10px;border-radius:10px;"><span style="color:#f2fa0f;font-weight:bold;">Prediction:</span> {predicted_class}</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="background-color:#111211;padding:10px;border-radius:10px;"><span style="color:#43bd06;font-weight:bold;">Confidence:</span> {confidence:.2f}</div>', unsafe_allow_html=True)

    st.balloons()
