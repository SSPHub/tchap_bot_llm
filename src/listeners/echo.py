from datetime import datetime
from zoneinfo import ZoneInfo

import simplematrixbotlib as botlib


def register(bot: botlib.Bot, prefix: str) -> None:
    @bot.listener.on_message_event
    async def echo(room, message):
        match = botlib.MessageMatch(room, message, bot, prefix)

        if match.is_not_from_this_bot() and (
            match.command("coucou") or match.command("Coucou")
        ):
            await bot.api.send_text_message(
                room.room_id,
                "Coucou, il est "
                + datetime.now(ZoneInfo("Europe/Paris")).strftime("%H:%M:%S")
                + " à Paris.",
            )
