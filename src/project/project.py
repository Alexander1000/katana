import project.build as build


class Project:
    name: str
    host: str

    builds: list

    workDir: str

    def __init__(self, name: str, host: str):
        self.name = name
        self.host = host
        self.builds = []

    def add_build(self, build: build.Build):
        self.builds.append(build)

    def get_builds(self) -> list:
        return self.builds

    def set_work_dir(self, work_dir: str):
        self.workDir = work_dir


def parse(work_dir: str, data: dict) -> Project:
    assert 'name' in data.keys(), "Expected field 'name' exists"
    assert 'host' in data.keys(), "Expected field 'host' exists"

    project = Project(name=data.get("name"), host=data.get("host"))
    project.set_work_dir(work_dir)

    if 'builds' in data.keys():
        builds_list_raw = data.get('builds')
        assert type(builds_list_raw).__name__ == 'list',\
            "Expected type 'list' of 'builds', but '%s' given" % type(builds_list_raw).__name__

        for build_raw in builds_list_raw:
            assert type(build_raw).__name__ == 'dict',\
                "Expected type 'dict' of 'builds' element, but '%s' given" % type(build_raw).__name__

            project.add_build(build.parse(build_raw))

    return project
