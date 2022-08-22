"""ExampleAbility class - subclass of ability

"""
from assets.ability import Ability

class ExampleAbility(Ability):

    def __init__(self, location: object = None, duration: int = 3):
        super().__init__("Example ability", "wealth", "Proof of concept", duration, location)

    def tick(self):
        pass