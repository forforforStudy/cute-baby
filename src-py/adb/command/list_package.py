from adb.bootstrap import ADBDevice
from adb.invoker import run


def list_package(target_device: ADBDevice = None):
    output_string, _ = run('shell pm list package', target_device)

    return bytes.decode(output_string).split('\r\n')
