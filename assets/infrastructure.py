""" Infrastrucure Class - Subclass of Asset

"""
from asset import Asset


class Infrastructure(Asset):

    def __init__(self, name: str,stattype: str,description: str, health: int, location: object):
        super().__init__(name, stattype, description)
        self.health = health
        self.location = location
