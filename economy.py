""" Economy Class

Acts as the tracker for everything to do with numbers in a nation.
"""


class Economy():

    def __init__(self, population: int, urban_population: int):

        self.raw_industrial_metals = 0
        self.raw_rare_metals = 0
        self.raw_oil = 0
        self.raw_natural_gas = 0
        self.raw_food = 0
        self.raw_production = 0

        self.intermediary_plastics = 0
        self.intermediary_electronics = 0
        self.intermediary_advanced_parts = 0

        self.finished_consumer_products = 0
        self.finished_military_products = 0
        self.finished_power = 0

        self.tracker_population = population
        self.tracker_urban_population = urban_population
        self.tracker_incoming_trade = 0      #To keep track of incoming resource value
        self.tracker_total_resource_production = 0
        self.tracker_total_resource_expenditure = 0     #Includes resources traded out of country
        self.tracker_economy_strength = 1
        self.tracker_budget = (self.tracker_total_resource_expenditure+self.tracker_total_resource_production-self.tracker_incoming_trade) * self.tracker_economy_strength * self.tracker_population

    def add_raw_industrial_metals(self,amount: int):
        self.raw_industrial_metals += amount

    def add_raw_rare_metals(self,amount: int):
        self.raw_rare_metals += amount

    def add_raw_oil(self,amount: int):
        self.raw_oil += amount

    def add_raw_natural_gas(self,amount: int):
        self.raw_natural_gas += amount

    def add_raw_food(self,amount: int):
        self.raw_food += amount

    def add_intermediary_plastics(self,amount: int):
        self.intermediary_plastics += amount

    def add_intermediary_electronics(self,amount: int):
        self.intermediary_electronics += amount

    def add_intermediary_advanced_parts(self,amount: int):
        self.intermediary_advanced_parts += amount

    def add_finished_consumer_products(self,amount: int):
        self.finished_consumer_products += amount

    def add_finished_military_products(self,amount: int):
        self.finished_military_products += amount

    def add_finished_power(self,amount: int):
        self.finished_power += amount

    def add_tracker_total_resource_production(self,amount: int):
        self.tracker_total_resource_production += amount

    def add_tracker_total_resource_consumption(self,amount: int):
        self.add_tracker_total_resource_consumption += amount

    def add_tracker_incoming_trade(self,amount: int):
        self.tracker_incoming_trade += amount

    def tick(self):
        # Called at beginning of every cycle, should be calculated before nation and assets

        self.tracker_budget = (self.tracker_total_resource_expenditure+self.tracker_total_resource_production-self.tracker_total_incoming_trade) * self.tracker_economy_strength * self.tracker_population
        
        # Reduce all resources to 0 to recalculate for next tick

        self.raw_industrial_metals = 0
        self.raw_rare_metals = 0
        self.raw_oil = 0
        self.raw_natural_gas = 0
        self.raw_food = 0
        self.raw_production = 0

        self.intermediary_plastics = 0
        self.intermediary_electronics = 0
        self.intermediary_advanced_parts = 0

        self.finished_consumer_products = 0
        self.finished_military_products = 0
        self.finished_power = 0

        self.tracker_incoming_trade = 0      #To keep track of incoming resource value
        self.tracker_total_resource_production = 0
        self.tracker_total_resource_expenditure = 0     #Includes resources traded out of country