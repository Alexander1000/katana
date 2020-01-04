import project.build as build


class Project:
    name: str
    host: str

    builds: []

    def __init__(self, name: str, host: str):
        self.name = name
        self.host = host

    def add_build(self, build: build.Build):
        self.builds.append(build)
