from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: '*'+name('у')+'кутывается в пледик*'), 
						Text	(lambda: 'Бррр!'), 
						Text	(lambda: '*'+name('д')+'рожит от холода*'), 
						Text	(lambda: '*'+name('в')+'ключает обогреватель*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (		
						Text	(lambda: '*'+name('ш')+'алит под котацу чтобы согрется*'), 
						Text	(lambda: '*'+name('д')+'рожит от холода прикасающихся рук*'), 
						Text	(lambda: '*'+name('г')+'реется, обнимая голышом*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (	
						Text	(lambda: '*'+name('в')+'ключает кондиционер*'), 
						Text	(lambda: '*'+name('т')+'ыкает мороженым в щеку*'), 
						Text	(lambda: '*'+name('п')+'ротягивает ледяной коктейль*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (		
						Text	(lambda: '*'+name('у')+'кутывается в пледик*'), 
						Text	(lambda: 'Бррр!'), 
						Text	(lambda: '*'+name('д')+'рожжит от холода*'), 
						Text	(lambda: '*'+name('в')+'ключает обогреватель*'),
					),
		'en': (None,),
		'ua': (None,),
	},
}