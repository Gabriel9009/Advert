# streamlit_app.py
import streamlit as st
import joblib
import numpy as np


# Load your trained model
model = joblib.load("Sales_model.pkl")  # or use pickle.load()

st.title("📈 Advertising Budget → Sales Predictor")

# User inputs
tv_budget = st.slider("TV Ad Budget ($)", 0, 300, 100)
radio_budget = st.slider("Radio Ad Budget ($)", 0, 50, 25)
newspaper_budget = st.slider("Newspaper Ad Budget ($)", 0, 120, 30)

# Prediction
input_data = np.array([[tv_budget, radio_budget, newspaper_budget]])
predicted_sales = model.predict(input_data)[0]

st.write(f"### 🔮 Predicted Sales: {predicted_sales:.2f} units")