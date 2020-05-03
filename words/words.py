from words.ru.nyan import nyan as ru_nyan
from words.ru.lewd import lewd as ru_lewd
from words.ru.angr import angr as ru_angr
from words.ru.scar import scar as ru_scar

from words.en.nyan import nyan as en_nyan
from words.en.lewd import lewd as en_lewd
from words.en.angr import angr as en_angr
from words.en.scar import scar as en_scar

reacts = {	'ru': {	'nyan':ru_nyan,
					'lewd':ru_lewd,
					'angr':ru_angr,
					'scar':ru_scar,	},
			'en': {	'nyan':en_nyan,
					'lewd':en_lewd,
					'angr':en_angr,
					'scar':en_scar,	}	}

triggers = {	('ня+к*н*у*', 'nya+k*n*',
				 'мя+у*ф*',   'my+a+f*')				: 'nyan',
				('му*рк*', 'mu*r+', 
				 'пу+р+',  'pu*r+')						: 'mur',
				('awo+', 'аву+')						: 'awoo',
				('ку+сь',)								: 'bite',
				('ли+зь',)								: 'lick',
				('це+мк*',)								: 'kiss',
				('ла+пк',)								: 'lapk',
				('ра+вр+', 'ррр+', 'ra+wr+', 'rrr+')	: 'rawr',

				('ме+х','me+h')							: 'meh',
				('бу+ль',)								: 'bulk',
				('ба+ка+', 'ba+ka+')					: 'baka',
				('хз',)									: 'idk',
				(r'^f$',)								: 'respect',
				('facepalm', 'фе*э*йспалм', 'рукалицо')	: 'facepalm',
				('ркн', 'роскомнадзор', 'rkn')			: 'rkn',
				('нееш',)								: 'notfood',

				('утре*[чк]*ц*а', 'охаё*[йо]*')			: 'morning',
				('ночи', 'снов', 'оясуми[насай]*')		: 'night',
				('приве+т', 'здравствуй')				: 'hello',
				('пока+', 'до встре+чи', 
					'проща+й', 'bye', 'see you')		: 'bye',

				('жарков*а*т*о*', )						: 'warm',
				('холоднов*а*т*о*', 'прохладно')		: 'cold',
				('грусть*[но]*',)						: 'sad',

				('тыгыдык',)							: 'tygydyk',
				('вививи',)								: 'vivivi',

				('тимур',)								: 'timur',
				('computational photography',)			: 'comp_p',
			} 