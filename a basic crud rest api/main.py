from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from datetime import date
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

superhumans = [
    {
        "id": 1,
        "name": "Batman",
        "alias": "Bruce Wayne",
        "type": "hero",
        "city": "Gotham",
        "power_level": 95,
        "first_appearance": date(1939, 5, 1),
        "status": "active",
    },
    {
        "id": 2,
        "name": "Joker",
        "alias": "Unknown",
        "type": "villain",
        "city": "Gotham",
        "power_level": 90,
        "first_appearance": date(1940, 4, 25),
        "status": "active",
    },
    {
        "id": 3,
        "name": "Catwoman",
        "alias": "Selina Kyle",
        "type": "anti-hero",
        "city": "Gotham",
        "power_level": 75,
        "first_appearance": date(1940, 4, 25),
        "status": "active",
    },
    {
        "id": 4,
        "name": "Robin",
        "alias": "Dick Grayson",
        "type": "hero",
        "city": "Gotham",
        "power_level": 70,
        "first_appearance": date(1940, 1, 1),
        "status": "active",
    },
    {
        "id": 5,
        "name": "Penguin",
        "alias": "Oswald Cobblepot",
        "type": "villain",
        "city": "Gotham",
        "power_level": 80,
        "first_appearance": date(1941, 12, 1),
        "status": "active",
    },
    {
        "id": 6,
        "name": "Riddler",
        "alias": "Edward Nygma",
        "type": "villain",
        "city": "Gotham",
        "power_level": 82,
        "first_appearance": date(1948, 10, 1),
        "status": "active",
    },
    {
        "id": 7,
        "name": "Bane",
        "alias": "Unknown",
        "type": "villain",
        "city": "Gotham",
        "power_level": 98,
        "first_appearance": date(1993, 1, 1),
        "status": "active",
    },
    {
        "id": 8,
        "name": "Nightwing",
        "alias": "Dick Grayson",
        "type": "hero",
        "city": "Blüdhaven",
        "power_level": 85,
        "first_appearance": date(1984, 6, 1),
        "status": "active",
    },
    {
        "id": 9,
        "name": "Two-Face",
        "alias": "Harvey Dent",
        "type": "villain",
        "city": "Gotham",
        "power_level": 78,
        "first_appearance": date(1942, 8, 1),
        "status": "active",
    },
]


class Superhuman(BaseModel):
    id: int
    name: str
    alias: str
    type: str
    city: str
    power_level: int
    first_appearance: date
    status: str

class SuperhumanUpdateModel(BaseModel):
    name: str
    alias: str
    type: str
    city: str
    power_level: int
    status: str



# get all the superhumans
@app.get('/superhumans', response_model=list[Superhuman])
async def get_superhumans():
    return superhumans



# add a new superhuman
@app.post('/superhumans', status_code=status.HTTP_201_CREATED) 
async def add_superhuman(superhuman_data: Superhuman) -> dict:
    new_superhuman = superhuman_data.model_dump()  # model dump() converts the Pydantic model to a dictionary
    superhumans.append(new_superhuman)
    return new_superhuman

    

# get a specific superhuman by ID
@app.get('/superhumans/{superhuman_id}')
async def get_superhuman(superhuman_id: int) -> dict:
    for superhuman in superhumans:
        if superhuman['id'] == superhuman_id:
            return superhuman 
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Superhuman not found")



# update a specific superhuman by ID
@app.patch('/superhumans/{superhuman_id}')
async def update_superhuman(superhuman_id: int, superhuman_update_data: SuperhumanUpdateModel) -> dict:
    for superhuman in superhumans:
        if superhuman['id'] == superhuman_id:
            superhuman['name'] = superhuman_update_data.name
            superhuman['alias'] = superhuman_update_data.alias
            superhuman['type'] = superhuman_update_data.type
            superhuman['city'] = superhuman_update_data.city
            superhuman['power_level'] = superhuman_update_data.power_level
            superhuman['status'] = superhuman_update_data.status

            return superhuman
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Superhuman not found")

        
        
# delete a specific superhuman by ID
@app.delete('/superhumans/{superhuman_id}')
async def delete_superhuman(superhuman_id: int) -> dict:
    for superhuman in superhumans:
        if superhuman['id'] == superhuman_id:
            superhumans.remove(superhuman)
            return {"message": "Superhuman deleted successfully"}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Superhuman not found")