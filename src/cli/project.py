from cmd import Cmd
import project.project as project


class ProjectMenu(Cmd):
    def do_q(self, args):
        print("Quitting.")
        raise SystemExit

    def emptyline(self):
        pass


def run(proj: project.Project):
    prompt = ProjectMenu()
    prompt.cmdloop("Welcome {}".format(proj.name))
