import os

import simplematrixbotlib as botlib

from ..config.settings import BotConfig, Creds


def create_bot(login_creds: Creds, bot_config: BotConfig) -> botlib.Bot:
    session_file = login_creds.session_stored_file
    session_dir = os.path.dirname(session_file)

    # Make sure the session directory exists.
    if session_dir:
        os.makedirs(session_dir, exist_ok=True)

    creds = botlib.Creds(
        homeserver=login_creds.homeserver,
        username=login_creds.username,
        password=login_creds.password,
        session_stored_file=session_file,
    )

    config = botlib.Config()
    config.emoji_verify = bot_config.emoji_verify
    config.ignore_unverified_devices = bot_config.ignore_unverified_devices
    config.encryption_enabled = bot_config.encryption_enabled

    # Keep the E2EE crypto store next to the session file so it persists on the
    # same volume.
    if session_dir:
        config.store_path = os.path.join(session_dir, "store")

    return botlib.Bot(creds, config)
