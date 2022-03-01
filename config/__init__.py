from dotenv           import load_dotenv
from db               import db_init
from helpers          import load_reactions
from config.tg_init   import tg_init, Client

def app_init():
  load_dotenv()

  app = tg_init()
  app.db, app.chat, app.user = db_init()
  
  load_reactions()
    
  return app
