import cli.main as main_cli
from server import main
import sys
import os


def help() -> str:
    help_text = 'Usage: katana [command] -c [config path]\n'
    help_text += 'Commands:\n'
    help_text += '\t<none> - run interactive cli\n'
    help_text += '\tstart - run http server\n'
    help_text += '\ttests - run unit-tests\n'
    return help_text


config_path = ''

if len(sys.argv) == 1:
    print(help())
    raise SystemExit

if sys.argv[1] == 'tests':
    for root, subdir, files in os.walk(os.getcwd() + "/tests"):
        if len(files) > 0:
            os.system("python3 -m unittest discover --pattern \"*_test.py\" {}".format(root))
    raise SystemExit

if sys.argv[1] == '-c':
    if len(sys.argv) > 2:
        config_path = sys.argv[2]
    else:
        print(help())
        raise SystemExit
else:
    if sys.argv[1] == 'start':
        if len(sys.argv) >= 4:
            if sys.argv[2] == '-c':
                config_path = sys.argv[3]
            else:
                print(help())
                raise SystemExit
        else:
            print(help())
            raise SystemExit
        server = main.Server(config_path)
        server.init()
        raise SystemExit
    else:
        print(help())
        raise SystemExit

main_cli.main(config_path)
