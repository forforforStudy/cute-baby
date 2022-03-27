import os
import pathlib

from colorama import init, Fore
from resources.screencap_thread import stop_screencap, start_screencap_thread

init()


class ScreencapsManager:
    screencaps_dir = os.path.abspath('./screencaps')

    @staticmethod
    def get_screencap_files():
        """
        获取截屏图片文件列表, 并根据创建时间倒序排序
        :return:
        """
        screencap_abs_files = [
            os.path.join(ScreencapsManager.screencaps_dir, file_name)
            for file_name in filter(lambda file_name: pathlib.Path(file_name).suffix == '.png',
                                    os.listdir(ScreencapsManager.screencaps_dir))
        ]

        screencap_abs_files.sort(key=lambda file_path: -os.path.getctime(file_path))

        return screencap_abs_files

    @staticmethod
    def latest(latest_size: int = 1):
        """
        获取最新的几条截屏文件目录
        :param latest_size:
        :return:
        """
        return ScreencapsManager.get_screencap_files()[0:latest_size]

    def __init__(self, pool_size: int):
        self.pool_size = pool_size
        self.is_screencap_doing = False

    def remove_of_oversize(self):
        """
        如果截屏文件数量超过了 pool_size 则需要将最旧的文件删除
        :return:
        """
        screencap_files = ScreencapsManager.get_screencap_files()
        if len(screencap_files) > self.pool_size:
            print(Fore.GREEN + '截屏文件过多超过: {}, 需要删减'.format(self.pool_size))
            for oversize_file in screencap_files[self.pool_size:]:
                os.remove(oversize_file)

    def start_screen_shot(self):
        print(Fore.GREEN + '开始定时截屏执行')
        self.is_screencap_doing = True
        start_screencap_thread()

    def stop_screen_shot(self):
        print(Fore.YELLOW + '停止定时截屏执行')

        self.is_screencap_doing = False
        stop_screencap()


screencaps_manager = ScreencapsManager(pool_size=500)

