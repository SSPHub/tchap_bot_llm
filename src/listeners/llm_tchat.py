import os

import nio
import simplematrixbotlib as botlib
from openai import OpenAI

end_point = "https://llm.lab.sspcloud.fr/api"

openai_client = OpenAI(
    base_url=end_point,
    api_key=os.environ.get("LLM_LAB_API_KEY", ""),
)


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


def get_in_reply_to_event_id(event):
    return event.get("content").get("m.relates_to").get("m.in_reply_to").get("event_id")


def get_role_event(event, bot):
    if event.sender == bot.async_client.user_id:
        return "assistant"
    else:
        return "user"


def extract_info(event) -> tuple | None:
    """
    Extract info from event.  Returns sender, body, and replied-to event ID
    """

    content = event.source.get("content", {})

    sender = event.sender
    body = content.get("body")
    replied_to_id = get_in_reply_to_event_id(event=event)

    return (sender, body, replied_to_id)


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


def register(bot: botlib.Bot, prefix: str) -> None:
    @bot.listener.on_message_event
    async def tchat_with_llm(room, message):
        match = botlib.MessageMatch(room, message, bot, prefix)

        if match.is_not_from_this_bot() and match.prefix() and match.command("llm"):
            prompt = generate_prompt(bot, room.room_id, match=match)
            response_llm = ask(prompt=prompt)

            await bot.api.send_markdown_message(
                room_id=room.room_id,
                message=response_llm,
                reply_to=match.event.event_id,
            )

    async def generate_prompt(bot: botlib.Bot, room_id: str, match):
        """
        Function to generate the full prompt from an event id
        Arg:
            - bot: botlib.Bot
            - room_id: str : the Matrix room id where the message is
            - match: a simplebot match
        Returns:
            - a list with history, from oldest to newest
        """
        history = history_append_top(history=[], role="user", content=match.event.body)

        reply_id = get_in_reply_to_event_id(match.event)

        if reply_id != "":
            history = retrieve_history(bot, room_id, reply_event_id=reply_id) + history

        prompt = add_system_prompt(history)

        return prompt

    async def retrieve_history(bot: botlib.Bot, room_id: str, reply_event_id: str):
        """
        Retrieves full history of chat in this discussion between the LLM and the user.
        History is defined by message being sent in reply to a message
        Args :
        - bot : the botlib bot. Used to fetch back other message
        - room_id : the room to search for past message
        - reply_event_id: the id of the message replied to
        """

        event = get_event(bot, room_id, reply_event_id)
        sender, body, reply_id_level2 = extract_info(event)
        role = get_role_event(event=event, bot=bot)

        if reply_id_level2 != "":
            history = retrieve_history(bot, room_id, reply_id_level2)
            return history_append_top(history=history, role=role, content=body)
        else:
            return history_append_top(history=[], role=role, content=body)

    async def get_event(bot: botlib.Bot, room_id: str, event_id: str):
        """
        Fetches an event by ID and returns it.
        Returns None if the event could not be fetched.
        """
        response = await bot.async_client.room_get_event(room_id, event_id)

        if isinstance(response, nio.RoomGetEventError):
            print(f"  ✘ Could not fetch event {event_id}: {response.message}")
            return None

        return response.event
