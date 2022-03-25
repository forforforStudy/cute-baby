from adb import ADB

if __name__ == '__main__':
    adb_ins = ADB.ready().use_first_device()

    adb_ins.screencap_once()
