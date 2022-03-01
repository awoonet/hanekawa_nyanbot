import re
from random import choice, randint
from helpers import TextHelper as t
from helpers.replier.dicts import *

class TextFormatter():
  def format_text(self, text):
    mood = self.chat.get_mood()
    lang = self.chat.get_lang()

    if re.search(r'[ⓊⒻⒶⓃⓋⓇⒸ]', text):
      text = text.replace('Ⓤ', f'**{t.username(self.msg.from_user)}**')
      text = text.replace('Ⓐ', choice(appelation_to_user[mood]))
      text = text.replace('Ⓕ', choice(faces[mood]))

      funcs = {
        'Ⓝ' : lambda txt: choice((*names[lang], txt.upper())).format(txt),
        'Ⓥ' : lambda txt: choice(('', txt)),
        'Ⓡ' : lambda txt: txt * randint(1, 6),
        'Ⓒ' : lambda txt: choice(txt.split(', ')),
      }

      i = 4
      while i > 0:
        for tag, func in funcs.items():
          if tag in text:
            
              txt = text.split(tag, maxsplit=2)
              answer = func(txt[1])
              text = f'{txt[0]}{answer}{txt[2]}'

              i+=1
          else:
            i-=1
            
    return text
