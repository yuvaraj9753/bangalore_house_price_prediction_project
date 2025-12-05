🏡 Bangalore House Price Prediction

A Machine Learning project to predict house prices in Bangalore using regression models and a clean Streamlit interface.

📌 Project Overview

This project aims to build a ML-based system that predicts house prices in Bangalore based on essential property features like location, total square footage, BHK, and bathrooms.
It includes end-to-end development: data cleaning, feature engineering, model building, model evaluation, and deployment using Streamlit.

✨ Features

✔️ Clean and processed real-estate dataset

✔️ Outlier removal + feature engineering

✔️ One-hot encoding for high-cardinality locations

✔️ Regression models: Linear, Lasso, Ridge

✔️ Selected best model using cross-validation

✔️ Model saved as .pkl for deployment

✔️ Streamlit web app for real-time prediction

📂 Project Structure
├── data/
│   └── Cleaned_data.csv
├── model/
│   └── RidgeModel.pkl
├── app.py                 # Streamlit app
├── notebook.ipynb         # EDA + Model training
├── requirements.txt
└── README.md

🔧 Technologies Used

Python

NumPy, Pandas

Scikit-learn

Matplotlib / Seaborn

Streamlit

Pickle

📊 Model Building

Performed Exploratory Data Analysis (EDA)

Cleaned the dataset by removing missing values, incorrect formats, and extreme outliers

Encoded location using OneHotEncoder

Tested multiple regression models

Final model: Ridge Regression (best performance + stability)

Saved model as RidgeModel.pkl

🌐 Deployment (Streamlit App)

Users can:

Select location

Enter square footage

Choose BHK + bathrooms

Get an instant predicted price in lakhs or crores

Run locally:
