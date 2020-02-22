import project.step as step
import time
import utils.digit_to_letter as digit_to_letter
import os


class Build:
    name: str
    description: str
    steps: list

    workDir: str

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.steps = []

    def add_step(self, step: step.Step):
        self.steps.append(step)

    def run(self, ctx: dict) -> bool:
        n_time = time.time_ns()
        work_dir = self.workDir + '/' + digit_to_letter.digit_to_letter(n_time)

        os.makedirs(work_dir, 0o777, False)

        ctx['workDir'] = work_dir

        success = True

        for step in self.steps:
            result = step.run(ctx)
            if not result:
                success = False
                break

        return success

    def set_work_dir(self, work_dir: str):
        self.workDir = work_dir


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
