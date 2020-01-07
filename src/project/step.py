class Step:
    name: str
    description: str

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


def parse(data: dict) -> Step:
    assert 'name' in data.keys(), "Expected field 'name' exists"
    assert 'description' in data.keys(), "Expected field 'description' exists"
    return Step(data.get('name'), data.get('description'))
