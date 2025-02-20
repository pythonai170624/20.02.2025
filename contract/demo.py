from abc import abstractmethod

# interface class
class ITurn_On_Off:
    @abstractmethod
    def turn_on(self):
        pass

    def turn_off(self):
        pass

# interface class
class IKitkat:
    @abstractmethod
    def run_kit_kat(self):
        pass

# interface class
class IBoom:
    @abstractmethod
    def go_boom(self):
        pass

class Electric(object, ITurn_On_Off):
    pass

class MobileDevice(Electric):
    pass

class Iphone(MobileDevice):
    pass

class Camera(Electric, IKitkat):
    pass

# android is mobile-device which has feature run kit-kat
class Android(MobileDevice, IKitkat):
    pass

class SamsungS10(Android, IBoom):
    pass

def run_kit_kat(device: IKitkat):
    device.run_kit_kat()
k = Camera()
if isinstance(k, IKitkat):
    k.run_kit_kat()