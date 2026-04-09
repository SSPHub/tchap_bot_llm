import simplematrixbotlib as botlib
import os

creds = botlib.Creds(
    "https://matrix.agent.finances.tchap.gouv.fr", 
    os.environ["TCHAP_BOT_SSPHUB_MATRIX_ID"], 
    os.environ["TCHAP_BOT_SSPHUB_PWD"],
    "session.txt")

config = botlib.Config()
config.emoji_verify = True
config.ignore_unverified_devices = True
config.encryption_enabled = True

bot = botlib.Bot(creds, config)
PREFIX = '!'

@bot.listener.on_message_event
async def echo(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("echo"):

        await bot.api.send_text_message(
            room.room_id, " ".join(arg for arg in match.args())
            )

@bot.listener.on_message_event
async def example(room, message):
    match = botlib.MessageMatch(room, message, bot)
    example_reaction = "✅"
    if match.is_not_from_this_bot() and match.prefix() and match.contains(r'\[([^\]]+)\]\(([^)]+)\)'):
        await bot.api.send_reaction(
            room_id=room.room_id,
            event=message,
            key=example_reaction)

bot.run()
