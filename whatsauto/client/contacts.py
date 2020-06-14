from .base import BaseClient
from dataclasses import dataclass


class Contact:
    name: str
    number: [str]
    mute: bool
    groups_in_common: list

    def __str__(self):
        if self.name:
            return self.name
        return self.number


class ContactMethods(BaseClient):
    pass
