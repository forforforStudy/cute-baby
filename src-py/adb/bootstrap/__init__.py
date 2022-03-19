from typing import List

from adb.invoker import run
from adb.bootstrap.device import ADBDevice


class Bin:
    def __init__(self):
        pass

    @staticmethod
    def bootstrap_adb() -> List[ADBDevice]:
        print('Bin bootstrap')

        run('kill-server')
        run('start-server')

        print('Bin current connected devices')

        output, _ = run('devices')

        print('Bin current connected devices output:')
        device_id_str = [bytes.decode(line).split('\t')[0] for line in output.splitlines()[1:-1]]

        for index, out_device_id in enumerate(device_id_str):
            print('{}: {}'.format(index, out_device_id))

        return list(map(lambda device_id: ADBDevice(device_id), device_id_str))
