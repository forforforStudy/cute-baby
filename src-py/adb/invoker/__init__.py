import subprocess
import bin

from adb.bootstrap.device import ADBDevice


def run(command: str, device: ADBDevice = None):
    # 整合指令
    run_cmd = ['adb.exe']
    if device is not None:
        run_cmd.append('-s {}'.format(device.device_id))
    run_cmd.append(command)

    return subprocess.Popen(' '.join(run_cmd),
                            shell=True,
                            cwd=bin.adb_path,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE).communicate()
