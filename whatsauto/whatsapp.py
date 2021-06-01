#!/usr/bin/env python
"""This module contains whatsauto objects"""
from uiautomator2 import Device
from queue import Queue


class WhatsApp:
    def __init__(self, device: Device = None, max_task: int = 0):
        if isinstance(device, Device):
            self.device = device
        else:
            self.device = Device(device)
        self.queue: Queue = Queue(maxsize=max_task)

    def message(self, func):
        pass

    def send_message(self, chat, text: str):
        pass
