"""ExampleInfrastrucure class - subclass of Infrastructure

"""

from assets.infrastructure import Infrastructure


class ExampleInfrastructure(Infrastructure):

    def __init__(self, location: object = None, health: int = 5):
        super().__init__("Example infrastructure", "wealth", "Blah blah blah", health, location)