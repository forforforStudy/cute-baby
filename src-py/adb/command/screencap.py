import uuid
import os.path as path

from dataclasses import dataclass

from adb.invoker import run


@dataclass
class ScreencapResult:
    file_name: str = ''
    abs_file_name: str = ''


def screencap() -> ScreencapResult:
    """
    直接adb截图操作, 返回生成的图片路径
    :return:
    """
    file_name = '{}.png'.format(uuid.uuid4())
    relative_screencap_folder = '../../resources/screencaps'

    run('adb.exe exec-out screencap -p > {}/{}'.format(relative_screencap_folder, file_name))

    abs_file_name = path.join(path.abspath(relative_screencap_folder), file_name)

    return ScreencapResult(file_name=file_name, abs_file_name=abs_file_name)
