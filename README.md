# Plant Disease Prediction System 🌿

This project is a Plant Disease Detection System that uses a trained TensorFlow model to identify plant diseases from uploaded images. The web application is built with Streamlit and deployed on Render.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Deployment](#deployment)
- [Contributing](#contributing)

## Overview

The Plant Disease Prediction System helps users identify diseases in plants by uploading images. The system leverages a convolutional neural network (CNN) model trained on a dataset of plant disease images.

## Features

- Upload plant images for disease prediction
- Display predicted disease and confidence score
- Simple and user-friendly interface

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/plant-disease-prediction.git
    cd plant-disease-prediction
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the app:**
    ```sh
    streamlit run app.py
    ```

## Usage

- Visit the deployed web app [here]((https://kwambekmurombeka-plant-disease-detection.onrender.com/)).
- Upload an image of a plant leaf.
- The system will display the predicted disease and confidence score.

## Model Training

The model was trained using TensorFlow on a dataset of plant disease images. The dataset includes various types of plant diseases and healthy plant images.

## Deployment

The app is deployed on Render. To deploy it yourself:

1. Create a GitHub repository and upload the project files.
2. Connect the repository to Render and set up a new web service with the following commands:
    - **Build Command:** `pip install -r requirements.txt`
    - **Start Command:** `streamlit run app.py`
3. Render will automatically build and deploy the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
