from os import getenv as env
import urllib.parse as urlparse

from pony.orm import *

from db.model_chat import generate_chat
from db.model_user import generate_user


def postgresql_credentials() -> dict:
    if not env("DATABASE_URL"):
        return dict(
            provider="postgres",
            user=env("PSQL_USER"),
            password=env("PSQL_PASS"),
            host=env("PSQL_HOST"),
            database=env("DB_NAME"),
        )

    else:
        url = urlparse.urlparse(env("DATABASE_URL"))
        return dict(
            provider="postgres",
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port,
            database=url.path[1:],
        )


def db_init() -> tuple:

    db = Database()

    Chat = generate_chat(db)
    User = generate_user(db, Chat)

    db.bind(**postgresql_credentials())
    db.generate_mapping(create_tables=True)

    print("DB initialized.", flush=True)
    return db, Chat, User
