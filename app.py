import streamlit as st
import pandas as pd
import pickle

# Load model
with open("linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Calories Burned Prediction App")
st.write("Enter your workout details below to estimate calories burned.")

# Input fields
age = st.number_input("Age", 0, 100, 25)
gender = st.selectbox("Gender", ["Male", "Female"])
weight = st.number_input("Weight (kg)", 0.0, 200.0, 70.0)
height = st.number_input("Height (m)", 0.0, 2.5, 1.75)
max_hr = st.number_input("Max Heart Rate", 0, 250, 180)
avg_hr = st.number_input("Average Heart Rate", 0, 250, 120)
rest_hr = st.number_input("Resting Heart Rate", 0, 150, 70)
duration = st.number_input("Session Duration (hours)", 0.0, 10.0, 1.0)
workout_type = st.selectbox("Workout Type", ["Cardio", "Strength", "Flexibility"])
fat = st.number_input("Fat Percentage", 0.0, 60.0, 20.0)
water = st.number_input("Water Intake (liters)", 0.0, 10.0, 2.0)
freq = st.number_input("Workout Frequency (days/week)", 0, 7, 4)
experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
bmi = st.number_input("BMI", 0.0, 50.0, 22.0)

if st.button("Predict Calories Burned"):
    df = pd.DataFrame([{
        "Age": age,
        "Gender": 1 if gender == "Male" else 0,
        "Weight (kg)": weight,
        "Height (m)": height,
        "Max_Heart_Rate": max_hr,
        "Avg_Heart_Rate": avg_hr,
        "Resting_Heart_Rate": rest_hr,
        "Session_Duration (hours)": duration,
        "Workout_Type": workout_type,
        "Fat_Percentage": fat,
        "Water_Intake (liters)": water,
        "Workout_Frequency (days/week)": freq,
        "Experience_Level": experience,
        "BMI": bmi
    }])

    prediction = model.predict(df)
    st.success(f"🔥 Estimated Calories Burned: {prediction[0]:.2f}")
