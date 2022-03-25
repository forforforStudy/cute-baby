from typing import List, Tuple

import bootstrap

from adb.bootstrap import ADBDevice, device
from adb.command.list_package import list_package
from adb.command.screencap import screencap, ScreencapResult
from adb.command.launch_app import launch_app
from adb.command.tap import tap
from adb.command.swipe import swipe
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
        """
        初始化构造函数
        :param current_devices:
        """
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

        for current_device in self.current_devices:
            self.screencaps.insert(0, screencap(current_device))

        return self

    def get_package_of_list(self) -> List[Tuple[ADBDevice, List[str]]]:
        """
        获取包名列表
        :return:
        """

        return [(current_device, list_package(current_device)) for current_device in self.current_devices]

    def launch_app(self, app_keyword: str):
        """
        打开APP程序
        :param app_keyword:
        :return:
        """
        for current_device in self.current_devices:
            launch_app(app_keyword, current_device)

    def tap(self, x: int, y: int):
        """
        模拟手势点击
        :param x:
        :param y:
        :return:
        """
        for current_device in self.current_devices:
            tap(x, y, current_device)

    def swipe(self, x: int, y: int, to_x: int, to_y: int):
        """
        模拟鼠标滑动
        :param x:
        :param y:
        :param to_x:
        :param to_y:
        :return:
        """
        for current_device in self.current_devices:
            swipe(x, y, to_x=to_x, to_y=to_y, target_device=current_device)

    def latest_screencap(self):
        return self.screencaps[0]


if __name__ == '__main__':
    adb_ins = ADB.ready().use_first_device()

    adb_ins.screencap_once()
