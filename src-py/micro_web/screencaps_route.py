from flask import request, jsonify

from micro_web.app import app
from micro_web.utils import route_wrap_01_version
from micro_web.utils.pagination import Pager

from resources.screencaps_manager import screencaps_manager


@app.route(route_wrap_01_version('screencaps'), methods=['GET'])
def get_screencap_pager():
    """
    分页获取截屏信息
    :return:
    """
    page_size = request.values.get('page_size')
    page_num = request.values.get('page_num')

    pager = Pager(page_size=int(page_size), page_num=int(page_num))

    return jsonify({'page_num': page_num, 'page_size': page_size})


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
