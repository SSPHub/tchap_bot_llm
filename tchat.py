import os

from openai import OpenAI

model_name = "gemma4-26b-moe"
end_point = "https://llm.lab.sspcloud.fr/api"


client = OpenAI(
    base_url=end_point,
    api_key=os.environ.get("LLM_LAB_API_KEY", ""),
)


def h_reset():
    history = []

    return history


def h_append(role, content):
    history.append({"role": role, "content": content})

    return history


def ask(question: str):
    h_append("user", question)

    response = client.chat.completions.create(
        model=model_name,
        messages=history,
    )

    answer = response.choices[0].message.content
    h_append("assistant", answer)
    return answer


while True:
    history = []
    question = input("You : ")
    if question.lower() == "quit":
        break

    print(f"Bot : {ask(question)}")
