from pydantic import BaseModel
from datetime import date


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

