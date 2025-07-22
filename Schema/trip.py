from pydantic import BaseModel
from datetime import date

class TripInp(BaseModel):
    name : str
    price : str
    paid_by : str

class TripOut(BaseModel):
    id: int
    name: str
    price : str
    paid_by : str
    date: date
    time: str
    
    class Config:
        orm_mode = True  