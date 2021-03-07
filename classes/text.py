from random import choice, randint

class Q:
	@staticmethod
	def choice(*x):	
		return choice(x)
	@staticmethod
	def randint(x):	
		return x * randint(1, 6)
	def randvoid(self, x):	
		return self.choice('', x)
	def face		(self):			
		faces	= ('', '', ' =^_^=',' ^_^', ' *-*', ' ^-^', '~', '^^', '))')
		return choice(faces)
	def name		(self, x):	
		names = ('Ханекава', 'Ханекава Тсубаса', 'Някава')
		return self.choice(f'{choice(names)} {x}', x.upper())
	def nyah		(self):			
		cutie		=	(', няха', ', няшка', ', милашка')
		kitty		= (', котенок', ', котеночек')
		lapa		=	(', лапочка', ', лапа')
		rabbit	= (', крольчёнок', ', зайчик')
		return self.choice('', cutie, kitty, lapa, rabbit)
	def tsunbaka(self):
		baka = (', придурок', ', дурак', ', бака', ', идиот')	
		return self.choice('', baka)
