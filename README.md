# Bahraini Currency Recognition with Deep Learning

## 📌 Overview

**Bahraini Currency Recognition** is a deep learning project designed to recognize Bahraini currency from images.

The project uses a trained deep learning classification model to identify the currency class from an uploaded image or a photo taken using a camera.

The project includes a trained model, a Jupyter Notebook for model development, and a Streamlit application for real-world testing and prediction.

## 🎯 Project Objective

The main objective of this project is to build an AI-based system that can recognize different Bahraini currency classes from images.

The project follows an image classification approach where the system answers:

> **"What currency is shown in this image?"**

## 💰 Currency Classes

The current application supports **9 currency classes**:

| Class | Currency |
| ----- | -------- |
| 1     | 0.05     |
| 2     | 0.100    |
| 3     | 0.25     |
| 4     | 0.5 BD   |
| 5     | 0.50     |
| 6     | 10 BD    |
| 7     | 1BD      |
| 8     | 20 BD    |
| 9     | 5 BD     |

## 🧠 How the System Works

The prediction pipeline follows these steps:

1. Upload an image or take a photo using the camera.
2. Convert the image to RGB format.
3. Resize the image to **224 × 224 pixels**.
4. Normalize the pixel values.
5. Pass the processed image to the trained deep learning model.
6. Predict the currency class.
7. Display the predicted currency and confidence score.
8. Display the probabilities for the currency classes.

## 🖥️ Live Demo

Try the application here:

👉 **[Bahraini Currency Recognition – Live Demo](https://bahrainicurrency.streamlit.app/)**

The application is built using **Streamlit** and allows users to upload a currency image or take a photo using their camera.

## 📂 Project Structure

```text
bahraini_currency/
│
├── Currency/
│   ├── 0.05/
│   ├── 0.100/
│   ├── 0.25/
│   ├── 0.5 BD/
│   ├── 0.50/
│   ├── 10 BD/
│   ├── 1BD/
│   ├── 20 BD/
│   └── 5 BD/
│
├── currency_model.keras
│   └── Trained deep learning model
│
├── money_app.py
│   └── Streamlit application
│
├── work_money_no_drive.ipynb
│   └── Model development and training notebook
│
├── requirements.txt
│   └── Required Python libraries
│
└── README.md
    └── Project documentation
```

## 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Pandas
* Pillow (PIL)
* Streamlit
* Jupyter Notebook

## ⚙️ Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Run the Streamlit application using:

```bash
streamlit run money_app.py
```

The application will open in your browser.

## 📸 Image Recommendations

For better prediction results:

* Use a clear image.
* Make sure the currency is fully visible.
* Use good lighting.
* Avoid excessive blur.
* Try different backgrounds and angles.

## 📊 Model Evaluation

The project evaluates the model using:

* Accuracy
* Confusion Matrix
* Precision and Recall
* Per-class performance
* Error analysis

The evaluation results are based on the experiments performed during model development.

## 🌍 Real-World Testing

The system can be tested using:

* Mobile phone photos
* Live camera input through the Streamlit application
* Images with different backgrounds
* Different angles and distances
* Different lighting conditions

## ⚠️ Limitations

Image classification can be affected by:

* Poor lighting
* Blurry images
* Different backgrounds
* Camera angles
* Similar-looking currency classes
* Images that are different from the training data

Therefore, real-world testing is important to understand the model's limitations.

## 🚀 Future Improvements

Possible future improvements include:

* Increasing the size and diversity of the dataset.
* Adding more real-world images.
* Improving performance on unseen backgrounds.
* Improving recognition of visually similar currency classes.
* Adding front-versus-back detection.
* Extending the system to detect and count multiple currencies in one image.

## 👩🏻‍💻 Project

**Bahraini Currency Recognition with Deep Learning**

### 🔗 Live Demo

[Try the Bahraini Currency Recognition App](https://bahrainicurrency.streamlit.app/)
