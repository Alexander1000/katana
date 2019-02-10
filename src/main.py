from cmd import Cmd
import sys

if len(sys.argv) != 3:
    print('Usage: katana -c [config path]')
    raise SystemExit

if sys.argv[1] == '-c':
    config_path = sys.argv[2]
else:
    print('Invalid arguments')
    raise SystemError

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
