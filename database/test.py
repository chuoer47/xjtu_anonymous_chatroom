from connectdb import *
from database.SQL import update_comer_record

data = (str(111), "('127.0.0.1', 49216)")
cur.execute(update_comer_record, data)
conn.commit()

