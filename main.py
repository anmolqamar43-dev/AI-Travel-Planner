from typing import Literal

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from gemini_service import generate_travel_plan


# -----------------------------------------
# FastAPI application
# -----------------------------------------

app = FastAPI(
    title="AI Travel Planner",
    description="Travel Planner using Gemini Prompting Techniques",
    version="1.0.0"
)


# -----------------------------------------
# Static files
# -----------------------------------------

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# -----------------------------------------
# Templates
# -----------------------------------------

templates = Jinja2Templates(
    directory="templates"
)


# -----------------------------------------
# Request model
# -----------------------------------------

class TravelRequest(BaseModel):
    name: str = Field(..., min_length=1)
    destination: str = Field(..., min_length=1)
    days: int = Field(..., ge=1, le=30)
    budget: float = Field(..., gt=0)
    interests: list[str] = Field(..., min_length=1)
    travel_style: str = Field(..., min_length=1)

    technique: Literal[
        "zero-shot",
        "few-shot",
        "structured"
    ]


# -----------------------------------------
# Home page
# -----------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# -----------------------------------------
# Generate itinerary
# -----------------------------------------

@app.post("/generate")
async def generate_itinerary(data: TravelRequest):

    try:

        traveler_data = {
            "name": data.name,
            "destination": data.destination,
            "days": data.days,
            "budget": data.budget,
            "interests": ", ".join(data.interests),
            "travel_style": data.travel_style
        }

        result = generate_travel_plan(
            traveler_data,
            data.technique
        )

        return {
            "success": True,
            "technique": data.technique,
            "itinerary": result
        }

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": str(e)
            }
        )


# -----------------------------------------
# Health check
# -----------------------------------------

@app.get("/health")
async def health_check():

    return {
        "status": "healthy",
        "application": "AI Travel Planner"
    }