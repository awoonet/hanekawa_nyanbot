from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: 'Вививи'), 
						Text	(lambda: f'*{name("з")}аводит старый жигуль*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (	
						Text	(lambda: f'*{name("з")}аводится*'), 
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (		
						Text	(lambda: 'Тыгыдык по лицу'),
					),	
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (None,),
		'en': (None,),
		'ua': (None,),
	},
}