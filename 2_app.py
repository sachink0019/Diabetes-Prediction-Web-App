from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models import model, MODEL_VERSION, scaler
from schema import UserInput
import pandas as pd

app = FastAPI()


#human readable 
@app.get('/')
def home():
      return{'message':'Diabetes prediction API'}

#machine readable
@app.get('/health')
def health_check():
      return{
            'status': 'ok',
            'model_version': MODEL_VERSION,
            'model_loaded': model is not None
      }



feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                  'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']


@app.post('/predict')
def predict(data: UserInput):

      features = pd.DataFrame([[
          data.pregnancies,
          data.glucose,
          data.blood_pressure,
          data.skin_thickness,
          data.insulin,
          data.bmi,
          data.diabetes_pedigree_function,
          data.age 

      ]], columns=feature_names)

      input_data_scaled = scaler.transform(features)

      prediction = model.predict(input_data_scaled)

      if prediction[0] == 0:
            result = " The person is Non-Diabetic"

      else:
            result = "The person is Diabetic"

      try:      

            return {
            "prediction":result
            }   

            return JSONResponse(status_code=200, content={"message": "Prediction completed succussfully"})         

      except Exception as e:

             return JSONResponse(status_code=500, content=str(e))

      
