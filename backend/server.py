from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import uuid

app = FastAPI()

class Job(BaseModel):
    id: str = str(uuid.uuid4())
    title: str
    company: str
    location: str
    salary: str

jobs = []

@app.get("/")
def root():
    return {"message": "API Running"}

@app.get("/jobs", response_model=List[Job])
def get_jobs():
    return jobs

@app.post("/jobs")
def add_job(job: Job):
    jobs.append(job)
    return job
