from fastapi import FastAPI
from src.superhumans.routes import superhuman_router


version = 'v1'

app = FastAPI(
    title= "Superhumans API",
    description= "A Rest API to manage superhumans in Gotham City",
    version= version
)

app.include_router(superhuman_router, prefix=f'/api/{version}/superhumans')

