from flask import request, jsonify

from micro_web.app import app
from micro_web.utils import route_wrap_01_version
from micro_web.utils.pagination import Pager


@app.route(route_wrap_01_version('screencaps'), methods=['GET'])
def get_screencap_pager():
    page_size = request.values.get('page_size')
    page_num = request.values.get('page_num')

    pager = Pager(page_size=int(page_size), page_num=int(page_num))

    return jsonify({'page_num': page_num, 'page_size': page_size})
