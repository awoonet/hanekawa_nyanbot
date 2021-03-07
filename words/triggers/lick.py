from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: f"Лизь {choice('тебя <3', '<3', '~')} "), 
						Text	(lambda: '*покраснела*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (		
						Text	(lambda: "Лизь тебя в щечку"), 
						Text	(lambda: '*покраснела*'), 
						Text	(lambda: f'*{name("н")}ежно ли{choice("зь", "жет")} ушко'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (		
						Text	(lambda: '*'+name('o')+'твешивает оплеуху и уходит*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (		
						Text	(lambda: 'Отстань, извращенец!'), 
						Text	(lambda: f'*{name("с")}жалась от страха, не в силах пошевелится*'),
					),
		'en': (None,),
		'ua': (None,),
	},
}