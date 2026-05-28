import os

import simplematrixbotlib as botlib
from openai import OpenAI


def register(bot: botlib.Bot, prefix: str) -> None:
    @bot.listener.on_message_event
    async def tchat_with_llm(room, message):
        match = botlib.MessageMatch(room, message, bot, prefix)

        if match.is_not_from_this_bot() and match.prefix() and match.command("llm"):
            prompt = generate_prompt(event_id=match.event.event_id)
            response_llm = ask(prompt=prompt)

            await bot.api.send_markdown_message(
                room_id=room.room_id,
                message=response_llm,
                reply_to=match.event.event_id,
            )


end_point = "https://llm.lab.sspcloud.fr/api"

openai_client = OpenAI(
    base_url=end_point,
    api_key=os.environ.get("LLM_LAB_API_KEY", ""),
)


def generate_prompt(event):
    """
    Function to generate the full prompt from an event id
    Arg:
        - event: a Matrix event
    Returns:
        - a list with history, from oldest to newest
    """
    event_id = event.event_id

    history = retrieve_history(event=event_id)

    prompt = add_system_prompt(history)

    return prompt


def history_append_top(history: list = [], role: str = "user", content: str = ""):
    """
    Function to add a message to history with role and content
    Args:
        - history: list : the history to append the message to
        - role: str : the role to give to the message
        - content: str : the content of the message
    """
    history_appended_top = [{"role": role, "content": content}] + history

    return history_appended_top


def get_model_name():
    model_name = "gemma4-26b-moe"
    return model_name


def add_system_prompt(history: list):
    history_with_system_prompt = (
        history_append_top(
            history=history,
            role="system",
            content="Respond with  markdown formatting. Do not use escape characters.",
        ),
    )

    return history_with_system_prompt


def ask(prompt: list):
    response = openai_client.chat.completions.create(
        model=get_model_name(),
        messages=prompt,
    )

    answer = response.choices[0].message.content
    return answer
