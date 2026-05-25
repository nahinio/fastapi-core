from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from src.superhumans.superhuman_data import superhumans
from src.superhumans.scemas import Superhuman, SuperhumanUpdateModel 

superhuman_router = APIRouter()


@superhuman_router.get('/', response_model=list[Superhuman])
async def get_superhumans():
    return superhumans




@superhuman_router.post('/', status_code=status.HTTP_201_CREATED) 
async def add_superhuman(superhuman_data: Superhuman) -> dict:
    new_superhuman = superhuman_data.model_dump() 
    superhumans.append(new_superhuman)
    return new_superhuman

    

@superhuman_router.get('/{superhuman_id}')
async def get_superhuman(superhuman_id: int) -> dict:
    for superhuman in superhumans:
        if superhuman['id'] == superhuman_id:
            return superhuman 
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Superhuman not found")



@superhuman_router.patch('/{superhuman_id}')
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

        
        

@superhuman_router.delete('/{superhuman_id}')
async def delete_superhuman(superhuman_id: int) -> dict:
    for superhuman in superhumans:
        if superhuman['id'] == superhuman_id:
            superhumans.remove(superhuman)
            return {"message": "Superhuman deleted successfully"}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Superhuman not found")