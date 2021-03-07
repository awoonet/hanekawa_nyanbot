import words.triggers

re_triggers = {		
	r'[аa][вw][уo]+'														: words.triggers.awoo,
	r'[бb][аяa]+[кk][аa]+'											: words.triggers.baka,
	r'ку+ськ?'																	: words.triggers.bite,
	r'бу+льк?'																	: words.triggers.bulk,

	r'до встре+чи+'															: words.triggers.bye,
	r'проща+(ва)?й(те)?'												: words.triggers.bye,
	r'(good )*bye'															: words.triggers.bye,
	r'see you'																	: words.triggers.bye,

	r'(про)?хо*л[оа]дно(вато)?'									: words.triggers.cold,
	r'[fф][aеэ]й*[cс]e*[pп][aа][lл][mм]'				: words.triggers.facepalm,
	r'скороговорк[ау]'													: words.triggers.nyahaha,

	r'приве+т(ств((ую)|(ем))*)*'								: words.triggers.hello,
	r'здра+вствуй(те)*'													: words.triggers.hello,
	r'ха+й'																			: words.triggers.hello,
	r'hi+'																			: words.triggers.hello,
	r'hello+'																		: words.triggers.hello,

	r'хз'																				: words.triggers.idk,
	r'и та+к сойд[её]+т'												: words.triggers.itsok,

	r'це+мк?'																		: words.triggers.kiss,
	r'ла+пк?'																		: words.triggers.lapk,
	r'ли+зьк?'																	: words.triggers.lick,
	r'li+ck'																		: words.triggers.lick,

	r'[мm][еe]+[хh]'														: words.triggers.meh,

	r'у+тр(е(чк)|ец)*а+'												: words.triggers.morning,
	r'оха(ё|йо)+'																: words.triggers.morning,
	r'(доб)*ран((оч)*к[уа])'										: words.triggers.morning,

	r'[мпmp][уu]*[рr]+[кk]*'										: words.triggers.mur,

	r'но+чи'																		: words.triggers.night,
	r'сно+в'																		: words.triggers.night,
	r'оясуми(насай)?'														: words.triggers.night,
	r'good night'																: words.triggers.night,
	r'dreams'																		: words.triggers.night,

	r'нееш'																			: words.triggers.notfood,

	r'[нмnm][ьy]?[яa]+([hх][aа])([hх][aа])+'		: words.triggers.nyahaha,
	r'[нмnm][ьy]?[яa]+[нn]?[вфf]?[уu]*c?[кk]?'	: words.triggers.nyan,

	r'[рr]+[аяa]+[вw][рr]+'											: words.triggers.rawr,
	r'г?(r|р)[rр]+'															: words.triggers.rawr,

	r'f'																				: words.triggers.respect,

	r'[rр][kк][nн]'															: words.triggers.rkn,
	r'роскомнадзор'															: words.triggers.rkn,

	r'[rр][uу][fф][uу][sс]'											: words.triggers.rufus,

	r'груст(ь|(н(ова(т|(стеньк)))*о))'					: words.triggers.sad,
	r'печаль(н(ова(т|(с*теньк)))*о)'						: words.triggers.sad,

	r'тиму+р+'																	: words.triggers.timur,

	r'ты(гы)+(дык)+'														: words.triggers.tygydyk,

	r'[вv][аa][сs](3|три)[кk]'									: words.triggers.vas3k,

	r'ви(ви)+'																	: words.triggers.vivivi,
	
	r'жа+рко(вато)?'														: words.triggers.warm,
} 