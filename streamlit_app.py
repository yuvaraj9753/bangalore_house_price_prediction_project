import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load Model + Data
ridge_model = pickle.load(open("ridge_model.pkl", "rb"))
clean_data = pd.read_csv("Cleaned_data.csv")

locations = sorted(clean_data["location"].unique())

st.set_page_config(page_title="Bangalore House Price Predictor", layout="centered")

st.title("🏡 Bangalore House Price Prediction")

location = st.selectbox("Location", locations)
total_sqft = st.number_input("Total Square Feet", 300.0, 10000.0, 1000.0, 10.0)
bath = st.number_input("Bathrooms", 1, 10, 2, 1)
bhk = st.number_input("BHK", 1, 10, 2, 1)


# ============================
# NEW FIXED PREPROCESSOR
# ============================
def preprocess_input(location, sqft, bath, bhk):
    df = pd.DataFrame([{
        "location": location,
        "total_sqft": float(sqft),
        "bath": float(bath),
        "bhk": int(bhk)
    }])
    return df


# Predict
if st.button("Predict Price"):
    try:
        x_input = preprocess_input(location, total_sqft, bath, bhk)
        prediction = ridge_model.predict(x_input)[0]

        st.success(f"Estimated Price: ₹ {round(prediction, 2)} Lakhs")

    except Exception as e:
        st.error(f"Error: {e}")
