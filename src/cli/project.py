from cmd import Cmd
import project.project as project


class ProjectMenu(Cmd):
    proj: project.Project

    def default(self, line):
        if line.isdigit():
            number = int(line)
            if 1 <= number <= len(self.proj.get_builds()):
                build = self.proj.get_builds()[number-1]
                print("Selected build '{}'\n".format(build.name))
                build.run(self.make_context())
                return
            else:
                print("Invalid build number")
            return

        super().default(line)

    def make_context(self) -> dict:
        ctx = {
            'project': self.proj
        }
        return ctx

    def do_q(self, args):
        print("Quitting.")
        raise SystemExit

    def emptyline(self):
        pass


def run(proj: project.Project):
    prompt = ProjectMenu()
    prompt.proj = proj
    prompt.prompt = 'katana [{}] > '.format(proj.name)
    prompt.doc_leader = 'Katana commands'
    prompt.doc_header = 'list commands'
    prompt.intro = 'Interactive commands'

    builds_prompt = ''

    i = 1
    for build in prompt.proj.get_builds():
        builds_prompt += "\t[{}] {}\n".format(i, build.name)
        i = i + 1

    prompt.cmdloop(
        'Project "{}" builds menu\n'.format(proj.name)
        + 'Select build:\n'
        + builds_prompt
        + 'Other:\n'
        + '\t [ q ] quite'
    )
