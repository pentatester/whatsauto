from .base import BaseUi
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


class CallUi(BaseUi):
    def remove(self, call: Call):
        pass

    def block(self, call: Call):
        pass
