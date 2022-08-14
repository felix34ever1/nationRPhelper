"""Nation Class

Used to store data about a nation including all assets it has, stats and land owned
"""


class Nation():

    def __init__(self, name, stat_wealth, stat_force, stat_political, object_economy):

        self.name = name
        self.stat_wealth = stat_wealth
        self.stat_force = stat_force
        self.stat_political = stat_political
        self.object_economy = object_economy
        self.list_assets = []
        self.list_regions = []

    def menu(self):
        
        pass

    def tick(self):

        pass