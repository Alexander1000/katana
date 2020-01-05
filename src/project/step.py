class Step:
    name: str

    def __init__(self, name: str):
        self.name = name


def parse(data: dict) -> Step:
    assert 'name' in data.keys(), "Expected field 'name' exists"
    return Step(data.get('name'))
