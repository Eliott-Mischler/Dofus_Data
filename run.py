from datetime import datetime
from item import Item
from date import Datetime
from base import Session, Base, engine

Base.metadata.create_all(engine)


def log_prices(price_list, type):
    id_offset = 1
    if type != 'rune':
        id_offset = 99
    session = Session()
    now = datetime.now()
    now = Datetime(now, type)
    for i,price in enumerate(price_list):
        item = Item(i+id_offset, price)
        item.date_time = now
        session.add(item)
    session.commit()
    session.close()