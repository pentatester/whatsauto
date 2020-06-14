from uiautomator2 import connect, Device, Session

from .base import BaseClient
from .calls import BaseCall, CallInfo, Call, CallMethods
from .chats import Chat, ChatMethods
from .contacts import Contact, ContactMethods
from .conversations import Reply, BaseMessage, StatusMessage, Message, Sticker, ConversationMethods


class Client(CallMethods, ChatMethods, ContactMethods, ConversationMethods):
    def __init__(self, DEVICE=None, app_name='com.whatsapp'):
        self.device: Device = Device(DEVICE)
        self.session: Session = self.device.session(
            app_name, attach=True)

    def stop(self):
        return self.session.close()
