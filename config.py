#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6403785146:AAFZrpcYWKHjsDIkGvFBZZYkxDgJcKi1ZeM")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "29310987"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "336c28913a45587a4c10af8cd620b68f")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6515901556").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
