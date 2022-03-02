awoo = r"\b([аa][вw][уo]+)\b"
baka = r"\b([бb][аяa]+[кk][аa]+)\b"
bite = r"\b(ку+ськ?)\b"
bulk = r"\b(бу+льк?)\b"
lapk = r"\b([лц]а+пк?)\b"
meh = r"\b((м+ех)|(me+h))\b"
not_nyan = r"\b(((не|not) ){1}[нмnm][ьy]?[яa]+[нn]?[вфf]?[уu]*(c?k|к)?)\b"
nyan = r"\b((?<!не )(?<!not )[нмnm][ьy]?[яa]+([нn]?|[вфf]?|[уu]*|(c?k|к)?))\b"
kiss = r"\b((ц[её]+мк?)|(kiss))\b"
lick = r"\b((ли+зьк?)|(li+ck))\b"
mur = r"\b(([mp]u*r+k*)|([мп]у*р+к*))\b"
rawr = r"\b(([рr]+[аяa]+[вw][рr]+)|(г?(r|р)[rр]+))\b"
tygydyk = r"\b(тыгыдык)\b"
vivivi = r"\b((ви){2,5}|(vi){2,5})\b"

facepalm = r"\b((facepalm)|(ф[еэ]йспалм))\b"
idk = r"\b(хз)\b"
itsok = r"\b(и та+к сойд[её]+т)\b"
notfood = r"\b(нееш)\b"
nyahaha = r"\b((скороговорк[ау])|([нмnm][ьy]?[яa]+([hх][aа]){2,5}))\b"
respect = r"\bf\b"
rkn = r"\b((ркн)|(rkn)|(роскомнадзор))\b"

cold = r"\b((про)?хо*л[оа]дно(вато)?)\b"
sad = r"\b((печаль(н(ова(т|(с*теньк)))*о))|(груст(ь|(н(ова(т|(с*теньк)))*о))))\b"
warm = r"\b(жа+рко(вато)?)\b"

coffee = r"\b((налей|(по)?дай) кофе(йку))\b"
cookies = r"\b(((по)?дай) печен(ьку|ек|ье))\b"
tea = r"\b((налей|(по)?дай) ча(я|ю))\b"

morning = (
    r"\b(((добро(го)? )?у+тр(е(чк)|ец)*а+)|(оха(ё|йо)+)|((доб)*ран((оч)*к[уа])))\b"
)
hello = r"\b((приве+т(ству((ю)|(ем))*)*)|(здра+вствуй(те)*)|(ха+(й|юшки))|(h(i+|e(ll|ww)o+)))\b"
bye = r"\b(до встре+чи+)|(проща+(ва)?й(те)?)|((good )*bye)|(see you)\b"
night = r"\b((но+чи)|(сно+в)|(оясуми(насай)?)|(good night)|(sweet dreams))\b"

triggers = (
    ("nyan", "awoo", awoo),
    ("nyan", "baka", baka),
    ("nyan", "bite", bite),
    ("nyan", "bulk", bulk),
    ("nyan", "lapk", lapk),
    ("nyan", "meh", meh),
    ("nyan", "not_nyan", not_nyan),
    ("nyan", "nyan", nyan),
    ("nyan", "kiss", kiss),
    ("nyan", "lick", lick),
    ("nyan", "mur", mur),
    ("nyan", "rawr", rawr),
    ("nyan", "tygydyk", tygydyk),
    ("nyan", "vivivi", vivivi),
    ("memes", "facepalm", facepalm),
    ("memes", "idk", idk),
    ("memes", "itsok", itsok),
    ("memes", "notfood", notfood),
    ("memes", "nyahaha", nyahaha),
    ("memes", "respect", respect),
    ("memes", "rkn", rkn),
    ("empathic", "cold", cold),
    ("empathic", "sad", sad),
    ("empathic", "warm", warm),
    ("food", "coffee", coffee),
    ("food", "cookies", cookies),
    ("food", "tea", tea),
    ("greeters", "morning", morning),
    ("greeters", "hello", hello),
    ("greeters", "bye", bye),
    ("greeters", "night", night),
)
