import simplematrixbotlib as botlib
import os
from datetime import datetime
from zoneinfo import ZoneInfo

creds = botlib.Creds(
    "https://matrix.agent.finances.tchap.gouv.fr", 
    os.environ["TCHAP_BOT_SSPHUB_MATRIX_ID"], 
    os.environ["TCHAP_BOT_SSPHUB_PWD"],
    session_stored_file="session.txt")

config = botlib.Config()
config.emoji_verify = True
config.ignore_unverified_devices = True
config.encryption_enabled = True

bot = botlib.Bot(creds, config)
PREFIX = '!'

@bot.listener.on_message_event
async def echo(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.command("coucou"):

        await bot.api.send_text_message(
            room.room_id, "Coucou, il est " + datetime.now(ZoneInfo("Europe/Paris")).strftime("%H:%M:%S") + " à Paris."
            )

@bot.listener.on_message_event
async def example(room, message):
    match = botlib.MessageMatch(room, message, bot)
    example_reaction = "✅"
    if match.is_not_from_this_bot() and match.contains('href'):
        await bot.api.send_reaction(
            room_id=room.room_id,
            event=message,
            key=example_reaction)

        await bot.api.send_text_message(
                room_id=room.room_id,
                message=f"I reacted to your message {match.event.body}", 
                reply_to=match.event.event_id)

bot.run()
