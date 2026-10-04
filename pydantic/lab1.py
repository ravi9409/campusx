from pydantic import BaseModel
from typing import Optional

class Patient(BaseModel):
    id: int
    name: str
    age: int
    disease: Optional[str]
    #use Optional for fields that may not have a value
    #if a field is Optional, it can be set to None
    
def insert_patient_data(patient: Patient):
    print(patient.id)
    print(patient.name)
    print(patient.age)
    print(patient.disease)
    print('inserted')
    
patient_info={"name": "nitish", "age": 30, "disease": "flu"}
patient1 = Patient(id=1, **patient_info)
insert_patient_data(patient1)