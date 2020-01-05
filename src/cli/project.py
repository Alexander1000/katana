from cmd import Cmd


class ProjectMenu(Cmd):
    def do_q(self, args):
        print("Quitting.")
        raise SystemExit

    def emptyline(self):
        pass


def run():
    prompt = ProjectMenu()
    prompt.cmdloop("Welcome")
