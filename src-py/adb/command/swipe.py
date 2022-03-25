from adb.bootstrap.device import ADBDevice
from adb.invoker import run


def swipe(x: int, y: int, to_x: int, to_y: int, target_device: ADBDevice):
    run('shell input swipe {} {} {} {}'.format(x, y, to_x, to_y), target_device)
