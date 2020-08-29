#!/usr/bin/env python
"""Class for representing a message"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from whatsauto import (WhatsAutoObject, User, Group, Document, Location, Photo,
                       Sticker)


@dataclass
class Message(WhatsAutoObject):
    user: Optional[User] = None
    group: Optional[Group] = None
    document: Optional[Document] = None
    location: Optional[Location] = None
    photo: Optional[Photo] = None
    sticker: Optional[Sticker] = None
    text: Optional[str] = None
    reply_to: Optional[Message] = None
    read: Optional[datetime] = None
    delivered: Optional[datetime] = None
    pending: Optional[bool] = False
    forwarded: Optional[bool] = False
