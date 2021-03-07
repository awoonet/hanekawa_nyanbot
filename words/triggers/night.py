from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: 'Доброй ночи'+nyah()+face()), 
						Text	(lambda: 'Приятных снов'+nyah()+face()), 
						Text	(lambda: 'Оясуми'+randvoid('насай')+nyah()+face()),
						Sticker	(
											'CAADAgADuGcAAuCjggcEK4Wuw6OReBYE',
											'CAADAgAD5h0AAuCjggekwJfpF4blcxYE',
											'CAADAgAD5x0AAuCjggfUw9fjxFR09BYE',
											'CAADBQADRwIAAunPYgjfF0mi4c26kRYE',
											'CAADAgADsyUAAuCjggerF63AIh5OCRYE',
											'CAADAgADt2cAAuCjggeEL-XEwL_VoRYE',
											'CAADAgAD32cAAuCjggeCGprfvE5HNBYE',
											'CAADAgAD4GcAAuCjggfs73jN2zfFeBYE',
											'CAADAgAD1mcAAuCjggcOLod87WZY0RYE',
											'CAADAgADpDcAAuCjggeHV6fwXeE7zxYE'
										),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (
						Text	(lambda: 'Эротических сновидений, *цем*'), 
						Text	(lambda: 'Доброй ночи'+nyah()+face()), 
						Text	(lambda: 'Оясуми'+randvoid('насай')+nyah()+face()),
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (		
						Text	(lambda: 'Надеюсь, ты не больше проснешься'), 
						Text	(lambda: 'Ты же больше не вернешься?'), 
						Text	(lambda: 'Наконец-то'),
					),	
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (		
						Text	(lambda: f'*{name("п")}ытается тихонько выйти из комнаты*'),
					),
		'en': (None,),
		'ua': (None,),
	},
}