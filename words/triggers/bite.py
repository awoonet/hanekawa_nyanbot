from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: 'Кусь'+nyah()+face()),
						Text	(lambda: 'Кусь, б-бака >_<'),
						Sticker	('CAADAgADxQADrHkzBnUN64jQMLBoFgQ',),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (		
						Text	(lambda: 'Кусь'+nyah()+face()),
						Text	(lambda: '*Нежно кусь за ушко*'), 
						Text	(lambda: '*'+name('а')+'ккуратно кусает шею*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (		
						Text	(lambda: 'Грызь '+choice('за ногу', 'в шею')),
						Sticker	('CAADAQADPAcAApEpAAEQyoxTBUX3TsUWBA',),
					),
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (		
						Text	(lambda: 'Помогите!'), 
						Text	(lambda: 'Ааа, кусают!'),
						Sticker	('CAADAgADxQADrHkzBnUN64jQMLBoFgQ',),
					),
		'en': (None,),
		'ua': (None,),
	},
}