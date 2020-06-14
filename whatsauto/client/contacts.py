from .base import BaseClient
from dataclasses import dataclass


class Contact:
    name: str
    number: [str]
    mute: bool
    groups_in_common: list


class ContactMethods(BaseClient):
    pass
