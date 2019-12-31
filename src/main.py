from cmd import Cmd
import sys

helpText = 'Usage: katana [command] -c [config path]'

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
        # todo: run server
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
