from random import choice, randint

class MessageSender:
  def reply(self, response: dict):
    lang = self.chat.get_lang()
    self.text	= response[lang]
    self.media	= response['media']
    
    text_exist = self.text is not None
    media_exist= self.media is not None
    media_chance = randint(1,10) > 8
  
    if media_exist and (media_chance or not text_exist):
      self.send_other()
    elif text_exist:
      self.send_text()
    
  def send_text(self):
    text = choice(self.text)
    text = self.format_text(text)
    self.msg.reply_text(text=text, quote=True)

  def send_other(self):
    answer = choice(self.media)
    if type(answer) is str:
      self.send_sticker(answer)
    elif type(answer) is int:
      self.send_media(answer)

  def send_sticker(self, sticker_id):
    self.msg.reply_sticker(sticker = sticker_id, quote = True)

  def send_media(self, media_id):
    self.app.copy_message(	
      chat_id							= self.msg.chat.id, 
      from_chat_id				= self.app.media_reactions_storage,
      message_id 					= media_id,
      reply_to_message_id	= self.msg.message_id,
      caption 						= '')

