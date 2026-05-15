# 🌾 Rice Leaf Disease Detector

A deep learning-based project that detects diseases in rice leaves using a Convolutional Neural Network (CNN) and provides real-time predictions through a Streamlit web application.

---

## 🚀 Overview

Rice crops are highly vulnerable to bacterial, viral, and fungal diseases, which significantly impact yield and food security. Early detection is crucial for effective treatment and prevention.

This project aims to:
- Automatically classify rice leaf diseases from images
- Provide a simple UI for real-time predictions
- Assist farmers and researchers with quick diagnosis

---

## 🧠 Model Details

- Model Type: Convolutional Neural Network (CNN)
- Input Size: 180 × 180 RGB images
- Classes:
  - Bacterial Leaf Blight
  - Brown Spot
  - Leaf Smut



---

## 📁 Dataset

- Total Images: 120
- Classes: 3
- Images per class: 40

The dataset is split into:
- Training set
- Validation set
- Test set

---

## ⚙️ Project Pipeline

1. Data Loading  
2. Data Preprocessing  
3. Data Augmentation  
4. Model Building (CNN)  
5. Model Training  
6. Evaluation  
7. Testing  
8. Deployment (Streamlit UI)

---

## 💻 Streamlit Web App

The project includes a user-friendly web interface where users can:

- Upload an image of a rice leaf
- Get instant disease prediction
- View prediction confidence

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/DaveGH143/miniproject-clg.git
cd miniproject-clg
