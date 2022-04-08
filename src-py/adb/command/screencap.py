import uuid
import os.path as path
from PIL import Image
from dataclasses import dataclass

from resources import screencaps_manager
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
    abs_file_name = path.join(screencaps_manager.ScreencapsManager.screencaps_dir, file_name)

    print('command.screencap - 截图生成: {}'.format(abs_file_name))

    return rotate_to_horizontal(ScreencapResult(file_name=file_name, abs_file_name=abs_file_name))


def rotate_to_horizontal(screencap_result: ScreencapResult):
    """
    如果图片大小不符合横屏, 需要旋转90°
    :param screencap_result:
    :return:
    """
    screencap_image = Image.open(screencap_result.abs_file_name)
    width, height = screencap_image.size

    print('截图文件尺寸大小 width = {}, height = {}'.format(width, height))
    if width < height:
        rotated_screencap_image = screencap_image.rotate(90, expand=True)
        rotated_screencap_image.save(screencap_result.abs_file_name)

    return screencap_result
