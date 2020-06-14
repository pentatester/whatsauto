from uiautomator2 import Device, Session


class BaseClient:
    def __init__(self):
        self.device: Device = None
        self.session: Session = None
