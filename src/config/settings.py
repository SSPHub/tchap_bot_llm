import os
from dataclasses import dataclass

DATA_DIR = "session"


@dataclass(frozen=True)
class Creds:
    homeserver: str
    username: str
    password: str
    session_stored_file: str


@dataclass(frozen=True)
class BotConfig:
    emoji_verify: bool
    ignore_unverified_devices: bool
    encryption_enabled: bool
    store_path: str


@dataclass(frozen=True)
class Settings:
    prefix: str
    room_ids: list[str]


def load_all(*args):
    return load_creds(), load_config(), load_settings(*args)


def load_creds() -> Creds:
    return Creds(
        homeserver="https://matrix.agent.finances.tchap.gouv.fr",
        username=os.environ["TCHAP_BOT_SSPHUB_MATRIX_ID"],
        password=os.environ["TCHAP_BOT_SSPHUB_PWD"],
        session_stored_file=os.path.join(DATA_DIR, "session.txt"),
    )


def load_config() -> BotConfig:
    return BotConfig(
        emoji_verify=True,
        ignore_unverified_devices=True,
        encryption_enabled=True,
        store_path=os.path.join(DATA_DIR, "store"),
    )


def load_settings(prefix: str = "!") -> Settings:
    return Settings(
        prefix=prefix,
        room_ids=[
            value
            for key, value in os.environ.items()
            if key.startswith("TCHAP_ROOM_ID")
        ],
    )
