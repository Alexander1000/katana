from cmd import Cmd
import config.loader as loader


class DeployerPrompt(Cmd):
    loader: loader.Loader

    def default(self, line):
        if line.isdigit():
            number = int(line)
            if 1 <= number <= len(self.loader.get_projects()):
                project = self.loader.get_projects()[number-1]
                print("Selected project '{}'\n".format(project.name))
            else:
                print("Invalid project number")
            return

        super().default(line)

    def do_q(self, args):
        print("Quitting.")
        raise SystemExit

    def emptyline(self):
        pass


def main(config_path: str):
    prompt = DeployerPrompt()
    prompt.loader = loader.Loader(config_path)
    prompt.prompt = 'katana > '
    prompt.doc_leader = 'Katana commands'
    prompt.doc_header = 'list commands'
    prompt.intro = 'Interactive commands'

    projectPrompt = ''

    i = 1
    for project in prompt.loader.get_projects():
        projectPrompt += "\t[{}] {}\n".format(i, project.name)
        i = i + 1

    prompt.cmdloop(
        'Welcome to katana...\n'
        + 'Select project:\n'
        + projectPrompt
        + 'Other:\n'
        + '\t [ q ] quite'
    )
