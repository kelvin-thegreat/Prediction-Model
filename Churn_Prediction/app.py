# Gender -> 1 Female 0 Male
# Churn -> 1 Yes 0 No
# Scaler exported as scaler.pkl 
# Model is exported as model.pkl 
# order of the X columns -> 'Age', 'Gender', 'Tenure', 'MonthlyCharges'

import streamlit as st
import joblib
import numpy as np  
import pandas as pd

# Load the scaler and model 
scaler = joblib.load('scaler.pkl')  # Load the scaler
model = joblib.load('model.pkl')  # Load the model

st.title("Churn Prediction Web App")

st.divider()

st.write("Please enter the values and hit the predict button for getting a prediction.")

st.divider()    

age = st.number_input("Enter Age", min_value=10, max_value=100, value=30) 
tenure = st.number_input("Enter Tenure", min_value=0, max_value=130, value=10)
monthly_charges = st.number_input("Enter Monthly Charges", min_value=30, max_value=150)
gender = st.selectbox("Enter the Gender", ["Male", "Female"])

st.divider() 

predict_button = st.button("Predict") 

if predict_button:
    # Convert
    gender_selected = 1 if gender == "Female" else 0

    X = [age, gender_selected, tenure, monthly_charges]

    columns = ['Age', 'Gender', 'Tenure', 'MonthlyCharges']
    # Create a DataFrame with the feature vector and column names
    # This ensures that the feature vector has the same structure as the training data
    X_df = pd.DataFrame([X], columns=columns)  # Create DataFrame with column names
    X_array = scaler.transform(X_df)  # Scale the feature vector
    prediction = model.predict(X_array)[0]
    predicted = "Yes" if prediction == 1 else "No"

    st.balloons()
    st.success("Prediction made successfully!")

    st.write(f"Predicted: {predicted}")

else:
    st.write("Please enter the values and use the predict button.")
