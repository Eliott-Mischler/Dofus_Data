from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Item(Base):
    __tablename__  = 'item_prices'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    price = Column(Integer)
    date_time_id = Column(Integer, ForeignKey('date_times.id'))
    date_time = relationship("Datetime")

    def __init__(self, name, price):
        self.name = name,
        self.price = price