from .base import BaseClient
from collections import namedtuple
from dataclasses import dataclass


@dataclass
class BaseCall:
    incoming: bool
    outcoming: bool
    time: str


@dataclass
class CallInfo(BaseCall):
    data: str


@dataclass
class Call(BaseCall):
    contact: str
    retry: int


class CallMethods(BaseClient):
    def remove(self, call: Call):
        pass

    def block(self, call: Call):
        pass
