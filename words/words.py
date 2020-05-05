from words.ru.nyan import nyan as ru_nyan
from words.ru.lewd import lewd as ru_lewd
from words.ru.angr import angr as ru_angr
from words.ru.scar import scar as ru_scar

from words.en.nyan import nyan as en_nyan
from words.en.lewd import lewd as en_lewd
from words.en.angr import angr as en_angr
from words.en.scar import scar as en_scar

reacts = {	'ru': {'nyan':ru_nyan,'lewd':ru_lewd,'angr':ru_angr,'scar':ru_scar,},
			'en': {'nyan':en_nyan,'lewd':en_lewd,'angr':en_angr,'scar':en_scar,}}

triggers = {	r'\b[нмnm][ьy]?[яa]+[нn]?[вфf]?[уu]*c?[кk]?([hх][aа])*\b'
														: 'nyan',
				r'\b[мпmp][уu]*[рr]+[кk]*\b'			: 'mur',
				r'\b[аa][вw][уo]+\b'					: 'awoo',
				r'\bку+ськ?\b'							: 'bite',
				r'\b(ли+зьк?)|(li+ck)\b'				: 'lick',
				r'\bце+мк?\b'							: 'kiss',
				r'\bла+пк?\b'							: 'lapk',
				r'\b([рr][аяa][вw][рr]+)|([rр]{3})\b'	: 'rawr',
				r'\b[мm][еe]+[хh]\b'					: 'meh',
				r'\bбу+льк?\b'							: 'bulk',
				r'\b[бb][аяa]+[кk][аa]+\b'				: 'baka',
				r'\bхз\b'								: 'idk',
				r'\bf\b'								: 'respect',
				r'\b[fф][aеэ]й*[cс]e*[pп][aа][lл][mм]|(рукалицо)\b'						
														: 'facepalm',
				r'\b([rр][kк][nн])|(роскомнадзор)\b'	: 'rkn',
				r'\bнееш'								: 'notfood',
				r'\b(утр(е(чк)|ец)*а+)|(оха(ё|йо)+)|((доб)*ран((оч)*к[уа]))\b' 			
														: 'morning',
				r'\b(ночи)|(снов)|(оясуми(насай)?)|(good night)|(dreams)\b'	
														: 'night',
				r'\b(приве+т)|(здра+вствуй)|(hi)|(hello)\b'
														: 'hello',
				r'\b(пока+)|(до встре+чи)|(проща+й)|((good)*bye)|(see you)\b'
														: 'bye',
				r'\bжарко(вато)?\b'						: 'warm',
				r'\b(про)?хо?л[оа]дно(вато)?\b'			: 'cold',
				r'\bгруст(ь|(н(ова(т|(стеньк)))*о))\b'	: 'sad',
				r'\bты(гы)+(дык)+\b'					: 'tygydyk',
				r'\b(ви)+\b'							: 'vivivi',
				r'\bтимур\b'							: 'timur',
				r'\bи та+к сойд[её]+т\b'				: 'itsok',
				r'\b[rр][uу][fф][uу][sс]\b'				: 'rufus',
				r'\b[вv][аa][сs](3|три)[кk]\b'			: 'vas3k',
			} 