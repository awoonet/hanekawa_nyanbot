from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: 'Тыгыдык!'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (	
						Text	(lambda: 'Сейчас сделаем тыгыдык в твоих штанах^^'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (None,),
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (None,),
		'en': (None,),
		'ua': (None,),
	},
}