from uiautomator2 import connect, Device


class Client:
    def __init__(self, DEVICE):
        self._device: Device = connect(DEVICE)

    @property
    def device(self):
        if self._device.info['currentPackageName'] != 'com.whatsapp':
            pass
        return self._device
