from uiautomator2 import Device, Session


class BaseClient:
    def __init__(self, device=None):
        if isinstance(device, Device):
            self.device = device
        else:
            self.device: Device = Device()
        if isinstance(device, Session):
            self.session = device
        else:
            self.session: Session = Session()

    def home(self):
        if self.device(resourceId="com.whatsapp:id/toolbar").exists:
            return
        else:
            self.device.press('back')
            return self.home()
