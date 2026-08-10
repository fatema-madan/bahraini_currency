
import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

model = tf.keras.models.load_model("currency_model.keras")

class_names = ['0.05', '0.100', '0.25', '0.5 BD', '0.50', '10 BD', '1BD', '20 BD', '5 BD']

st.title("Bahraini Currency Recognition")

uploaded_file = st.file_uploader("Upload a currency image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array)
    predicted_class = np.argmax(prediction[0])
    confidence = prediction[0][predicted_class]

    st.write("Prediction:", class_names[predicted_class])
    st.write("Confidence:", float(confidence))
