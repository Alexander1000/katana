from cmd import Cmd
import project.project as project


class ProjectMenu(Cmd):
    proj: project.Project

    def do_q(self, args):
        print("Quitting.")
        raise SystemExit

    def emptyline(self):
        pass


def run(proj: project.Project):
    prompt = ProjectMenu()
    prompt.proj = proj
    prompt.prompt = 'katana [{}] >'.format(proj.name)
    prompt.doc_leader = 'Katana commands'
    prompt.doc_header = 'list commands'
    prompt.intro = 'Interactive commands'
    prompt.cmdloop('Welcome')
