import threading
import time

stop_screencap = True


def stop_screencap_threads():
    global stop_screencap

    stop_screencap = False


def start_screencap_thread():
    def running_target():
        from adb import ADB
        global stop_screencap

        while True and stop_screencap is False:
            adb_ins = ADB.ready().use_first_device()
            adb_ins.screencap_once()
            time.sleep(2)

    global stop_screencap
    stop_screencap = False
    current_thread = threading.Thread(target=running_target)
    current_thread.start()
