import bootstrap
from adb.command.screencap import screencap


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

    @staticmethod
    def screencap_once():
        """
        执行一次截图
        :return:
        """
        screencap()

    def run_app(self):
        pass


if __name__ == '__main__':
    ADB.ready()

    ADB.screencap_once()


