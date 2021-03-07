from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: "Aw"+randint('o')+randvoid(" =^o^= ~")), 
						Text	(lambda: "Ав"+randint('у')+randvoid(" =^o^= ~")), 
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (	
						Text	(lambda: "Aw"+randint('o')+randvoid(" =^o^= ~")), 
						Text	(lambda: "Ав"+randint('у')+randvoid(" =^o^= ~")), 
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (		
						Text	(lambda: 'Awoo *хищно улыбается*'), 
						Text	(lambda: 'Авууу!'),
					),	
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (		
						Text	(lambda: "Aв-ву... >_<"), 
						Text	(lambda: 'Aw-wo'),
						Sticker	('CAADAQADPQcAApEpAAEQfBRxUdnXev0WBA',),
					),
		'en': (None,),
		'ua': (None,),
	},
}