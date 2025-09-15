"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    # Intellectuel
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Math Olympiad": {
        "description": "Prepare for and participate in math competitions.",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Science Club": {
        "description": "Explore science experiments and projects.",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": []
    },
    # Sportif
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches.",
        "schedule": "Tuesdays & Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": []
    },
    "Basketball Club": {
        "description": "Practice basketball and play friendly games.",
        "schedule": "Fridays, 5:00 PM - 6:30 PM",
        "max_participants": 20,
        "participants": []
    },
    # Artistique
    "Art Workshop": {
        "description": "Explore painting, drawing, and sculpture techniques.",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": []
    },
    "Music Band": {
        "description": "Join the school band and perform at events.",
        "schedule": "Mondays & Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 25,
        "participants": []
    },
    "Drama Club": {
        "description": "Act, direct, and produce school plays.",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": []
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
