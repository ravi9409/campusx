from dataclasses import field
    
from pydantic import AnyUrl, BaseModel, Field, field_validator
from typing import Annotated, Optional
from pydantic import EmailStr

class Patient(BaseModel):
    id: int
    name: Annotated[str, Field(max_length=50,title="Name of the patient",description="Full name of the patient")]
    email: EmailStr
    linked_url:AnyUrl
    #use AnyUrl for fields that should contain a URL
    #use EmailStr for fields that should contain an email address
    age: int=Field(gt=30)
    disease: Optional[str]
    #use Optional for fields that may not have a value
    #if a field is Optional, it can be set to None

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domain=['hdfc.com','icici.com']
        domain=value.split('@')[-1]
        if domain not in valid_domain:
            raise ValueError(f"Email domain must be one of {valid_domain}")
        return value

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linked_url)
    print(patient.age)
    print(patient.disease)
    print('inserted')
    
patient_info={"name": "nitish", "email": "nitish@example.com", "linked_url": "http://example.com", "age": 31, "disease": "flu"}
patient1 = Patient(id=1, **patient_info)
insert_patient_data(patient1)