from flask import jsonify

from micro_web.utils.constant import API_VERSION


def route_wrap_01_version(request_mapping: str):
    """
    flask 路由映射包裹器
    增加API_VERSION

    :param request_mapping:
    :return:
    """
    return '{}/{}'.format(API_VERSION, request_mapping)


def gen_default_success_response():
    """
    通用成功返回体
    :return:
    """
    return jsonify({'status': 'Success'})
