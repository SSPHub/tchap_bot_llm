# Bot tchap - features

## Echo

replies with time when message starts with coucou

## Url react

## Send request to LLM lab

send your message to LLM when starting with `!llm`

# How to

## Technical requirements

- username of Tchap account as a secret stored under "TCHAP_BOT_SSPHUB_MATRIX_ID"
- password of your Tchap account as a secret stored under "TCHAP_BOT_SSPHUB_PWD"
- "LLM_LAB_API_KEY" : api key to LLM.lab

**Note - config set in the code:**

- homeserver of Tchap to "https://matrix.agent.finances.tchap.gouv.fr",
- url of llmlab : "https://llm.lab.sspcloud.fr/api"

## run it

just run `uv run main.py`.

## add a function

Add a listener script in the src/listeners folder
