from adb.bootstrap.device import ADBDevice
from adb.invoker import run


def tap(x: int, y: int, target_device: ADBDevice):
    print('command.tap - 执行手势点击')
    run('shell input tab {} {}'.format(x, y), target_device)
