from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: f'Утр{randvoid("ечк")}а{nyah()}{face()}'),
						Text	(lambda: 'Привет'+nyah()+face()), 
						Text	(lambda: 'Охайо'+nyah()+face()),
						Sticker	(
											'CAADAgAD0mMAAuCjggfe1LWingZagRYE',
											'CAADAgADkCUAAuCjggeCPV98a6NIvhYE',
											'CAADAgADQikAAuCjggcJ3jT9RTZm-hYE',
											'CAADAgADXgEAAu243wpLqt8sTQivpRYE',
											'CAADAgAD2AADOYhhEqPQlBGL82DmFgQ',
											'CAADAgAD0mMAAuCjggfe1LWingZagRYE',
											'CAADAgADkCUAAuCjggeCPV98a6NIvhYE',
											'CAADAgADQikAAuCjggcJ3jT9RTZm-hYE',
											'CAADAgADwR0AAuCjggfyS_hgl5kxYRYE'
										),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (	
						Text	(lambda: f'Утр{randvoid("ечк")}а{choice(nyah()+face(),"не устал после вчерашнего?")}'),
						Text	(lambda: 'Привет'+nyah()+face()), 
						Text	(lambda: 'Охайо'+nyah()+face()),
						Sticker	(
											'CAADAgAD2AADOYhhEqPQlBGL82DmFgQ',
											'CAADAgADAwEAAjmIYRJkhs5iEOzAahYE'
										),
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (		
						Text	(lambda: 'Утра'+tsunbaka()), 
						Text	(lambda: 'Зачем приперся'+tsunbaka()+randvoid('!?')), 
						Text	(lambda: 'Иди, досыпай вечным сном'),
					),	
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (	
						Text	(lambda: 'Ут-тра...>_<'),
					),
		'en': (None,),
		'ua': (None,),
	},
}