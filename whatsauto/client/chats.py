from .base import BaseClient
from .conversations import ConversationMethods
from dataclasses import dataclass

_CHAT_TAB = '//*[@resource-id="com.whatsapp:id/tabs"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]'
_SEARCH_BUTTON = "com.whatsapp:id/menuitem_search"
_SEARCH_INPUT = "com.whatsapp:id/search_src_text"

_CONTACT_CONTAINER = "com.whatsapp:id/contact_row_container"
_CONTACT_NAME = "com.whatsapp:id/conversations_row_contact_name"

_ARCHIVED = "com.whatsapp:id/conversations_row_tip_tv"


@dataclass
class Chat:
    contact: str
    message: str
    time: str
    counter: int
    group: bool
    muted: bool

    @staticmethod
    def from_contact_row_container(widget):
        return widget


class ChatMethods(BaseClient):

    def open_tab_chat(self):
        self.device.xpath(_CHAT_TAB)

    def open_chat(self, contact):
        contact = str(contact)
        self.home()
        self.device(resourceId=_SEARCH_BUTTON).click()
        self.device(resourceId=_SEARCH_INPUT).click()
        self.device.send_keys(contact, clear=True)
        if self.device(
                resourceId=_CONTACT_NAME, text=contact).exists:
            self.device(
                resourceId=_CONTACT_NAME, text=contact).click()
            return True
        return False

    def open_archived(self):
        if self.home():
            pass
        if self.device(resourceId=_ARCHIVED).exists:
            self.device(
                resourceId=_ARCHIVED).click()
            return True
        return False
