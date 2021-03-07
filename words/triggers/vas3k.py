from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

def ru():
	start 		= "Интересные статьи:\n"
	articles 	= {
		'computational_graphy':'Вычислительная фотография',
		'augmented_reality'		:'Дополненная реальность AR',
		'machine_translation'	:'Машинный перевод',
	}
	return start, articles

def en():
	start 		= "Intresting articles:\n"
	articles = {
		'computational_graphy':'Computational Photography',
		'augmented_reality'		:'Augmented Reality AR',
		'machine_translation'	:'Machine Translation',
	}

def vas3k(lang):
	start, articles = lang()
	return start+"\n".join(f'<a href="https://vas3k.ru/blog/{x}/">{y}</a>' for x, y in articles.items())

answers = {
	'nyan': {
		'ru': (Text (lambda: vas3k(ru)),),
		'en': (Text (lambda: vas3k(en)),),
		'ua': (None,),
	},
	'lewd': {
		'ru': (Text (lambda: vas3k(ru)),),
		'en': (Text (lambda: vas3k(en)),),
		'ua': (None,),
	},
	'angr': {
		'ru': (Text (lambda: vas3k(ru)),),
		'en': (Text (lambda: vas3k(en)),),
		'ua': (None,),
	},
	'scar': {
		'ru': (Text (lambda: vas3k(ru)),),
		'en': (Text (lambda: vas3k(en)),),
		'ua': (None,),
	},
}
