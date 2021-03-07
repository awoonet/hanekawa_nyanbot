from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

F =(	
		Other	(6),
		Other	(7),
		Other	(8),
		Other	(9),
		Other	(10),
		Sticker	(
							"CAADAgAD2h0AAuCjggdT4wFdB92SAxYE",
							"CAADAgADSAADn-OXGFg_k6j563-iFgQ"
							),
	)
	
answers = {
	'nyan': {
		'ru': F,
		'en': F,
		'ua': F,
	},
	'lewd': {
		'ru': F,
		'en': F,
		'ua': F,
	},
	'angr': {
		'ru': F,
		'en': F,
		'ua': F,
	},
	'scar': {
		'ru': F,
		'en': F,
		'ua': F,
	},
}