from time			    import sleep
from config 		    import hnkw_id

def check_admin(app, chat_id, user_id):
	user = app.get_chat_member(chat_id, user_id)
	if (user.status == 'administrator' or 
		user.status == 'creator'):
		return True
	else:
		return False

def msg_del(app, msg):
	"""
	Функция удаления командного сообщения, если бот имеет админ-статус.
	"""
	hnkw_u = app.get_me()
	hnkw = app.get_chat_member(str(msg.chat.id), hnkw_u.id)
	
	if (hnkw.status == 'administrator' or 
		hnkw.status == 'creator' and 
		hnkw.can_delete_messages):
		app.delete_messages(str(msg.chat.id), msg.message_id)

def admin_send(app, msg, txt):
	new_msg = msg.reply(txt)
	msg_del(app, msg)
	sleep(7)
	msg_del(app, new_msg)

def roleplay_send(app, msg, txt):
	if msg.reply_to_message: msg.reply(txt, reply_to_message_id=msg.reply_to_message.message_id)
	else:					 msg.reply(txt, quote=False)
	msg_del(app, msg)