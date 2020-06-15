from .base import BaseClient
from dataclasses import dataclass
from collections import namedtuple

Reply = namedtuple('Reply', ['message', 'sticker'])

_MESSAGE_LIST = "android:id/list"
_TEXT_INPUT = "com.whatsapp:id/entry"
_CONTACT_NAME = "com.whatsapp:id/conversation_contact_name"
_CONTACT_STATUS = "com.whatsapp:id/conversation_contact_status"  # text = online / time
_BACK_BUTTON = "com.whatsapp:id/back"

_EMOJI_BUTTON = "com.whatsapp:id/emoji_picker_btn"
_CAMERA_BUTTON = "com.whatsapp:id/camera_btn"

_ATTACH_BUTTON = "com.whatsapp:id/input_attach_button"
# | |
# V V
_PICK_DOCUMENT = "com.whatsapp:id/pickfiletype_document_holder"
_PICK_CAMERA = "com.whatsapp:id/pickfiletype_camera_holder"
_PICK_GALLERY = "com.whatsapp:id/pickfiletype_gallery_holder"
_PICK_AUDIO = "com.whatsapp:id/pickfiletype_audio_holder"
_PICK_LOCATION = "com.whatsapp:id/pickfiletype_location_holder"
_PICK_CONTACT = "com.whatsapp:id/pickfiletype_contact_holder"


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
        return self.device(resourceId=_CONTACT_NAME).exists and self.device.xpath(_CONTACT_STATUS).exists

    def search(self, message):
        pass

    def get_messages(self):
        if self.in_conversation:
            pass
        if self.device(resourceId="android:id/list").exists:
            pass

    def send_text(self, message):
        if self.device(resourceId=_TEXT_INPUT).exists:
            self.device.send_keys(message, clear=True)
            self.device.send_action("send")
            return True
        return False
