from micro_web.app import app

import micro_web.screencaps_route


def bootstrap(port: int = 5555):
    app.run(host='127.0.0.1', port=port)
