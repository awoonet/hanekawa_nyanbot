from static.answers import *

triggers = {
	r'\b([аa][вw][уo]+)\b'																		:awoo,
	r'\b([бb][аяa]+[кk][аa]+)\b'																:baka,
	r'\b(ку+ськ?)\b'																			:bite,
	r'\b(бу+льк?)\b'																			:bulk,
	r'\b(до встре+чи+)|(проща+(ва)?й(те)?)|((good )*bye)|(see you)\b'							:bye,
	r'\b((налей|(по)?дай) кофе)\b'																:coffee,
	r'\b((про)?хо*л[оа]дно(вато)?)\b'															:cold,
	r'\b(((по)?дай) печен(ьку|ек))\b'															:cookies,
	r'\b((facepalm)|(ф[еэ]йспалм))\b'															:facepalm,
	r'\b((приве+т(ству((ю)|(ем))*)*)|(здра+вствуй(те)*)|(ха+(й|юшки))|(h(i+|e(ll|ww)o+)))\b'	:hello,
	r'\b(хз)\b'																					:idk,
	r'\b(и та+к сойд[её]+т)\b'																	:itsok,
	r'\b((ц[её]+мк?)|(kiss))\b'																	:kiss,
	r'\b([лц]а+пк?)\b'																			:lapk,
	r'\b((ли+зьк?)|(li+ck))\b'																	:lick,
	r'\b((м+ех)|(me+h))\b'																		:meh,
	r'\b(((добро(го)? )?у+тр(е(чк)|ец)*а+)|(оха(ё|йо)+)|((доб)*ран((оч)*к[уа])))\b'				:morning,
	r'\b(([mp]u*r+k*)|([мп]у*р+к*))\b'															:mur,
	r'\b((но+чи)|(сно+в)|(оясуми(насай)?)|(good night)|(sweet dreams))\b'						:night,
	r'\b(((не|not) ){1}[нмnm][ьy]?[яa]+[нn]?[вфf]?[уu]*(c?k|к)?)\b'								:not_nyan,
	r'\b(нееш)\b'																				:notfood,
	r'\b((скороговорк[ау])|([нмnm][ьy]?[яa]+([hх][aа]){2,5}))\b'								:nyahaha,
	r'\b((?<!не )(?<!not )[нмnm][ьy]?[яa]+([нn]?|[вфf]?|[уu]*|(c?k|к)?))\b'						:nyan,
	r'\b(([рr]+[аяa]+[вw][рr]+)|(г?(r|р)[rр]+))\b'												:rawr,
	r'\bf\b'																					:respect,
	r'\b((ркн)|(rkn)|(роскомнадзор))\b'															:rkn,
	r'\b((rufus)|(руфус))\b'																	:rufus,
	r'\b((печаль(н(ова(т|(с*теньк)))*о))|(груст(ь|(н(ова(т|(с*теньк)))*о))))\b'					:sad,
	r'\b((налей|(по)?дай) ча(я|ю))\b'															:tea,
	r'\b(тыгыдык)\b'																			:tygydyk,
	r'\b((вас(три|3)к)|(vas(tri|3)k))\b'														:vas3k,
	r'\b((ви){2,5}|(vi){2,5})\b'																:vivivi,
	r'\b(жа+рко(вато)?)\b'																		:warm
}