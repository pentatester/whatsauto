#!/usr/bin/env python
"""Base class for whatsauto objects"""
from uiautomator2 import Device


class WhatsAutoObject:
    device: Device = None
