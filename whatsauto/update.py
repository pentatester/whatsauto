#!/usr/bin/env python
"""Class for representing an update in whatsapp"""

from dataclasses import dataclass
from typing import Optional
from whatsauto import User, Message, Group


@dataclass
class Update(object):
    user: Optional[User] = None
    group: Optional[Group] = None
    message: Optional[Message] = None
