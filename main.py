from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# DIRECT DATA (instead of loading from JSON file)
data = [
    { "name": "8LdMj", "marks": 74 },
    { "name": "WmfXWG", "marks": 81 },
    { "name": "005OKVxKa", "marks": 48 }
]

@app.get("/")
def root():
    return {"message": "Welcome to Student Marks API"}

@app.get("/api")
def get_marks(name: List[str] = []):
    name_to_marks = {student["name"].lower(): student["marks"] for student in data}
    result = [name_to_marks.get(n.lower(), None) for n in name]
    return {"marks": result}
