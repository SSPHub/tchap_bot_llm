from .config.settings import load_all
from .core.bot import create_bot
from .listeners import load_all as load_all_listeners


def run(prefix: str):
    creds, config, settings = load_all(prefix)

    bot = create_bot(creds, config)

    print("Loading listeners...")
    load_all_listeners(bot, settings.prefix)

    print("Starting bot...")
    bot.run()
