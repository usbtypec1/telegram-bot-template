import pathlib
import tomllib
from typing import Final, Self

from pydantic import BaseModel


ROOT_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parent.parent.parent
CONFIG_FILE_PATH: Final[pathlib.Path] = ROOT_PATH / "config.toml"


class TelegramBotSettings(BaseModel):
    skip_updates: bool
    token: str


class Settings(BaseModel):
    telegram_bot: TelegramBotSettings

    @classmethod
    def from_toml(cls) -> Self:
        config_toml = CONFIG_FILE_PATH.read_text(encoding="utf-8")
        config = tomllib.loads(config_toml)
        return cls.model_validate(config)
