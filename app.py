import coloredlogs
from app_init import app_init

coloredlogs.install(level='INFO')

app = app_init()

app.run()
