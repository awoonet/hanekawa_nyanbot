from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: '*'+name('о')+'ткрывает окно*'), 
						Text	(lambda: '*'+name('к')+'ушает мороженое*'), 
						Text	(lambda: '*'+name('в')+'ключает кондиционер*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (		
						Text	(lambda: '*'+name('с')+'адится голышом на подоконник*'), 
						Text	(lambda: '*'+name('п')+'ролила воду на маечку и та просвечивает*'), 
						Text	(lambda: '*'+name('р')+'аздевается, чтобы охладится*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (		
						Text	(lambda: '*'+name('в')+'ключает обогреватель*'), 
						Text	(lambda: '*'+name('п')+'одсыпает углей в печь*'), 
						Text	(lambda: '*'+name('в')+'ключает кондиционер на обогрев*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (		
						Text	(lambda: '*'+name('о')+'ткрывает окно*'), 
						Text	(lambda: '*'+name('в')+'ключает кондиционер*'),
					),
		'en': (None,),
		'ua': (None,),
	},
}