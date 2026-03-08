from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # อนุญาตทุก origin (สำหรับ dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/welcome")
def welcome(name: str):
    return {"message": f"Welcome to Course Management {name}"}