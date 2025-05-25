from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student data
with open("students.json") as f:
    student_data = json.load(f)

@app.get("/api")
def get_marks(name: List[str] = []):
    name_to_marks = {student["name"]: student["marks"] for student in student_data}
    result = [name_to_marks.get(n, None) for n in name]
    return {"marks": result}
