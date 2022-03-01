from os       import getenv as env
from pyrogram import Client, filters
from helpers  import with_db, load_reactions

class Client(Client):
  filters = filters
  with_db = with_db
  reactions = load_reactions()
  
  media_reactions_storage	= -1001157282357

def tg_init():
  telegram_credentials = dict(
    session_name=env('SESSION_NAME'),
    api_id      =env('API_ID'),
    api_hash    =env('API_HASH'),
    bot_token   =env('BOT_TOKEN'),
    plugins     ={'root':'plugins'},
  )
  
  app = Client(**telegram_credentials)
  
  print('TG initialized.')
  return app
