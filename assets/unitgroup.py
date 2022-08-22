''' UnitGroup Class - Subclass of Asset

'''
from asset import Asset


class UnitGroup(Asset):

    def __init__(self, name: str, stattype: str, description: str, health: int, composition: list = []):
        super().__init__(name, "unitgroup", stattype, description)
        self.health = health
        self.composition = composition

    def get_health(self) -> int:
        return self.health

    def get_composition(self) -> list:
        return self.composition