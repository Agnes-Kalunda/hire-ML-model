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