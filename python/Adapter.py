class OldDevice(object):
    def info(self):
        print("Type: Made in China")
        print("Tension: 220V")
        print("Tension type: alternating current")

class ChineseSocket(object):
    def __init__(self, device):
        self.device = device

    def render(self):
        self.device.info()

class NewDevice(object):
    def type_info(self):
        print("Type: Made in China")

    def tension_info(self):
        print("Tension: 220V")

    def tension_type_info(self):
        print("Tension type: alternating current")

class Adapter(object):
    def __init__(self, device):
        self.device = device

    def info(self):
        self.device.type_info()
        self.device.tension_info()
        self.device.tension_type_info()

oldd = OldDevice()
socket = ChineseSocket(oldd)
socket.render()
print("===adapt new device===")
newd = NewDevice()
adpt = Adapter(newd)
socket = ChineseSocket(adpt)
socket.render()
