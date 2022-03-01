from config import Client as app
from helpers.replier  import Replaier

@app.on_message(app.filters.group)
@app.with_db
def func(app, msg, user):
	Replaier(app, msg, user)
