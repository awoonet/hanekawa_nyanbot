from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: 'Привет'+randvoid('ствую')+nyah()+face()), 
						Text	(lambda: 'Здравствуй'+nyah()+face()),
						Sticker	(
											'CAADAgAD0mMAAuCjggfe1LWingZagRYE',
											'CAADAgADkCUAAuCjggeCPV98a6NIvhYE',
											'CAADAgADQikAAuCjggcJ3jT9RTZm-hYE',
											'CAADAgADwR0AAuCjggfyS_hgl5kxYRYE',
										),
					),
		'en': (	
						Text	(lambda: 'Привет'+randvoid('ствую')+nyah()+face()), 
						Text	(lambda: 'Здравствуй'+nyah()+face()),
						Sticker	(
											'CAADAgAD0mMAAuCjggfe1LWingZagRYE',
											'CAADAgADkCUAAuCjggeCPV98a6NIvhYE',
											'CAADAgADQikAAuCjggcJ3jT9RTZm-hYE',
											'CAADAgADwR0AAuCjggfyS_hgl5kxYRYE',
										),
					),
		'ua': (	
						Text	(lambda: 'Привет'+randvoid('ствую')+nyah()+face()), 
						Text	(lambda: 'Здравствуй'+nyah()+face()),
						Sticker	(
											'CAADAgAD0mMAAuCjggfe1LWingZagRYE',
											'CAADAgADkCUAAuCjggeCPV98a6NIvhYE',
											'CAADAgADQikAAuCjggcJ3jT9RTZm-hYE',
											'CAADAgADwR0AAuCjggfyS_hgl5kxYRYE',
										),
					),
	},
	'lewd': {
		'ru': (		
						Text	(lambda: '*'+name('п')+'риветственно целует*'),
						Sticker	('CAADAgADCAAD5ODJIxqwyU-ZhSOBFgQ',),
					),
		'en': (		
						Text	(lambda: '*'+name('п')+'риветственно целует*'),
						Sticker	('CAADAgADCAAD5ODJIxqwyU-ZhSOBFgQ',),
					),
		'ua': (		
						Text	(lambda: '*'+name('п')+'риветственно целует*'),
						Sticker	('CAADAgADCAAD5ODJIxqwyU-ZhSOBFgQ',),
					),
	},
	'angr': {
		'ru': (		
						Text	(lambda: 'Что ты тут забыл'+g()+randvoid('!?')), 
						Text	(lambda: 'Проваливай'+g()+randvoid('!')),
					),
		'en': (		
						Text	(lambda: 'Что ты тут забыл'+g()+randvoid('!?')), 
						Text	(lambda: 'Проваливай'+g()+randvoid('!')),
					),
		'ua': (		
						Text	(lambda: 'Что ты тут забыл'+g()+randvoid('!?')), 
						Text	(lambda: 'Проваливай'+g()+randvoid('!')),
					),
	},
	'scar': {
		'ru': (		
						Text	(lambda: 'Здравствуй'),
					),
		'en': (		
						Text	(lambda: 'Здравствуй'),
					),
		'ua': (		
						Text	(lambda: 'Здравствуй'),
					),
	},
}