from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from Database.database import Base, engine
from Schema.trip import TripInp, TripOut
from Model.trip import Trip
from Database.database import get_db
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://dehraduntrip.netlify.app","http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.post("/createTrip",response_model=TripOut)
async def createTrip(tripData: TripInp, db: Session = Depends(get_db)):
     new_trip = Trip(
        name=tripData.name,
        price=tripData.price,
        paid_by=tripData.paid_by
    )
     db.add(new_trip)
     db.commit()
     db.refresh(new_trip)
     return new_trip

@app.get("/getTrip",response_model=List[TripOut])
async def getTrip(db: Session = Depends(get_db)):
     return db.query(Trip).all()

@app.get("/deleteTrip/{id}")
async def getTrip(id : int ,db: Session = Depends(get_db)):
     trip = db.query(Trip).filter(Trip.id == id).first()
     if not trip:
         raise HTTPException(status_code=404, detail="Product not found")
     db.delete(trip)
     db.commit()
     return {"message": "Product deleted successfully"}
