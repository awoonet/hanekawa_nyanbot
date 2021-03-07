from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Sticker	('CAADAgAD_GcAAuCjggcc4yEXnt2GTBYE',),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (		
						Text	(lambda: f'*{name("р")}асстегивает пуговку расширяя декольте*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (		
						Text	(lambda: f'*{name("п")}ерехватывает руку* Не трогай!'),
					),	
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (		
						Text	(lambda: f"Ааа, не надо! *{name('у')}бегает в страхе*"),
					),
		'en': (None,),
		'ua': (None,),
	},
}