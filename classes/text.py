from random import choice, randint
import re

names = {
		'ru':['Ханекава {}', 'Ханекава-чан {}', 'Ханекава Тсубаса {}', 'Цубаса-кун {}', 'Някава {}', 'Някава-нян {}'],
		'en':['Hanekawa {}', 'Hanekawa-chan {}','Hanekawa Tsubasa {}', 'Tsubasa-kun {}','Nyakawa {}', 'Nyakawa-nyan {}'],
		'ua':['Ханекава {}', 'Ханекава-чан {}', 'Ханекава Тсубаса {}', 'Цубаса-кун {}', 'Някава {}', 'Някава-нян {}'],
}

faces	= {
	'nyan'	: ('=^_^=','^_^', '*-*', '^-^', '~', '^^', '))', '😊', '☺️', '🙂', '😉'),
	'lewd'	: ('*-*', '^-^', '😍', '🥰', '😘', '😚', '☺️'),
	'angr'	: (', 😡', ', 😤', ),
	'scar'	: ('😖', '😣', '😔', '>_<'),
}

appelation_to_user	=	{
	'nyan'	: ('', ', няха', ', няшка', ', милашка',),
	'lewd'	: ('', ', котенок', ', котеночек', ', лапочка', ', лапа', ', крольчёнок', ', зайчик'),
	'angr'	: ('', ', придурок', ', дурак', ', бака', ', идиот'),
	'scar'	: ('',''),
}

def tsu(lang, mood, text):
	if 'Ⓟ' in text:
		text = text.replace('Ⓟ', '')
		return text

	text = text.replace('Ⓕ', choice(faces[mood]))
	text = text.replace('Ⓐ', choice(appelation_to_user[mood]))

	funcs = {
		'Ⓝ' : lambda l, txt: choice((*names[l], txt.upper())).format(txt),
		'Ⓥ' : lambda _, txt: choice(('', txt)),
		'Ⓡ' : lambda _, txt: txt * randint(1, 6),
		'Ⓒ' : lambda _, txt: choice(txt.split(', ')),
	}

	q = 4
	while q>0:
		for tag, func in funcs.items():
			if tag in text:
					txt = text.split(tag, maxsplit=2)
					answer = func(lang, txt[1])
					text = f'{txt[0]}{answer}{txt[2]}'
			else:
				q = q-1

	return text

