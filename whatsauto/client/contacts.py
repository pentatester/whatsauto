from .base import BaseUi
from dataclasses import dataclass


class Contact:
    name: str
    number: [str]
    mute: bool
    groups_in_common: list


class ContactUi(BaseUi):
    pass
