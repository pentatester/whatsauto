from .base import BaseClient
from dataclasses import dataclass
from collections import namedtuple

Reply = namedtuple('Reply', ['message', 'sticker'])


@dataclass
class BaseMessage:
    time: str
    date: str
    reply: Reply


@dataclass
class StatusMessage(BaseMessage):
    text: str


@dataclass
class Message(BaseMessage):
    text: str
    reply: Reply


@dataclass
class Sticker(BaseMessage):
    name: str
    creator: str


class ConversationMethods(BaseClient):
    @property
    def in_conversation(self):
        return self.device(resourceId="com.whatsapp:id/conversation_contact").exists and self.device.xpath('//*[@resource-id="com.whatsapp:id/back"]/android.widget.FrameLayout[1]').exists

    def search(self, message):
        pass

    def get_messages(self):
        if self.in_conversation:
            pass
        if self.device(resourceId="android:id/list").exists:
            pass
