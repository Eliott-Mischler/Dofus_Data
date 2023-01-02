from datetime import datetime
from item import Item
from date import Datetime
from base import Session, Base, engine

Base.metadata.create_all(engine)

def log_prices(name_list, price_list, type):
    session = Session()
    now = datetime.now()
    now = Datetime(now, type)
    for name, price in zip(name_list, price_list):
        item = Item(name, price)
        item.date_time = now
        session.add(item)
    session.commit()
    session.close()