import project.step as step


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
