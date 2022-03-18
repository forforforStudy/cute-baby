import subprocess
import bin


def run(command: str):
    return subprocess.Popen(command,
                            shell=True,
                            cwd=bin.adb_path,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE).communicate()
