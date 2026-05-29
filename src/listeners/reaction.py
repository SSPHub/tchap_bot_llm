import simplematrixbotlib as botlib


def register(bot: botlib.Bot, prefix: str) -> None:
    @bot.listener.on_message_event
    async def react_to_proxy(room, message):
        match = botlib.MessageMatch(room, message, bot)
        example_reaction = "😖"
        if match.is_not_from_this_bot() and match.contains("proxy"):
            await bot.api.send_reaction(
                room_id=room.room_id, event=message, key=example_reaction
            )

            # await bot.api.send_text_message(
            #     room_id=room.room_id,
            #     message=f"I reacted to your message {match.event.body}",
            #     reply_to=match.event.event_id,
            # )
