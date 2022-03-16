from adb.bootstrap.invoker import run


class Bin:
    @staticmethod
    def bootstrap_adb() -> bool:
        print('Bin bootstrap')

        run('adb.exe kill-server')
        run('adb.exe start-server')

        print('Bin current connected devices')

        output, _ = run('adb.exe devices')

        print('Bin current connected devices output:')

        for line in output.splitlines():
            print(line)

        return len(output.splitlines()) > 2
