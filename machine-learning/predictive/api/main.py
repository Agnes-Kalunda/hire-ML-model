import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle


app = FastAPI

origins = [

"http://localhost",

"http://localhost:8080",

"http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,

    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#loading model

model = pickle.load(open("../model/hireable.pkl", "rb"))

#defining class
class Candidate(BaseModel):
    gender : int
    bsc: float
    workex: int
    etest_p: float
    msc: float

#home rote

@app.get("/")

def read_root():
    return {"data": "Hi! Lets predict your hirablity!"}

#prediction route

@app.post("/prediction/")

async def get_prediction(data: Candidate):
    sample = [[
        data.gender,
        data.bsc,
        data.workex,
        data.etest_p,
        data.msc
    ]]

    hired = model.predict(sample).tolist()[0]

    return{
       "data":{
            'prediction': hired,
            'interpretation': ' Candidate can be hired.' if hired == 1 else "Candidate cannot be hired.Sorry."



    }
}

if __name__ == '__main__':
    uvicorn.run(app, port = 3000, host = "0.0.0.0")


