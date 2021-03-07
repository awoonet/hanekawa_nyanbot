from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (	
						Text	(lambda: f"{choice('Н','М','н','м')}{randvoid('я')}{choice('', 'у', 'н', 'вк')}{face()}"),
						Text	(lambda: f"{choice('Ny','ny')}{randint('a')}{randvoid('n')}{face()}"),
						Other	(2),
						Sticker	(
											'CAADAgADaCkAAuCjggc25OCNdwABB-QWBA',
											'CAADAQADUAcAApEpAAEQJrWBxenFdf0WBA',
											'CAADAQADnyMAAnj8xgU0Q-u3iNi_BhYE',
											'CAADAgAD8QgAAotGbSd1yMpKZ2deghYE'
										),
					),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (	
						Text	(lambda: f"{choice('Н', 'М','н','м')}{randint('я')}{choice('', 'у', 'н', 'вк')}{face()}"),
						Text	(lambda: f"{choice('Ny', 'ny')}{randint('a')}{randvoid('n')}{face()}"),
						Other	(2),
						Sticker	(
											'CAADAgADaCkAAuCjggc25OCNdwABB-QWBA',
											'CAADAQADUAcAApEpAAEQJrWBxenFdf0WBA',
											'CAADAQADnyMAAnj8xgU0Q-u3iNi_BhYE',
											'CAADAgAD8QgAAotGbSd1yMpKZ2deghYE'
										),
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (		
						Text	(lambda: f'*{name("с")}тукает ладонью по голове*'), 
						Text	(lambda: 'Не някай тут.'),
						Text	(lambda: 'Рознякались тут.'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (		
						Text	(lambda: 'Н-н-н-я...'), 
						Text	(lambda: f'*{name("н")}якнула из-за дивана*'),
					),
		'en': (None,),
		'ua': (None,),
	},
}