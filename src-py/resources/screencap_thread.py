import threading
import time

from adb import ADB

stop_screencap = True


def running_target():
    global stop_screencap

    while True and stop_screencap is False:
        adb_ins = ADB.ready().use_first_device()
        adb_ins.screencap_once()
        time.sleep(2)


def stop_screencap_threads():
    global stop_screencap
    stop_screencap = True


def start_screencap_thread():
    global stop_screencap
    stop_screencap = False
    current_thread = threading.Thread(target=running_target)
    current_thread.start()


def is_screencaps_thread_doing() -> bool:
    global stop_screencap

    return stop_screencap
