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