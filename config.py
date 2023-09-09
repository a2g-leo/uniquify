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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQG_QAsACwSgA9Tui629xHr8z9nRtXOY2Ujty12pOtyaoSgZAEj-0ndI6B2A1fCsJoOp5SqIAmJnmqBCPzMgE2OAiNDUf6vIqruMyRm3o1pYG0GptlJCQTeh8KHL52bD5tPIeT0EvE2nGoUst9jJhEbLJG6uYJbtfmvPDRCFWZ_T3NIK3B-Dd6LX0-jjNyvo3KrZ4IcaNF0zaxbbTH-mpDD6bhsD-kFeiNdWHGHuk73kpIMxd4aySHlJwTetgOO_2Zxk1fE8Jmd6_YGP4euag0MQ4x2MTNqK7Q9m-lhaLoVP24YwAf37-oBqwH-KR_ZqVH7fv_7ZpLOno11RnxoPC4FWXA16GAAAAAGEYMR0AA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
