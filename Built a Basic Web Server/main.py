from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

# Create FastAPI application instance
app = FastAPI()


# Root endpoint
# Used to verify that the Bat Server is running properly
@app.get("/")
async def read_root():
    return {
        "message": "Bat Server is active. Gotham is under protection."
    }


# Path parameter example
# Captures a dynamic value directly from the URL
# Example: /signal/spiderman
@app.get("/signal/{hero_name}")
async def call_hero(hero_name: str) -> dict:

    return {
        "message": f"Signal received. Welcome to Gotham, {hero_name}."
    }


# Query parameter example
# Query parameters are passed after '?'
# Example: /mission?villain=Joker
@app.get("/mission")
async def assign_mission(villain: str = "Unknown Villain") -> dict:

    return {
        "mission": f"Batman is tracking {villain} tonight."
    }


# Combining path and query parameters
# Example:
# /mission/Batman?city=Gotham
@app.get("/mission/{hero_name}")
async def mission_location(hero_name: str, city: str) -> dict:

    return {
        "message": f"{hero_name} has been deployed to protect {city}."
    }


# Optional query parameter example
# Default values are used if no parameter is provided
# Example:
# /batcomputer?hero=Nightwing
@app.get("/batcomputer/")
async def batcomputer_access(
    hero: Optional[str] = "Batman",
    access_level: Optional[str] = "Standard"
) -> dict:

    return {
        "access": f"{hero} granted {access_level} Batcomputer access."
    }


# Request body schema
# Defines the expected JSON structure for gadget creation
class GadgetCreateModel(BaseModel):
    gadget_name: str
    purpose: str


# POST endpoint
# Creates a new Batman gadget using JSON request body
@app.post("/gadgets/", status_code=201)
async def create_gadget(gadget: GadgetCreateModel):

    return {
        "message": "New gadget added to the Batcave.",
        "gadget_name": gadget.gadget_name,
        "purpose": gadget.purpose
    }


# Header parameter example
# Headers contain metadata about the incoming request
@app.get("/get-headers/")
async def get_headers(

    accept: Optional[str] = Header(None),
    content_type: Optional[str] = Header(None),
    user_agent: Optional[str] = Header(None),
    host: Optional[str] = Header(None)

) -> dict:

    return {
        "Accept": accept,
        "Content-Type": content_type,
        "User-Agent": user_agent,
        "Host": host
    }