import pathlib
import tomllib
from collections.abc import Mapping
from dataclasses import dataclass

__all__ = (
    'Config',
    'load_config_from_file_path',
    'parse_config',
)


@dataclass(frozen=True, slots=True)
class Config:
    telegram_bot_token: str


def parse_config(config: Mapping) -> Config:
    return Config(telegram_bot_token=config['telegram_bot']['token'])


def load_config_from_file_path(file_path: pathlib.Path) -> Config:
    config_text = file_path.read_text(encoding='utf-8')
    config = tomllib.loads(config_text)
    return parse_config(config)
