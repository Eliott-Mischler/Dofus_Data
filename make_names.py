import psycopg2
from dotenv import load_dotenv

from psycopg2.extras import execute_values
import os

load_dotenv()
conn = psycopg2.connect("postgresql://postgres:k3SoBK6L35OQq5FzGzRY@containers-us-west-46.railway.app:6593/railway")

name_string = open(os.path.join('clean_data','runes.txt'), encoding='utf-8').read() + '\n' + open(os.path.join('clean_data', 'resources.txt'), encoding='utf-8').read()
name_list = [name for name in name_string.splitlines() if name]
cursor = conn.cursor()

double_list = [(i+1, name) for i, name in enumerate(name_list)]

query = "INSERT INTO item_names (id, name) values %s ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name"

execute_values(cursor, query, double_list, template=None, page_size = 100)
conn.commit()
