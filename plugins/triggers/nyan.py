from classes.client import app

answers = {
	'nyan': {
		'ru': {	
			'text' : ("ⒸН, М, н, мⒸⓇяⓇⒸ , у, н, вкⒸⒻ",
								"ⒸN, M, n, mⒸyⓇaⓇⓋnⓋⒻ"),
			'media': (2,
								'CAADAgADaCkAAuCjggc25OCNdwABB-QWBA',
								'CAADAQADUAcAApEpAAEQJrWBxenFdf0WBA',
								'CAADAQADnyMAAnj8xgU0Q-u3iNi_BhYE',
								'CAADAgAD8QgAAotGbSd1yMpKZ2deghYE'),
		},
		'en': {	
			'text' : "ⒸN, M, n, mⒸyⓇaⓇⓋnⓋⒻ",
			'media': (2,
								'CAADAgADaCkAAuCjggc25OCNdwABB-QWBA',
								'CAADAQADUAcAApEpAAEQJrWBxenFdf0WBA',
								'CAADAQADnyMAAnj8xgU0Q-u3iNi_BhYE',
								'CAADAgAD8QgAAotGbSd1yMpKZ2deghYE'),
		},
		'ua': { 
			'none' : True, 
			},
	},
	'lewd': {
		'ru': {	
			'text' : ("ⒸН, М, н, мⒸⓇяⓇⒸ , у, н, вкⒸⒻ",
								"ⒸN, M, n, mⒸyⓇaⓇⓋnⓋⒻ"),
			'media': (2,
								'CAADAgADaCkAAuCjggc25OCNdwABB-QWBA',
								'CAADAQADUAcAApEpAAEQJrWBxenFdf0WBA',
								'CAADAQADnyMAAnj8xgU0Q-u3iNi_BhYE',
								'CAADAgAD8QgAAotGbSd1yMpKZ2deghYE'),
		},
		'en': {	
			'text' : "ⒸN, M, n, mⒸyⓇaⓇⓋnⓋⒻ",
			'media': (2,
								'CAADAgADaCkAAuCjggc25OCNdwABB-QWBA',
								'CAADAQADUAcAApEpAAEQJrWBxenFdf0WBA',
								'CAADAQADnyMAAnj8xgU0Q-u3iNi_BhYE',
								'CAADAgAD8QgAAotGbSd1yMpKZ2deghYE'),
		},
		'ua': { 
			'none' : True, 
			},
	},
	'angr': {
		'ru': {	
			'text' : ('*ⓃсⓃтукает ладонью по голове*',
								'ⒸНе някай, РознякалисьⒸ тут.'),
		},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
	'scar': {
		'ru': {	
			'text' : ('Н-н-н-я...',
								'*ⓃнⓃякнула из-за дивана*'),
		},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b([нмnm][ьy]?[яa]+[нn]?[вфf]?[уu]*(c?k|к)?)\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def nyan(app, msg, chat):
	chat.replier(app, msg, answers)