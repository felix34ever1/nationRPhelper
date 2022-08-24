""" Ability Class - subclass of Asset

"""

from asset import Asset


class Ability(Asset):

    def __init__(self,name: str,stattype: str,description: str, duration: int, location: object):
        self.duration = duration
        self.location = location # The nation object this will effect in
        super().__init__(name, "ability", stattype, description)

    def set_location(self, location: object):
        self.location = location

    def set_duration(self, duration: int):
        self.duration = duration

    def get_duration(self) -> int:
        return(self.duration)

    def tick(self, phase = 1):
        if phase == 3:
            self.duration -= 1