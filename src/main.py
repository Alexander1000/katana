import cli.main as main_cli
from server import main
import sys

helpText = 'Usage: katana [command] -c [config path]'
config_path = ''

if len(sys.argv) == 1:
    print(helpText)
    raise SystemExit

if sys.argv[1] == '-c':
    if len(sys.argv) > 2:
        config_path = sys.argv[2]
    else:
        print(helpText)
        raise SystemExit
else:
    if sys.argv[1] == 'start':
        if len(sys.argv) >= 4:
            if sys.argv[2] == '-c':
                config_path = sys.argv[3]
            else:
                print(helpText)
                raise SystemExit
        else:
            print(helpText)
            raise SystemExit
        server = main.Server(config_path)
        server.init()
        raise SystemExit
    else:
        print(helpText)
        raise SystemExit

main_cli.main(config_path)
