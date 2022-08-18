""" Asset class

Used as a parent class for the basic data about assets,
no objects of this should therefore exist
"""


class Asset():

    def __init__(self,name: str,stattype: str,description: str):
        
            self.name = name
            self.stattype = stattype
            self.description = description