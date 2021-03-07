from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: 'Р'+randvoid('ав')+randint('р')+'!'),
						Text	(lambda: 'R'+randvoid('aw')+randint('r')+'!'),
						Sticker	('CAADAgAD1j0AAuCjggeCzkUtb_PLChYE'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (		
						Text	(lambda: 'Ну чего ты'+nyah()+face()),
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (		
						Text	(lambda: 'Р'+randvoid('ав')+r('р')+'!'),
						Text	(lambda: 'R'+randvoid('aw')+r('r')+'!'),
						Text	(lambda: f'*{name("г")}розно рычит*'),
					),	
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (		
						Text	(lambda: '*'+name('т')+'ихо рычит за углом*'),
					),
		'en': (None,),
		'ua': (None,),
	},
}