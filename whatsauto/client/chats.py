from .base import BaseUi
from dataclasses import dataclass


@dataclass
class Chat:
    contact: str
    message: str
    time: str
    counter: int


class ChatUi(BaseUi):
    pass
