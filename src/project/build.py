import project.step as step
import context.context as context


class Build:
    name: str
    description: str
    steps: list

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.steps = []

    def add_step(self, step: step.Step):
        self.steps.append(step)

    def run(self, ctx: context.Context):
        print("I'm running")


def parse(data: dict) -> Build:
    assert 'name' in data.keys(), "Expected field 'name' exists"
    assert 'description' in data.keys(), "Expected field 'description' exists "
    assert 'steps' in data.keys(), "Expected field 'steps' exists"

    build = Build(data.get('name'), data.get('description'))

    step_list_raw = data.get('steps')
    assert type(step_list_raw).__name__ == 'list', "Expected type 'list' of 'build.steps', but '%s' given" % type(step_list_raw).__name__

    for step_raw in step_list_raw:
        assert type(step_raw).__name__ == 'dict', "Expected type 'dict' of element steps, but '%s' given" % type(step_raw).__name__

        build.add_step(step.parse(step_raw))

    return build
