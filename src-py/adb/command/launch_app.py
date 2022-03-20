from adb.command.list_package import list_package
from adb.bootstrap import ADBDevice


def launch_app(keyword: str, device: ADBDevice = None) -> str:
    list_results = list_package(device)
    target_package_name = next(package_name for package_name in list_results if keyword in package_name)

    if target_package_name is None:
        raise RuntimeError('未找到关键词为: {} 的app包'.format(keyword))
    else:
        return target_package_name
