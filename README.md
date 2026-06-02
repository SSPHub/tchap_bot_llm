# Bot tchap - features

Will load all `register` functions listed in all .py files of the listeners folder.
To deactivate a module, just update the name from `def register` to `def no_register` for example.

# Repo structure
```
tchap_bot_test/
│
├── main.py                  # Point d'entrée : appelle src.run("!")
├── pyproject.toml           # Dépendances (matrix-nio[e2e], openai, simplematrixbotlib)
├── uv.lock                  # Verrouillage des versions (uv)
├── .python-version          # Version Python du projet (3.13)
├── README.md                # Doc d'usage et de déploiement
├── LICENSE
│
├── src/                     # Le code du bot, organisé en package
│   ├── __init__.py          # run() : charge la config, crée le bot, branche les listeners
│   │
│   ├── config/              # ── Couche configuration ──
│   │   ├── __init__.py
│   │   └── settings.py      # Creds, BotConfig, Settings + lecture des variables d'env
│   │
│   ├── core/                # ── Couche cœur ──
│   │   ├── __init__.py
│   │   └── bot.py           # create_bot() : instancie le bot simplematrixbotlib
│   │
│   └── listeners/           # ── Couche fonctionnalités (une par fichier) ──
│       ├── __init__.py      # load_all() : charge auto. tous les modules avec register()
│       ├── echo.py          # coucou → renvoie l'heure (la fonctionnalité de test)
│       ├── llm_tchat.py     # !llm → interroge le LLM + reconstitue l'historique
│       └── reaction.py      # réaction à un mot-clé (la fonctionnalité "mystère")
│
├── bash/                    # Scripts d'exploration de l'API Matrix (phase de découverte)
│   ├── get_token.sh         # Récupère un jeton d'accès
│   ├── get_event.sh         # Lit un événement par son ID
│   ├── post_msg.sh          # Poste un message
│   └── logout.sh            # Se déconnecte
│
├── dockerfile               # Image Docker (avec build de libolm pour le chiffrement)
├── .dockerignore
│
├── k8s/
│   └── deployment.yaml      # Déploiement Kubernetes : secrets + volume persistant
│
└── .github/
    ├── workflows/
    │   └── deploy.yaml       # GitHub Action : build + push de l'image à chaque commit
    └── dependabot.yml        # Mises à jour automatiques des actions GitHub
```
 
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
