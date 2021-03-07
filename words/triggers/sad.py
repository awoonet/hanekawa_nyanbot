from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: 'Не печалься'+nyah()+face()),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (		
						Text	(lambda: '*'+name('п')+'рижимается и гладит*'),
						Text	(lambda: 'Не печалься,*'+name('ц')+'елует в лоб и обнимает*'),
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