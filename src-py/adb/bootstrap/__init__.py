import bin
import subprocess


class Bin:
    @staticmethod
    def bootstrap_adb() -> bool:
        print('Bin bootstrap')
        subprocess.Popen('adb.exe kill-server',
                         shell=True,
                         cwd=bin.adb_path).communicate()

        subprocess.Popen('adb.exe start-server',
                         shell=True,
                         cwd=bin.adb_path).communicate()

        print('Bin current connected devices')
        output, _ = subprocess.Popen('adb.exe devices',
                                     shell=True,
                                     cwd=bin.adb_path,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE).communicate()

        print('Bin current connected devices output:')

        for line in output.splitlines():
            print(line)

        return len(output.splitlines()) > 2
