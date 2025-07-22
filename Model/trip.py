from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timezone
from Database.database import Base
from zoneinfo import ZoneInfo


def get_current_time_str():
    return datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%I:%M %p")

def get_utc_date():
    return datetime.now(timezone.utc).date()

class Trip(Base):
    __tablename__ = "trip_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(String, nullable=False)
    paid_by = Column(String, nullable=False)
    date = Column(Date, default=get_utc_date)
    time = Column(String, default=get_current_time_str)

