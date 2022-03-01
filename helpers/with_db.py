from pony.orm import *
  
def per_message(app, msg):
  chat = app.chat.find_or_create(msg)
  user = app.user.find_or_create(msg, chat)
  chat.users.add(user)
  
  return user
    
def with_db(func):
  def wrapper(app, msg):
    with db_session:
      user = per_message(app, msg)
      
      func(app, msg, user)
      
  return wrapper
