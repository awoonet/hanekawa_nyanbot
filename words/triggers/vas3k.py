from classes.media 	import Sticker, Text, Other

def vas3k(lang):
	start 		= {	'ru':"ⓅИнтересные статьи:\n",
								'en':"ⓅIntresting articles:\n"}
	articles 	= {
		'computational_photography'	:{'ru':'Вычислительная фотография',
																	'en':'Computational Photography'},
		'augmented_reality'					:{'ru':'Дополненная реальность AR',
																	'en':'Augmented Reality AR'},
		'machine_translation'				:{'ru':'Машинный перевод',
																	'en':'Machine Translation'},
	}
	return start[lang]+"\n".join(f'<a href="https://vas3k.ru/blog/{x}/">{y[lang]}</a>' for x, y in articles.items())

answers = {
	'nyan': {	'ru': (Text (vas3k('ru')),),
						'en': (Text (vas3k('en')),),
						'ua': (None,)},
	'lewd': {	'ru': (Text (vas3k('ru')),),
						'en': (Text (vas3k('en')),),
						'ua': (None,)},
	'angr': {	'ru': (Text (vas3k('ru')),),
						'en': (Text (vas3k('en')),),
						'ua': (None,)},
	'scar': {	'ru': (Text (vas3k('ru')),),
						'en': (Text (vas3k('en')),),
						'ua': (None,)},
}
