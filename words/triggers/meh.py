from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: 'Вздыхает'), 
						Text	(lambda: 'Пушисто!'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (		
						Text	(lambda: '*Прижимается и гладит*'),
						Text	(lambda: f'Не печалься{nyah()} *целует в лоб и обнимает*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (		
						Text	(lambda: 'Это мне надо вздыхать, потому что ты тут.'),
					),	
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (		
						Text	(lambda: 'Вздыхает'),
					),
		'en': (None,),
		'ua': (None,),
	},
}