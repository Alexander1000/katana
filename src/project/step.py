allowed_actions = [
    'run-custom-shell'
]


class Step:
    name: str
    description: str
    action: str
    command: str

    def __init__(self, name: str, description: str, action: str):
        self.name = name
        self.description = description
        self.action = action

    def set_command(self, command: str):
        self.command = command

    def run(self, ctx: dict) -> bool:
        return True


def parse(data: dict) -> Step:
    assert 'name' in data.keys(), "Expected field 'name' exists"
    assert 'description' in data.keys(), "Expected field 'description' exists"
    assert 'action' in data.keys(), "Expected field 'action' exists"
    action = data.get('action')
    if action not in allowed_actions:
        raise AssertionError

    step = Step(data.get('name'), data.get('description'), action)

    if action == 'run-custom-shell':
        assert 'command' in data.keys(), "Expected field 'command' exists"
        step.set_command(data.get('command'))

    return step

