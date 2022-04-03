awoo = r"\b([аa][вw][уo]+)\b"
baka = r"\b([бb][аяa]+[кk][аa]+)\b"
bite = r"\b(ку+ськ?)\b"
bulk = r"\b(бу+льк?)\b"
lapk = r"\b([лц]а+пк?)|([пp][аa][вw]+)\b"
meh = r"\b((м+ех)|(me+h))\b"
not_nyan = r"\b(((не|not) ){1}[нмnm][ьy]?[яa]+[нn]?[вфf]?[уu]*(c?k|к)?)\b"
nyan = r"\b((?<!не )(?<!not )[нмnm][ьy]?[яa]+([нn]?|[вфf]?|[уu]*|(c?k|к)?))\b"
kiss = r"\b((ц[её]+мк?)|(kiss))\b"
lick = r"\b((л[иі]+зьк?)|(li+ck)|(lee+z))\b"
mur = r"\b(([mp]u*r+k*)|([мп]у*р+к*))\b"
rawr = r"\b(([рr]+[аяa]+[вw][рr]+)|(г?(r|р)[rр]+))\b"

facepalm = r"\b((facepalm)|(ф[еэ]йспалм))\b"
idk = r"\b(хз)\b"
itsok = r"\b(и та+к сойд[её]+т)\b"
notfood = r"\b(нееш)\b"
nyahaha = r"\b((скоро(говор|мов)к[ау])|([нмnm][ьy]?[яa]+([hх][aа]){2,5}))\b"
respect = r"\bf\b"
rkn = r"\b(([рr][кk][нn])(роскомнадзор))\b"
tygydyk = r"\b(т[иы]г[иы]д[иы]к)\b"
vivivi = r"\b(([вv][иіi]){2,5})\b"

cold = r"\b((про)?хо*л[оа]дно(вато)?)\b"
sad = r"\b((печаль(н(ова(т|(с*теньк)))*о))|(груст|сум(ь|(н(ова(т|(с*теньк)))*о))))\b"
warm = r"\b((жа+рк?|спек(от)?н?)(а+|овато)?)\b"

coffee = r"\b((нал[еи]й|(по)?дай) (кофе(йку)|кав[уи]))\b"
cookies = r"\b(((по)?дай) печ(ен(ьку|ек|ье|ю+ше*к[уи])|иво))\b"
tea = r"\b((нал[еи]й|(по)?дай) ча(я|ю))\b"

morning = (
    r"\b(((добро(го)? )?у+тр(е(чк)|ец)*а+)|(оха(ё|йо)+)|((доб)?ран((оч)*к[уа])))\b"
)
hello = r"\b((прив[еі]+т(ству((ю)|(ем))*)*)|(здра+вствуй(те)*)|(ха+(й|юшки))|(h(i+|e(l|w){2,2}o+)))\b"
bye = r"\b(до (встре+чи+|зу+стрічі+))|(проща+(ва)?й(те)?)|((good )*bye)|(see you)\b"
night = r"\b((но+ч[иі])|(сно+в)|(оясум[иі](насай)?)|(good night)|(sweet dreams))\b"

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
    ("memes", "facepalm", facepalm),
    ("memes", "idk", idk),
    ("memes", "itsok", itsok),
    ("memes", "notfood", notfood),
    ("memes", "nyahaha", nyahaha),
    ("memes", "respect", respect),
    ("memes", "rkn", rkn),
    ("memes", "tygydyk", tygydyk),
    ("memes", "vivivi", vivivi),
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
