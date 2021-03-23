import time, requests

def find_ip():
	url = 'http://ipinfo.io/json'
	with requests.get(url) as response:
		response.raise_for_status()
		return response.json()

def turn_on(app):
	bot = app.get_me()

	json = find_ip()
	txt = f'**Turned on bot:**'
	txt+= f'\n`User:     {bot.first_name}`'
	txt+= f'\n`Username: @{bot.username}`'
	txt+= f'\n`User ID:  {bot.id}`'
	txt+= f'\n`Time:     {time.strftime("%y/%m/%d %H:%M:%S", time.localtime())}`'
	txt+= f'\n`Location: {json["city"]} ({json["country"]})`'
	txt+= f'\n`IP:       {json["ip"]}`'

	app.send_message(app.config_id, txt)

	return bot

