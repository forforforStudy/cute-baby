from typing import List, Tuple

import bootstrap

from adb.bootstrap import ADBDevice, device
from adb.command.list_package import list_package
from adb.command.screencap import screencap, ScreencapResult
from adb.invoker import run


class ADB:
    @staticmethod
    def ready():
        """
        准备好ADB的工作
        :return:
        """
        result = bootstrap.Bin.bootstrap_adb()

        if result and len(result) > 0:
            print('adb had bootstrap and devices has connected')
            return ADB(result)
        else:
            print('adb had bootstrap and no devices connected')
            raise RuntimeError('没有Device设备链接, ADB无法执行.')

    def __init__(self, current_devices: List[ADBDevice]):
        self.screencaps: List[ScreencapResult] = []
        self.current_devices = current_devices

    def use_first_device(self):
        """
        获取首个device设备实例的ADB运行器
        :return:
        """
        only_first_devices = self.current_devices[:1]
        return ADB(only_first_devices)

    def screencap_once(self):
        """
        执行一次截图, 并推到数组第一个
        :return:
        """

        for device in self.current_devices:
            self.screencaps.insert(0, screencap(device))

        return self

    def get_package_of_list(self) -> List[Tuple[ADBDevice, List[str]]]:
        """
        获取包名列表
        :return:
        """

        return [(device, list_package(device)) for device in self.current_devices]

    def latest_screencap(self):
        return self.screencaps[0]


if __name__ == '__main__':
    adb_ins = ADB.ready().use_first_device()

    for list_result in adb_ins.get_package_of_list():
        (device, package_list) = list_result
        print('device_id: {}'.format(device.device_id))
        for package_name in package_list:
            print('\t{}'.format(package_name))
