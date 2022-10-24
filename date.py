from sqlalchemy import Column, String, Integer, DateTime
from base import Base

class Datetime(Base):
    __tablename__ = 'date_times'

    id = Column(Integer, primary_key = True)
    type = Column(String)
    date_time = Column(DateTime)

    def __init__(self, date_time, type):
        self.date_time = date_time,
        self.type = type