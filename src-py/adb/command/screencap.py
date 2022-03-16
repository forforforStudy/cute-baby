import uuid
from adb.bootstrap import run


def screencap() -> str:
    """
    直接adb截图操作, 返回生成的图片路径
    :return:
    """
    file_name = '{}.png'.format(uuid.uuid4())
    run('adb.exe exec-out screencap -p > ../../resources/screencaps/{}'.format(file_name))

    return file_name
