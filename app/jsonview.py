from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as f: 
        data=json.load(f)
    return data

@app.get("/")
def root():
    return {"message": "Patient management system API"}

@app.get("/hello")
def hello():
    return {"message": "Hello only"}

@app.get("/view")
def view():
    return load_data()

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description='ID of the patient in DB',example='P001'
)):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    return HTTPException(status_code=404,detail='Patient not found')

@app.get("/sort")
def sort_patient(sort_by: str=Query(...,description='Sort on the basis of height,weight or bmi'),order=Query('Sort in asc or desc order')
):
    valid_fields=['heights','weights','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail='Invalid order')
    
    data=load_data()
    
    sort_order=True if order=='desc' else False 
    
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=True)
    
    return sorted_data