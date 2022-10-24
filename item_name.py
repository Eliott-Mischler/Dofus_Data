from sqlalchemy import Column, String, Integer
from base import Base

class ItemName(Base):
    __tablename__  = 'item_names'

    id = Column(Integer, primary_key = True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
