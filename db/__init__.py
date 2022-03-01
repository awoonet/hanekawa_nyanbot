from os import getenv as env

from pony.orm import *

from db.model_chat import generate_chat
from db.model_user import generate_user

def db_init():
  postgresql_credentials = dict(
    provider='postgres',
    user    =env('PSQL_USER'),
    password=env('PSQL_PASS'),
    host    =env('PSQL_HOST'),
    database=env('DB_NAME'),
  )
    
  db = Database()
  
  Chat = generate_chat(db)
  User = generate_user(db, Chat)
  
  db.bind(**postgresql_credentials)
  db.generate_mapping(create_tables=True)
  
  
  print('DB initialized.')
  return db, Chat, User
