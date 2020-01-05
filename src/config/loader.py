import yaml
import os
import project.project as proj
import project.build as build
import project.step as step


class Loader:
    listen: str
    port: int

    projects: []

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

            assert 'name' in proj_configs.keys(), "Expected field 'name' exists in project file '%s'" % f
            assert 'host' in proj_configs.keys(), "Expected field 'host' exists in project file '%s'" % f

            print("Load configs for project: '%s', host: '%s'" % (proj_configs.get("name"), proj_configs.get("host")))

            project = proj.Project(name=proj_configs.get("name"), host=proj_configs.get("host"))

            self.projects.append(project)

            if 'builds' in proj_configs.keys():
                builds_list_raw = proj_configs.get('builds')
                assert type(builds_list_raw).__name__ == 'list', "Expected type 'list' of 'builds', but '%s' given" % type(builds_list_raw).__name__

                for build_raw in builds_list_raw:
                    assert type(build_raw).__name__ == 'dict', "Expected type 'dict' of 'builds' element, but '%s' given" % type(build_raw).__name__

                    assert 'name' in build_raw.keys(), "Expected field 'name' exists in 'build[]'"
                    assert 'description' in build_raw.keys(), "Expected field 'description' exists in 'build[]'"
                    assert 'steps' in build_raw.keys(), "Expected field 'steps' exists in 'build[]'"

                    b = build.Build(build_raw.get('name'), build_raw.get('description'))

                    project.add_build(b)

                    step_list_raw = build_raw.get('steps')
                    assert type(step_list_raw).__name__ == 'list', "Expected type 'list' of 'builds.steps', but '%s' given" % type(step_list_raw).__name__

                    for step_raw in step_list_raw:
                        assert type(step_raw).__name__ == 'dict', "Expected type 'dict' of element steps, but '%s' given" % type(step_raw).__name__

                        b.add_step(step.parse(step_raw))

    def get_projects(self):
        return self.projects

    def get_listen(self) -> str:
        return self.listen

    def get_port(self) -> int:
        return self.port
