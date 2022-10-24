from item_name import ItemName
from base import Session, Base, engine
import os

Base.metadata.create_all(engine)


name_string = open(os.path.join('clean_data','runes.txt'), encoding='utf-8').read() + '\n' + open(os.path.join('clean_data', 'resources.txt'), encoding='utf-8').read()
name_list = [name for name in name_string.splitlines() if name]
session = Session()

for name in name_list:
    item_name = ItemName(name)
    session.add(item_name)
session.commit()
session.close()