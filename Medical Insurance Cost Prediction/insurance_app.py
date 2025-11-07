import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open(r"C:\Users\hp\Downloads\insurance_model.pkl", "rb"))

# Page title
st.set_page_config(page_title="Medical Insurance Cost Prediction", layout="centered")
st.title("Medical Insurance Cost Prediction")
st.write("Enter your details below to predict the estimated medical insurance cost.")

# Input fields
age = st.slider("Age", 18, 100, 25)
sex = st.selectbox("Sex", ("male", "female"))
bmi = st.number_input("BMI (Body Mass Index)", 10.0, 60.0, 25.0)
children = st.selectbox("Number of Children", (0, 1, 2, 3, 4, 5))
smoker = st.selectbox("Smoker", ("yes", "no"))
region = st.selectbox("Region", ("northeast", "northwest", "southeast", "southwest"))

# Encoding categorical data
sex = 1 if sex == "male" else 0
smoker = 1 if smoker == "yes" else 0
region_map = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
region = region_map[region]

# Prediction
if st.button("Predict"):
    features = np.array([[age, sex, bmi, children, smoker, region]])
    prediction = model.predict(features)
    st.success(f"Estimated Insurance Cost: **Rs{prediction[0]:,.2f}**")

# Footer
st.markdown("---")
st.caption("Developed by Vishal — Machine Learning Project")
