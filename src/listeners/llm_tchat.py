import os

import simplematrixbotlib as botlib
from openai import OpenAI


def register(bot: botlib.Bot, prefix: str) -> None:
    @bot.listener.on_message_event
    async def tchat_with_llm(room, message):
        match = botlib.MessageMatch(room, message, bot, prefix)

        if match.is_not_from_this_bot() and match.prefix() and match.command("llm"):
            response_llm = ask(match.event.body)
            await bot.api.send_text_message(
                room_id=room.room_id,
                message=response_llm,
                reply_to=match.event.event_id,
            )


end_point = "https://llm.lab.sspcloud.fr/api"

openai_client = OpenAI(
    base_url=end_point,
    api_key=os.environ.get("LLM_LAB_API_KEY", ""),
)


def get_model_name():
    model_name = "gemma4-26b-moe"
    return model_name


def format_msg(message: str):
    return [{"role": "user", "content": message}]


def ask(question: str):
    response = openai_client.chat.completions.create(
        model=get_model_name(),
        messages=format_msg(question),
    )

    answer = response.choices[0].message.content
    return answer
