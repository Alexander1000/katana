import yaml
import os
import project.project as proj
from pathlib import Path


class Loader:
    listen: str
    port: int

    projects: list

    workDir: str

    def __init__(self, config_file: str):
        self.projects = []

        file = open(config_file, "r")
        configs = yaml.load(file, Loader=yaml.FullLoader)
        file.close()

        assert 'server' in configs.keys(), "Expected field 'server' exists"
        srv_conf = configs.get('server')
        assert type(srv_conf).__name__ == 'dict', "Expected type 'dict' of 'server', but '%s' given" % type(srv_conf).__name__
        assert 'listen' in srv_conf.keys(), "Expected field 'listen' exists in 'server'"
        assert 'port' in srv_conf.keys(), "Expected field 'port' exists in 'server'"

        self.listen = srv_conf.get('listen')
        self.port = srv_conf.get('port')

        if 'workDir' in configs.keys():
            self.workDir = configs.get('workDir')
            if self.workDir[0:2] == '~/':
                self.workDir = "{}/{}".format(str(Path.home()), self.workDir[2:])

            if not os.path.exists(self.workDir):
                os.makedirs(self.workDir, 0o777, False)

        assert 'projectsDir' in configs.keys(), "Expected field 'projectsDir' exists"
        projects_dir = configs.get('projectsDir')
        assert type(projects_dir).__name__ == 'str'

        for f in os.listdir(projects_dir):
            filename, file_ext = os.path.splitext(f)
            if file_ext != '.yml':
                continue

            proj_file = open("{}/{}".format(projects_dir, f), "r")
            proj_configs = yaml.load(proj_file, Loader=yaml.FullLoader)
            proj_file.close()

            p = proj.parse(self.workDir, proj_configs)
            self.projects.append(p)

    def get_projects(self):
        return self.projects

    def get_listen(self) -> str:
        return self.listen

    def get_port(self) -> int:
        return self.port
