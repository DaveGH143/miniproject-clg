

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Page config
st.set_page_config(
    page_title="Rice Leaf Disease Detector",
    page_icon="🌾",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.stTitle {
    text-align: center;
    color: #4CAF50;
}
.result-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #1c1f26;
    text-align: center;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.h5")
model = tf.keras.models.load_model(model_path)

class_names = ['Bacterial leaf blight', 'Brown spot', 'Leaf smut']

# Title
st.markdown("<h1 style='text-align: center;'>🌾 Rice Leaf Disease Detector</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Upload a rice leaf image and let AI detect the disease</p>", unsafe_allow_html=True)

st.divider()

# Upload
uploaded_file = st.file_uploader("📤 Upload a leaf image", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1,1])

    with col1:
        st.image(image, caption="📷 Uploaded Image", use_column_width=True)

    with col2:
        with st.spinner("🔍 Analyzing image..."):
            img = image.resize((180,180))
            img = np.array(img)/255.0
            img = np.expand_dims(img, axis=0)

            prediction = model.predict(img)
            idx = np.argmax(prediction)
            confidence = float(np.max(prediction) * 100)

        st.markdown("###  Prediction Result")

        st.success(f"{class_names[idx]}")

        st.markdown("###  Confidence")
        st.progress(int(confidence))

        st.info(f"{confidence:.2f}% confidence")

        if confidence < 60:
            st.warning("⚠️ Low confidence. Try a clearer image.")
