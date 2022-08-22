""" Ability Class - subclass of Asset

"""

from asset import Asset


class Ability(Asset):

    def __init__(self,name: str,stattype: str,description: str, duration: int, location: object):
        self.duration = duration
        self.location = location # The nation object this will effect in
        super().__init__(name, stattype, description)        

    def tick(self):
        self.duration -= 1