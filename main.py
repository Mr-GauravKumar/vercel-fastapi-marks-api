from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Correct way to load JSON once
file_path = os.path.join(os.path.dirname(__file__), "students.json")
with open(file_path, "r") as f:
    data = json.load(f)

@app.get("/")
def root():
    return {"message": "Welcome to Student Marks API"}

@app.get("/api")
def get_marks(name: List[str] = []):
    # ✅ Use lowercase mapping and lowercase lookup
    name_to_marks = {student["name"].lower(): student["marks"] for student in data}
    result = [name_to_marks.get(n.lower(), None) for n in name]
    return {"marks": result}
