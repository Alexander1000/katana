from cmd import Cmd
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
        server = main.Server()
        server.init()
        raise SystemExit
    else:
        print(helpText)
        raise SystemExit


class DeployerPrompt(Cmd):
    def do_q(self, args):
        print("Quitting.")
        raise SystemExit

    def emptyline(self):
        pass


prompt = DeployerPrompt()
prompt.prompt = 'deployer > '
prompt.doc_leader = 'Deployer commands'
prompt.doc_header = 'list commands'
prompt.intro = 'Interactive deployer\n for deploy on production'

projectPrompt = ''

prompt.cmdloop(
    'Welcome to deployer...\n'
    + 'Other:\n'
    + '\t [ q ] quite'
)
