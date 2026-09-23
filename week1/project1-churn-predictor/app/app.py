import streamlit as st
import pandas as pd
import joblib 
import shap 
import matplotlib.pyplot as plt

import sys
sys.path.append(r"R:\AI_BOOTCAMP\week1\project1-churn-predictor\src")
from preprocess import preprocess


#loading model from joblib
model= joblib.load(r"R:\AI_BOOTCAMP\week1\project1-churn-predictor\models\churn_model.pkl")

st.title("Telco Customer Churn Predictor")

uploaded_file = st.file_uploader("Upload Your Data-Set Here in CSV form")
if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    df = preprocess(df)
    st.subheader("Uploaded Data")
    st.dataframe(df.head())
    df_clean = df.copy()  # copy before adding prediction columns
    predictions = model.predict(df)
    probabilities = model.predict_proba(df)[:, 1]

    df['Churn Prediction'] = predictions
    df['Churn Probability'] = probabilities
    st.subheader("Prediction Results")
    df['Churn Prediction'] = df['Churn Prediction'].replace({0: 'No', 1: 'Yes'})
    st.dataframe(df[['Churn Prediction', 'Churn Probability']])

    # adding shap waterfall for prediction result
    st.subheader("SHAP Explainability")
    explainer = shap.Explainer(model.named_steps['model'], feature_names=df_clean.columns.tolist())
    shap_values = explainer(model.named_steps['scaler'].transform(df_clean))
    fig, ax = plt.subplots()
    shap.plots.waterfall(shap_values[0], show=False)
    st.pyplot(fig)
else:
    st.warning("Please upload a CSV file to continue")