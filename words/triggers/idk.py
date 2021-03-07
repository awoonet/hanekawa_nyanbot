from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: "Хрен знает!"),
						Sticker	(
											"CAADAgADxgADFTCdEMtnrnydTqyFFgQ",
											"CAADAgADxgADFTCdEMtnrnydTqyFFgQ",
											"CAADAgADXgADfEkIHLp8ZxiHco1PFgQ",
											"CAADAQADgyMAAnj8xgVdT-nJb8X-4RYE",
											"CAADAQADNxUAAnj8xgUDRa4NoDjQuxYE",
											"CAADAgAD5QQAAm8Odx33vxPNKJ2mbRYE",
											"CAADAgAD2gQAAm8Odx07gps43J10HBYE",
											"CAADAgADrjcAAuCjggcOsTcSgkzZghYE"
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