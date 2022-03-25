import uuid
import os.path as path

from dataclasses import dataclass

from adb import ADBDevice
from adb.invoker import run


@dataclass
class ScreencapResult:
    file_name: str = ''
    abs_file_name: str = ''


def screencap(target_device: ADBDevice = None) -> ScreencapResult:
    """
    直接adb截图操作, 返回生成的图片路径
    :return:
    """
    print('command.screencap - 执行截图操作')

    file_name = '{}.png'.format(uuid.uuid4())
    relative_screencap_folder = '../../resources/screencaps'

    cmd = 'exec-out screencap -p > {}/{}'.format(relative_screencap_folder, file_name)

    run(cmd, target_device)

    abs_file_name = path.join(path.abspath(relative_screencap_folder), file_name)

    print('command.screencap - 截图生成: {}'.format(abs_file_name))

    return ScreencapResult(file_name=file_name, abs_file_name=abs_file_name)
