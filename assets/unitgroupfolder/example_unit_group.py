'''ExampleUnitGroup Class - Subclass of UnitGroup

'''
from assets.unitgroup import UnitGroup


class ExampleUnitGroup(UnitGroup):

    def __init__(self, health: int = 10, composition: list = []):
        super().__init__("example unit group", "force", "Example unit group", health, composition)
