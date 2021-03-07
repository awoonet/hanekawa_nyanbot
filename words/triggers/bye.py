from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text		(lambda: f'Пока{nyah()}{face()}'),
						Text		(lambda: f'До встречи{nyah()}{face()}'),
						Text		(lambda: f'Возвращайся{nyah()}{face()}'),
						Text		(lambda: f'Я буду ждать{nyah()}{face()}'),
						Text		(lambda: f'*{name("м")}ило машет рукой на прощание*'),
						Sticker	(	
											'CAADAgAD5x0AAuCjggfUw9fjxFR09BYE',
											'CAADBQADRwIAAunPYgjfF0mi4c26kRYE',
											'CAADAgADsyUAAuCjggerF63AIh5OCRYE',
											'CAADAgADpDcAAuCjggeHV6fwXeE7zxYE'
										),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (
						Text		(lambda: f'До встречи{nyah()}{face()}'),
						Text		(lambda: f'Возвращайся{nyah()}{face()}'),
						Text		(lambda: f'Я буду ждать{nyah()}{face()}'),
						Text		(lambda: f'*{name("м")}ило машет рукой на прощание*'),
						Text		(lambda: f'*{name("п")}осылает воздушный поцелуй*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (		
						Sticker	('CAADAgADJgEAAs6YzRZ-CemTFSRlGRYE',),
					),
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (
						Text		(lambda: f'Пока{randvoid(">_<")}'),
					),
		'en': (None,),
		'ua': (None,),
	},
}