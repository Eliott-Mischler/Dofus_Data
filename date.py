from sqlalchemy import Column, String, Integer, DateTime
from base import Base

class Datetime(Base):
    __tablename__ = 'date_times'

    id = Column(Integer, primary_key = True)
    date_time = Column(DateTime)

    def __init__(self, date_time):
        self.date_time = date_time,