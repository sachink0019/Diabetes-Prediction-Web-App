from pydantic import BaseModel, Field, computed_field, model_validator
from typing import Literal, Annotated, Optional
import numpy as np
from enum import Enum



class Gender(str, Enum):
      male = "male"
      female = "female"
      others = "others"

# pydantic model to validate incoming data
class UserInput(BaseModel):
      
      gender: Gender = Field(..., description='Gender of the patient')
      pregnancies: Annotated[int , Field(..., ge=0, description="This Section only for female patient")]
      glucose: Annotated[int, Field(..., gt=0, description='Enter Glucose level of the patient')]
      blood_pressure: Annotated[int, Field(..., gt=0, description='Blood Pressure of the patient')]
      skin_thickness: Annotated[int, Field(...,gt=0, description='Skin Thickness of the patient')]
      insulin: Annotated[int, Field(..., description='insulin level of the patient')]
      bmi: Annotated[float, Field(..., gt=0, description='Enter BMI value of patient')]
      diabetes_pedigree_function: Annotated[float, Field(..., gt=0, description='Enter Diabetes Pedigree Function value of the patient')]
      age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]


      @model_validator(mode='after')
      def validate_pregnancies(self):

            if self.gender != Gender.female and self.pregnancies != 0:
                  raise ValueError("Pregnancies must be 0 for non-female patients")
            return self