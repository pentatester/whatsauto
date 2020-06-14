from .base import BaseClient
from .conversations import ConversationMethods
from dataclasses import dataclass


@dataclass
class Chat:
    contact: str
    message: str
    time: str
    counter: int
    group: bool


class ChatMethods(BaseClient):
    def open_chat(self, contact):
        contact = str(contact)
        self.home()
        self.device(resourceId="com.whatsapp:id/menuitem_search").click()
        self.device(resourceId="com.whatsapp:id/search_src_text").click()
        self.device.send_keys(contact, clear=True)
        self.device(
            resourceId="com.whatsapp:id/conversations_row_contact_name", text=contact).click()
        return

    def open_archived(self):
        if self.home():
            pass
        if self.device(resourceId="com.whatsapp:id/conversations_row_tip_tv").exists:
            self.device(
                resourceId="com.whatsapp:id/conversations_row_tip_tv").click()
            return True
        return False

    def send_text(self, contact, message):
        self.open_chat(contact)
        if self.device(resourceId="com.whatsapp:id/entry").exists:
            self.device.send_keys(message, clear=True)
            self.device.send_action("send")
            return True
        return False
