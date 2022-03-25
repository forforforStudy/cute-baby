import re

from adb.command.list_package import list_package
from adb.invoker import run
from adb.bootstrap import ADBDevice


def launch_app(keyword: str, device: ADBDevice = None):
    print('command.launch_app - 执行运行APP, 关键词: "{}"'.format(keyword))

    list_results = list_package(device)
    target_package_name = next(package_name for package_name in list_results if keyword in package_name)

    if target_package_name is None:
        raise RuntimeError('未找到关键词为: {} 的app包'.format(keyword))
    else:
        target_package_name = target_package_name.replace('package:', '')

        print('command.launch_app - 查找到关键词: "{}" 包名: "{}"'.format(keyword, target_package_name))
        print('command.launch_app - 准备获取包: "{}"的MainActively'.format(target_package_name))

        output, _ = run('shell dumpsys package {}'.format(target_package_name))
        for output_line in bytes.decode(output).splitlines():
            match_obj = re.search('{}\\S+'.format(target_package_name), output_line)
            if match_obj is not None:
                # 开始调用运行
                group = match_obj.group()

                run('shell am start {}'.format(group))
                print('launch_app - 成功运行App: {}'.format(group))
                return

    raise RuntimeError('未能成功执行关键词为: "{}" 的任何App'.format(keyword))