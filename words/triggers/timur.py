from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: 'Копай, бля!'),
						Text	(lambda: f'*{name("п")}рячется за занавеской* >_<'),
						Sticker	(
											'CAADAgADWCkAAuCjggdo5gnw-q-JfRYE',
											'CAADAgADrDcAAuCjggft5Gh808VgXRYE'
										),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (None,),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (		
						Text	(lambda: f'*{name("в")}ыносит надоевший мусор*'),
					),	
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (		
					Text	(lambda: f'*{name("п")}рячется за занавеской* >_<'),
					),
		'en': (None,),
		'ua': (None,),
	},
}