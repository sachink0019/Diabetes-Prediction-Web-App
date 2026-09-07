import streamlit as st
import requests

API_URL = "http://13.53.174.221:8000/predict"

st.title("Diabetes Prediction App")

st.markdown("Enter the foloowing details mentioned below here")

# Input fieds

gender = st.selectbox(
    "Select Gender",
    ["male", "female", "others"]
)


if gender == "female":
    pregnancies = st.number_input(
        "Enter the number of pregnancies",
        min_value=0,
        max_value=20,
        step=1
    )
else:
    pregnancies = 0


glucose = st.number_input("Enter the glucose level", min_value=0, max_value=300)
blood_pressure	 = st.number_input("Enter the blood pressure level", min_value=0, max_value=200)
skin_thickness = st.number_input("Enter the skin thickness level", min_value=0, max_value=100)
insulin = st.number_input("Enter the insulin level", min_value=0, max_value=1000)
bmi = st.number_input("Enter the BMI level", min_value=0, max_value=100)
diabetes_pedigree_function = st.number_input("Enter the diabetes pedigree function level", min_value=0.0, max_value=2.5, step=0.01)
age = st.number_input("Enter the age of the patient", min_value=1, max_value=120)





if st.button("Predict Diabetes"):
    
    input_data = {
        "pregnancies": pregnancies,
        "glucose": glucose,
        "blood_pressure": blood_pressure,
        "skin_thickness": skin_thickness,
        "insulin": insulin,
        "bmi": bmi,
        "diabetes_pedigree_function": diabetes_pedigree_function,
        "gender": gender,
        "age": age
    }

    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()


        if response.status_code == 200 and "prediction" in result:
             prediction = result["prediction"]
             st.success(f"Prediction: {prediction}")
             

        else:
            st.error(f"API Error : {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
         st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")
        
                     


