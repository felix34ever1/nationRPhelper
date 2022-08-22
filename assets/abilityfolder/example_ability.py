"""ExampleAbility class - subclass of ability

"""
from assets.ability import Ability

class ExampleAbility(Ability):

    def __init__(self, location: object):
        super().__init__("Example ability", "wealth", "Proof of concept", 3, location)

    def tick(self):
        pass