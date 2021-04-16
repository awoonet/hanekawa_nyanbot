from classes.client import app

def vas3k(lang):
	start 		= {	
		'ru':"Интересные статьи:\n",
		'en':"Intresting articles:\n",
		'ua':"Цікаві статті:\n"
		}
	articles 	= {
		'computational_photography'	:{
			'ru':'Вычислительная фотография',
			'ua':'Обчислювальна фотографія',
			'en':'Computational Photography'
			},
		'augmented_reality'					:{
			'ru':'Дополненная реальность AR',
			'ua':'Доповнена реальність AR',
			'en':'Augmented Reality AR'
			},
		'machine_translation'				:{
			'ru':'Машинный перевод',
			'ua':'Машинний переклад',
			'en':'Machine Translation'
			},
		'quantum_computing'					:{
			'ru':'Квантовый компьютер',
			'ua':'Квантовий комп\'ютер',
			'en':'Quantum Сomputing'
			},
	}
	return start[lang]+"\n".join(f'<a href="https://vas3k.ru/blog/{x}/">{y[lang]}</a>' for x, y in articles.items())

answers = {
	'nyan': {	
		'ru': {
			'text' : vas3k('ru'),
		},
		'en': {
			'text' : vas3k('en'),
		},
		'ua': {
			'text' : vas3k('ua'),
		},
	},
	'lewd': {	
		'ru': {
			'text' : vas3k('ru'),
		},
		'en': {
			'text' : vas3k('en'),
		},
		'ua': {
			'text' : vas3k('ua'),
		},
	},
	'angr': {	
		'ru': {
			'text' : vas3k('ru'),
		},
		'en': {
			'text' : vas3k('en'),
		},
		'ua': {
			'text' : vas3k('ua'),
		},
	},
	'scar': {	
		'ru': {
			'text' : vas3k('ru'),
		},
		'en': {
			'text' : vas3k('en'),
		},
		'ua': {
			'text' : vas3k('ua'),
		},
	},
}


trigger = r'\b((вас(три|3)к)|(vas(tri|3)k))\b'
@app.on_message(app.filter_regex(trigger))
@app.decorator
def vas3k(app, msg, chat):
	chat.replier(app, msg, answers)