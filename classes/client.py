import shelve

from classes.katsugram	import app
from classes.сhat 		import Chat

class app(app):
	bot = type('Foo', (), {'username':'hanekawa_nyanbot'})

	def run(self):
		db = lambda x: shelve.open(x)

		super().run(db)

	@staticmethod
	def database(func):
		def wrapper(app, msg):
			try:
				chat_id = msg.chat.id

				if chat_id not in app.db:
					app.db[chat_id] = Chat(msg, app.db)
				
				chat = app.db[chat_id]
				
				func(app, msg, chat)

				app.db[chat_id] = chat
				app.db.sync()

			except Exception as error:
				app.send_error(msg, error)
				
			raise app.ContinuePropagation()

		return wrapper
