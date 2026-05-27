import importlib
import pkgutil
from pathlib import Path

import simplematrixbotlib as botlib


def load_all(bot: botlib.Bot, prefix: str) -> None:
    package_dir = Path(__file__).parent
    for _, module_name, _ in pkgutil.iter_modules([str(package_dir)]):
        module = importlib.import_module(f"src.listeners.{module_name}")
        if hasattr(module, "register"):
            module.register(bot, prefix)
            print(f"  ✔ Loaded listener: {module_name}")
