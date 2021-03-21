from random import choice, randint
import re

names = {
		'ru':['Ханекава {}', 'Ханекава-чан {}', 'Ханекава Тсубаса {}', 'Цубаса-кун {}', 'Някава {}', 'Някава-нян {}'],
		'en':['Hanekawa {}', 'Hanekawa-chan {}','Hanekawa Tsubasa {}', 'Tsubasa-kun {}','Nyakawa {}', 'Nyakawa-nyan {}'],
		'ua':['Ханекава {}', 'Ханекава-чан {}', 'Ханекава Тсубаса {}', 'Цубаса-кун {}', 'Някава {}', 'Някава-нян {}'],
}

faces	= {
	'nyan'	: ('=^_^=','^_^', '*-*', '^-^', '~', '^^', '))'),
	'lewd'	: ('*-*', '^-^', '♡♡', '♡'),
	'angr'	: (),
	'scar'	: ('>_<'),
}

appelation_to_user	=	{
	'nyan'	: ('', ', няха', ', няшка', ', милашка',),
	'lewd'	: ('', ', котенок', ', котеночек', ', лапочка', ', лапа', ', крольчёнок', ', зайчик'),
	'angr'	: ('', ', придурок', ', дурак', ', бака', ', идиот'),
	'scar'	: ('',''),
}

class Media:
	def __init__(self, text=False, media=False, none=False):
		self.text	= text
		self.media= media
		self.none	= none

	def reply(self, app, msg, chat):
		if not self.none:
			self.app = app
			self.msg = msg
			self.chat = chat

			if randint(1,10) > 8:
				self.send_other()
			else:
				self.send_text()

	def send_text(self):
		if self.text:
			text = self.guess_smth_or_tuple(self.text)
			text = self.format_text(text)
			self.msg.reply_text(text = text, quote	= True)
		else:
			self.send_other()

	def send_other(self):
		if self.media:
			answer = self.guess_smth_or_tuple(self.media)
			if type(answer) is str:
				self.send_sticker(answer)
			elif type(answer) is int:
				self.send_media(answer)
		else:
			self.send_text()

	def send_sticker(self, sticker_id):
		self.msg.reply_sticker(sticker = sticker_id, quote = True)

	def send_media(self, media_id):
		self.app.copy_message(	
			chat_id							= self.msg.chat.id, 
			from_chat_id				= self.app.media_id,
			message_id 					= media_id,
			reply_to_message_id	= self.msg.message_id,
			caption 						= '')

	@staticmethod
	def guess_smth_or_tuple(smth):
		if type(smth) is tuple:	return choice(smth)  
		else: 									return smth

	def format_text(self, text):
		mood = self.chat.conf['mood']
		lang = self.chat.conf['lang']

		if re.search(r'[ⓊⒻⒶⓃⓋⓇⒸ]', text):
			text = text.replace('Ⓤ', f'**{self.app.username_finder(self.msg.from_user)}**')
			text = text.replace('Ⓕ', choice(faces[mood]))
			text = text.replace('Ⓐ', choice(appelation_to_user[mood]))

			funcs = {
				'Ⓝ' : lambda txt: choice((*names[lang], txt.upper())).format(txt),
				'Ⓥ' : lambda txt: choice(('', txt)),
				'Ⓡ' : lambda txt: txt * randint(1, 6),
				'Ⓒ' : lambda txt: choice(txt.split(', ')),
			}

			i = 4
			while i > 0:
				for tag, func in funcs.items():
					if tag in text:
						
							txt = text.split(tag, maxsplit=2)
							answer = func(txt[1])
							text = f'{txt[0]}{answer}{txt[2]}'

							i+=1
					else:
						i-=1
						
		return text