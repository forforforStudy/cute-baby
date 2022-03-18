from typing import List

import bootstrap
from adb.command.screencap import screencap, ScreencapResult


class ADB:
    @staticmethod
    def ready():
        """
        准备好ADB的工作
        :return:
        """
        result = bootstrap.Bin.bootstrap_adb()

        if result:
            print('adb had bootstrap and devices has connected')
        else:
            print('adb had bootstrap and no devices connected')

        return ADB()

    def __init__(self):
        self.screencaps: List[ScreencapResult] = []

    def screencap_once(self):
        """
        执行一次截图, 并推到数组第一个
        :return:
        """

        self.screencaps.insert(0, screencap())
        return self

    def latest_screencap(self):
        return self.screencaps[0]

    def run_app(self):
        pass


if __name__ == '__main__':
    adb_ins = ADB.ready()

    latest_screencap = adb_ins.screencap_once().latest_screencap()

    print('file_name: {}, abs_file_name: {}'.format(latest_screencap.file_name, latest_screencap.abs_file_name))
