# streamlit_app.py
from turtle import pd
import pandas as pd
import joblib
import streamlit as st
import numpy as np

# Load the trained model
model = joblib.load("house_price_rf_model.pkl")

# --- CSS Styling ---
st.markdown("""
<style>
/* Page background and text color */
.stApp {
    background-color: #000000;
    color: #ffffff;
    font-family: 'Arial', sans-serif;
}

/* Input box styling */
.input-box {
    background-color: #1c1c1c;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 2px 2px 10px rgba(255,255,255,0.1);
    margin-bottom: 20px;
}

/* Button styling */
div.stButton > button:first-child {
    background-color: #2E86C1;
    color: white;
    height: 3em;
    width: 100%;
    border-radius: 10px;
    font-size: 16px;
    font-weight: bold;
}

/* Divider color */
hr {
    border: 1px solid #ffffff;
}
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='text-align:center; color:#2E86C1;'>🏠 India House Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#ffffff;'>Enter the details of the house to get an estimated price.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Input Section ---
st.markdown('<div class="input-box">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    bedrooms = st.number_input("Number of Bedrooms", min_value=0, value=3)
    bathrooms = st.number_input("Number of Bathrooms", min_value=0, value=2)

with col2:
    living_area = st.number_input("Living Area (sq ft)", min_value=100, value=2000)
    condition = st.selectbox("Condition of the House", ["Poor", "Average", "Good", "Excellent"])

schools_nearby = st.number_input("Number of Schools Nearby", min_value=0, value=3)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")

# Encode condition
condition_map = {"Poor": 0, "Average": 1, "Good": 2, "Excellent": 3}
condition_encoded = condition_map[condition]

# Predict button
if st.button("Predict Price"):
    X = pd.DataFrame([[bedrooms, bathrooms, living_area, condition_encoded, schools_nearby]],
                 columns=['number of bedrooms', 'number of bathrooms', 'living area',
                          'condition of the house', 'Number of schools nearby'])
    
    prediction = model.predict(X)
    st.markdown(f"""
    <div style='background-color:#2E86C1; color:#ffffff; padding:20px; border-radius:10px; text-align:center; font-size:20px; font-weight:bold;'>
        Estimated House Price: ₹ {prediction[0]:,.2f}
    </div>
    """, unsafe_allow_html=True)

# Index(['number of bedrooms', 'number of bathrooms', 'living area',
      # 'condition of the house', 'Number of schools nearby'],
      # dtype='object')