from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/welcome/{organizer_name}")
def welcome_organizer(organizer_name:str):
    return f"Welcome to the event organized by {organizer_name}!"

@app.get("/event/{event_id}")
def get_event_by_id(event_id: int):
    return {"event_id": event_id, "event_name": "Sample Event", "date": "2024-12-31"}
