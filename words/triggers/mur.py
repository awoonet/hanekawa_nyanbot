from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: choice('М','П')+randint('у')+randint('р')+face()),
						Text	(lambda: choice('M','P')+randint('u')+randint('r')+face()),
						Sticker	('CAADAQADUAcAApEpAAEQJrWBxenFdf0WBA',),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (	
						Text	(lambda: choice('М','П')+randint('у')+randint('р')+face()),
						Text	(lambda: choice('M','P')+randint('u')+randint('r')+face()),
						Sticker	('CAADAQADUAcAApEpAAEQJrWBxenFdf0WBA',),
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
	
		'ru': (		
						Text	(lambda: '*'+name('с')+'верлит взглядом*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (		
						Text	(lambda: 'Мр'), 
						Text	(lambda: f'*{name("и")}спуганно тихо мурлыкает*'),
					),
		'en': (None,),
		'ua': (None,),
	},
}