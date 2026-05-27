import simplematrixbotlib as botlib

from ..config.settings import BotConfig, Creds


def create_bot(login_creds: Creds, bot_config: BotConfig) -> botlib.Bot:
    creds = botlib.Creds(
        homeserver=login_creds.homeserver,
        username=login_creds.username,
        password=login_creds.password,
    )

    config = botlib.Config()
    config.emoji_verify = bot_config.emoji_verify
    config.ignore_unverified_devices = bot_config.ignore_unverified_devices
    config.encryption_enabled = bot_config.encryption_enabled

    return botlib.Bot(creds, config)
