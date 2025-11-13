import streamlit as st
import pandas as pd
import pickle

# Load model
with open("linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Calories Burned Prediction App")

st.write("Enter workout details below:")

# Create inputs
age = st.number_input("Age", 0, 100)
gender = st.selectbox("Gender", ["Male", "Female"])
weight = st.number_input("Weight (kg)")
height = st.number_input("Height (m)")
max_hr = st.number_input("Max Heart Rate")
avg_hr = st.number_input("Average Heart Rate")
rest_hr = st.number_input("Resting Heart Rate")
duration = st.number_input("Session Duration (hours)")
workout_type = st.selectbox("Workout Type", ["Cardio", "Strength", "Flexibility"])
fat = st.number_input("Fat Percentage")
water = st.number_input("Water Intake (liters)")
freq = st.number_input("Workout Frequency (days/week)")
experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
bmi = st.number_input("BMI")

# Predict
if st.button("Predict Calories Burned"):
    df = pd.DataFrame([{
        "Age": age, "Gender": 1 if gender == "Male" else 0,
        "Weight (kg)": weight, "Height (m)": height, "Max_Heart_Rate": max_hr,
        "Avg_Heart_Rate": avg_hr, "Resting_Heart_Rate": rest_hr,
        "Session_Duration (hours)": duration, "Workout_Type": workout_type,
        "Fat_Percentage": fat, "Water_Intake (liters)": water,
        "Workout_Frequency (days/week)": freq, "Experience_Level": experience, "BMI": bmi
    }])
    result = model.predict(df)
    st.success(f"Predicted Calories Burned: {result[0]:.2f}")
