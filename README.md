# Hanekawa Nyan Bot

Telegram bot made with pyrogram. Made to add some cutines in your chat!)

## Installation

- You should have installed and working PostgreSQL database.

- Clone this repository and add .env file.

- Install all dependencies by:

```
python3 -m pip install -r requirements.txt
```

- You need add this environment variables:

  - API_ID, API_HASH - obtain on [telegram register app page](https://my.telegram.org/apps)
  - BOT_TOKEN - obtain from telegram bot for registring bots - [BotFather](https://t.me/BotFather)
  - DATABASE_URL - link in format `postgres://USER:PASSWORD@LINK_TO_DB:5432/DATABASE_NAME`

  - MEDIA_REACTIONS_STORAGE - channel with media reactions
  - CONFIG_MESSAGES - channel to receive error messages
  - IGNORED_USERS - set with user ids, for bot replier ignorance

## Deploy

- You can start bot on your machine or in Docker.

  - If you would use docker, make `/app/session` as docker volume.

- It has config file for CapRover self-hosted PaaS as well.

- If you want to start up it on Heroku, please add `Procfile` with content:

```
worker: python3 app.py
```

## Bot possibilities

- Bot can reply on triggers setted up in `static/triggers.py`.

- Can answer on commands: `/me, /pat, /hug, /boop, /jamk, /lapk, /koos, /lick, /kiss`.

- Use `/config` to set up bot parameters in this chat. (Only for chat admins)
