from flask import jsonify

from micro_web.app import app
from micro_web.utils import route_wrap_01_version
from resources.screencaps_manager import screencaps_manager


@app.route(route_wrap_01_version('screencaps'), methods=['GET'])
def get_screencap_pager():
    """
    获取截屏信息
    :return:
    """
    screencap_files = screencaps_manager.get_screencap_files(with_abs_dir=False)

    return jsonify({'items': screencap_files, 'total': len(screencap_files)})


@app.route(route_wrap_01_version('screencaps/start'), methods=['POST'])
def start_screencaps():
    """
    控制开始执行定时截屏任务
    :return:
    """
    screencaps_manager.start_screen_shot()


@app.route(route_wrap_01_version('screencaps/stop'), methods=['POST'])
def stop_screencaps():
    """
    停止定时截屏任务
    :return:
    """
    screencaps_manager.stop_screen_shot()
