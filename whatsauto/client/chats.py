from .base import BaseClient
from dataclasses import dataclass


@dataclass
class Chat:
    contact: str
    message: str
    time: str
    counter: int
    group: bool


class ChatMethods(BaseClient):
    pass
