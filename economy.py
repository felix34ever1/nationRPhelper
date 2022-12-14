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
        self.tracker_economy_strength = 50
        self.tracker_political_stability = 50
        self.tracker_budget = (self.tracker_total_resource_expenditure+self.tracker_total_resource_production-self.tracker_incoming_trade) * (self.tracker_economy_strength*100000) + (self.tracker_population-self.tracker_urban_population+(self.tracker_urban_population*3)) * (self.tracker_political_stability/50)

    def set_tracker_population(self, amount: int):
        self.tracker_population = amount
        
    def set_tracker_urban_population(self, amount: int):
        self.tracker_urban_population = amount
    
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
    
    def add_raw_production(self,amount: int):
        self.raw_production += amount

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

    def add_tracker_total_resource_expenditure(self,amount: int):
        self.tracker_total_resource_expenditure += amount

    def add_tracker_incoming_trade(self,amount: int):
        self.tracker_incoming_trade += amount

    def add_tracker_economy_strength(self, amount: float):
        self.tracker_economy_strength += amount

    def add_tracker_political_stability(self, amount: float):
        self.tracker_political_stability += amount

    def set_tracker_economy_strength(self, amount: float):
        self.tracker_economy_strength = amount

    def set_tracker_political_stability(self, amount: float):
        self.tracker_political_stability = amount

    def set_tracker_budget(self, amount: float):
        self.tracker_budget = amount

    def menu(self):
        print('''
[1] - View statistics
[2] - Manage resources manually
[3] - Manage population manually
[4] - Exit
''')
        choice = int(input("Select item on menu: "))
        match choice:
            case 1:
                print(f"""
    [RAW RESOURCES]
Industrial Metals: {self.raw_industrial_metals}
Rare Metals: {self.raw_rare_metals}
Oil: {self.raw_oil}
Natural Gas: {self.raw_natural_gas}
Food: {self.raw_food}
Production: {self.raw_production}

    [INTERMEDIARY RESOURCES]
Plastics: {self.intermediary_plastics}
Electronics: {self.intermediary_electronics}
Advanced Parts: {self.intermediary_advanced_parts}

    [FINISHED PRODUCTS]
Consumer Products: {self.finished_consumer_products}
Military Products: {self.finished_military_products}
Power: {self.finished_power} 

    [NATION STATS]
Economic Strength: {self.tracker_economy_strength}
Political Stability: {self.tracker_political_stability}
Budget: {self.tracker_budget}
""")
            case 2:
                print(f"""
[1] Industrial Metals
[2] Rare Metals
[3] Oil
[4] Natural Gas
[5] Food
[6] Production
[7] Plastics
[8] Electronics
[9] Advanced Parts
[10] Consumer Products
[11] Military Products
[12] Power
                """)
                choice = int(input("Select resource to add to using index: "))
                if choice < 1 or choice > 12:
                    print("Choice unselected, returning...")
                else:
                    amount = int(input("Select amount to add: "))
                    if choice == 1:
                        self.add_raw_industrial_metals(amount)
                        print(f"New amount: {self.raw_industrial_metals}")
                    elif choice == 2:
                        self.add_raw_rare_metals(amount)
                        print(f"New amount: {self.raw_rare_metals}")
                    elif choice == 3:
                        self.add_raw_oil(amount)
                        print(f"New amount: {self.raw_oil}")
                    elif choice == 4:
                        self.add_raw_natural_gas(amount)
                        print(f"New amount: {self.raw_natural_gas}")
                    elif choice == 5:
                        self.add_raw_food(amount)
                        print(f"New amount: {self.raw_food}")
                    elif choice == 6:
                        self.add_raw_natural_gas(amount)
                        print(f"New amount: {self.raw_natural_gas}")

                    elif choice == 7:
                        self.add_intermediary_plastics(amount)
                        print(f"New amount: {self.intermediary_plastics}")
                    elif choice == 8:
                        self.add_intermediary_electronics(amount)
                        print(f"New amount: {self.intermediary_electronics}")
                    elif choice == 9:
                        self.add_intermediary_advanced_parts(amount)
                        print(f"New amount: {self.add_intermediary_advanced_parts}")
                    elif choice == 10:
                        self.add_finished_consumer_products(amount)
                        print(f"New amount: {self.finished_consumer_products}")
                    elif choice == 11:
                        self.finished_military_products(amount)
                        print(f"New amount: {self.finished_military_products}")
                    elif choice == 12:
                        self.add_finished_power(amount)
                        print(f"New amount: {self.finished_power}")                             
            case 3:
                print(f"""
[1]||Population:         [{self.tracker_population}]
[2]||Urban Population:   [{self.tracker_urban_population}]
                """)
                choice = int(input("Select number to change: "))
                if choice < 1 or choice > 2:
                    print("Out of index error, returning...")
                else:
                    amount = int(input("Input amount to change to: "))
                    if choice == 1:
                        self.set_tracker_population(amount)
                        
                    elif choice == 2:
                        self.set_tracker_urban_population(amount)
            case 4:
                print("Returning to nation menu...")           

    def save(self, parent_nation: object):
        # Must first scan file and see if a save of the economy already exists,
        # if it does it must replace the file again with the correct line rewritten.
        
        file = open("saves/economylist.txt","r")
        line_number = 0
        line_array = []
        final_line_number = -1
        for line in file:
            # Scan the entire file for if entity already exists
            line_array.append(line)
            if line.rfind(str(parent_nation.get_name())) != -1:
                final_line_number = line_number
            line_number +=1
            file.close
        if final_line_number == -1:
            # If the entity doesn't already exist, just append at end of file
            file = open("saves/economylist.txt","a")
            file.write(f"{parent_nation.get_name()},{self.raw_industrial_metals},{self.raw_rare_metals},{self.raw_oil},{self.raw_natural_gas},{self.raw_food},{self.raw_production},{self.intermediary_plastics},{self.intermediary_electronics},{self.intermediary_advanced_parts},{self.finished_consumer_products},{self.finished_military_products},{self.finished_power},{self.tracker_incoming_trade},{self.tracker_total_resource_expenditure},{self.tracker_total_resource_production},{self.tracker_economy_strength},{self.tracker_budget},{self.tracker_population},{self.tracker_urban_population},{self.tracker_political_stability}\n")
        else:
            # If entity already exists, rewrite entire file and make the specifc line it was on changed again
            file = open("saves/economylist.txt","w")
            for line in line_array:
                if line_array.index(line) != final_line_number:
                    file.write(line)
                else:
                    file.write(f"{parent_nation.get_name()},{self.raw_industrial_metals},{self.raw_rare_metals},{self.raw_oil},{self.raw_natural_gas},{self.raw_food},{self.raw_production},{self.intermediary_plastics},{self.intermediary_electronics},{self.intermediary_advanced_parts},{self.finished_consumer_products},{self.finished_military_products},{self.finished_power},{self.tracker_incoming_trade},{self.tracker_total_resource_expenditure},{self.tracker_total_resource_production},{self.tracker_economy_strength},{self.tracker_budget},{self.tracker_population},{self.tracker_urban_population},{self.tracker_political_stability}\n")
            file.close()


    def tick(self):
        # Called at beginning of every cycle, should be calculated before nation and assets

        self.tracker_budget =self.tracker_budget + ((self.tracker_total_resource_expenditure+self.tracker_total_resource_production-self.tracker_incoming_trade) * (self.tracker_economy_strength*100000) + (self.tracker_population-self.tracker_urban_population+(self.tracker_urban_population*3)) * (self.tracker_political_stability/50))/6
        
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

        self.tracker_population = int((self.tracker_population * (1.001))//1)
        self.tracker_urban_population = int((self.tracker_urban_population*(1+self.tracker_economy_strength//10000))//1)