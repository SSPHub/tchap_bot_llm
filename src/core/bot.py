import os

import simplematrixbotlib as botlib

from ..config.settings import BotConfig, Creds


def create_bot(login_creds: Creds, bot_config: BotConfig) -> botlib.Bot:

    # Make sure the session directory exists.
    session_dir = os.path.dirname(login_creds.session_stored_file)

    if session_dir:
        os.makedirs(session_dir, exist_ok=True)

    creds = botlib.Creds(
        homeserver=login_creds.homeserver,
        username=login_creds.username,
        password=login_creds.password,
        session_stored_file=login_creds.session_stored_file,
    )

    config = botlib.Config()
    config.emoji_verify = bot_config.emoji_verify
    config.ignore_unverified_devices = bot_config.ignore_unverified_devices
    config.encryption_enabled = bot_config.encryption_enabled
    config.store_path = bot_config.store_path

    return botlib.Bot(creds, config)
