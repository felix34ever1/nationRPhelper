""" Infrastrucure Class - Subclass of Asset

"""
from asset import Asset


class Infrastructure(Asset):

    def __init__(self, name: str,stattype: str,description: str, health: int, location: object):
        super().__init__(name, "infrastructure", stattype, description)
        self.health = health
        self.location = location

    def set_location(self, location: object):
        self.location = location

    def set_health(self, health: int):
        self.health = health

    def get_location(self) -> object:
        return self.location

    def get_health(self) -> int:
        return self.health