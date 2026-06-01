# Bot tchap - features

Will load all `register` functions listed in all .py files of the listeners folder.
To deactivate a module, just update the name from `def register` to `def no_register` for example.

# Docker

Every push to the repo triggers the release of a new docker image

## Echo

replies with time when message starts with coucou

## Url react - disabled for now

When you send an url, the bot replies with a tick mark.
The script is more an example and disabled for now.

## Send request to LLM lab

send your message to LLM when starting with `!llm`
If you reply to the answer, (still starting with !llm), it will remember past exchanges to the same messages.

# How to

## Technical requirements

- username of Tchap account as a secret stored under "TCHAP_BOT_SSPHUB_MATRIX_ID"
- password of your Tchap account as a secret stored under "TCHAP_BOT_SSPHUB_PWD"
- "LLM_LAB_API_KEY" : api key to LLM.lab

**Note - config set in the code:**

- homeserver of Tchap to "https://matrix.agent.finances.tchap.gouv.fr",
- url of llmlab : "https://llm.lab.sspcloud.fr/api"

## run it locally

just run `uv run main.py`.

## add a function

Add a listener script in the src/listeners folder

## Deploy it

- have Kubernetes admin role
- have as env var :
  - DOCKERHUB_USERNAME : DOCKER HUB account to pull the image from
  - SSP_USERNAME : your username from SSPCloud account
- run it with

```{bash}
sed "s/\${DOCKERHUB_USERNAME}/$DOCKERHUB_USERNAME/g; s/\${SSP_USERNAME}/$SSP_USERNAME/g" k8s/deployment.yaml | kubectl apply -f -
```
