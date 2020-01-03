from cmd import Cmd
import config.loader as loader


class DeployerPrompt(Cmd):
    loader: loader.Loader

    def do_q(self, args):
        print("Quitting.")
        raise SystemExit

    def emptyline(self):
        pass


def main(config_path: str):
    l = loader.Loader(config_path)

    prompt = DeployerPrompt()
    prompt.loader = l
    prompt.prompt = 'katana > '
    prompt.doc_leader = 'Katana commands'
    prompt.doc_header = 'list commands'
    prompt.intro = 'Interactive commands'

    projectPrompt = ''

    i = 1
    for project in l.get_projects():
        projectPrompt += "\t[{}] {}\n".format(i, project.name)
        i = i + 1

    prompt.cmdloop(
        'Welcome to katana...\n'
        + 'Select project:\n'
        + projectPrompt
        + 'Other:\n'
        + '\t [ q ] quite'
    )
