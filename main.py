"""The main script of the project.

"""

from tempfile import tempdir
from nation import Nation
from economy import Economy
from asset import Asset
from assetstore import AssetStore


list_nation = []
assetStore = AssetStore(list_nation)


def menu():
    isRunning = True

    while isRunning:
        print('''
[0] - Access nation menu 
[1] - Tick
[2] - Save
        ''')
        try:
            choice = int(input("Select option: "))
        except:
            print("You dolt")
        else:
            match choice:
                
                case 0:
                
                    for nation in list_nation:
                        print(f"[{list_nation.index(nation)}] - {nation.get_name()}")
                    
                    choice = int(input(f"Select index of country menu to access or {len(list_nation)}: "))
                    if choice > len(list_nation) or choice < 0:
                        print("Out of index error, returning..")
                    elif choice == len(list_nation):
                        print("Returning...")
                    else:
                        list_nation[choice].menu()
    
                case 1:
                
                    for nation in list_nation:
                        nation.tick(1)
                    
                    for nation in list_nation:
                        nation.tick(2)
                
                case 2:
                
                    for nation in list_nation:
                        nation.save()
                
                case _:
                
                    print("Out of index error")


def load():
    
    nation_file = open("saves/nationlist.txt")
    for line in nation_file:
        # Prepares line into array to be turned into nation.
        line = line.replace("\n","")
        line_parsed = line.split(",")
        economy_file = open("saves/economylist.txt")
        
        economy_found = False
        for economy in economy_file:
            if economy.find(line_parsed[0]) != -1:
                economy = economy.replace("\n","")
                economy_parsed = economy.split(",")
                economy_found = True
        if economy_found == True:
            economy_file.close()
            list_nation.append(Nation(line_parsed[0], line_parsed[1], line_parsed[2], line_parsed[3], Economy(int(economy_parsed[18]),int(economy_parsed[19])),assetStore, int(line_parsed[4])))
            list_nation[-1].get_economy().add_raw_industrial_metals(int(economy_parsed[1]))
            list_nation[-1].get_economy().add_raw_rare_metals(int(economy_parsed[2]))
            list_nation[-1].get_economy().add_raw_oil(int(economy_parsed[3]))
            list_nation[-1].get_economy().add_raw_natural_gas(int(economy_parsed[4]))
            list_nation[-1].get_economy().add_raw_food(int(economy_parsed[5]))
            list_nation[-1].get_economy().add_raw_production(int(economy_parsed[6]))

            list_nation[-1].get_economy().add_intermediary_plastics(int(economy_parsed[7]))
            list_nation[-1].get_economy().add_intermediary_electronics(int(economy_parsed[8]))
            list_nation[-1].get_economy().add_intermediary_advanced_parts(int(economy_parsed[9]))

            list_nation[-1].get_economy().add_finished_consumer_products(int(economy_parsed[10]))
            list_nation[-1].get_economy().add_finished_military_products(int(economy_parsed[11]))
            list_nation[-1].get_economy().add_finished_power(int(economy_parsed[12]))

            list_nation[-1].get_economy().add_tracker_incoming_trade(int(economy_parsed[13]))
            list_nation[-1].get_economy().add_tracker_total_resource_expenditure(int(economy_parsed[14]))
            list_nation[-1].get_economy().add_tracker_total_resource_production(int(economy_parsed[15]))
            list_nation[-1].get_economy().set_tracker_economy_strength(int(economy_parsed[16]))
            list_nation[-1].get_economy().set_tracker_budget(int(economy_parsed[17]))

        else:
            print(f"No economy found for {line_parsed[0]}, creating default, Manually set population -> ")
            population = int(input("Enter Population: "))
            urb_population = int(input("Enter Urban Population: "))
            list_nation.append(Nation(line_parsed[0], line_parsed[1], line_parsed[2], line_parsed[3], Economy(population,urb_population),assetStore, int(line_parsed[4])))
        
            

    for nation in list_nation:
        asset_file = open(f"saves/nations/{nation.get_name()}")
        for line in asset_file:
            line = line.replace("\n","")
            line_parsed = line.split(",")
            asset_file_name = line_parsed[0].lower().replace(" ","_")
            asset_class_name = line_parsed[0].title().replace(" ","")
            exec(f"from assets.{line_parsed[1]}folder.{asset_file_name} import {asset_class_name}")
            if line_parsed[1] == "ability":
                for target_nation in list_nation:
                    if target_nation.get_name() == line_parsed[3]:
                        nation_selected = target_nation
                exec(f"asset_object = {asset_class_name}(nation_selected,line_parsed[2])")
                exec("nation.load_asset(asset_object)")

            elif line_parsed[1] == "infrastructure":
                for target_nation in list_nation:
                    if target_nation.get_name() == line_parsed[2]:
                        nation_selected = target_nation
                exec(f'asset_object = {asset_class_name}(nation_selected,int(line_parsed[3]))')
                exec("nation.load_asset(asset_object)")

            elif line_parsed[1] == "unitgroup":
                composition = line_parsed[2]
                composition = composition.replace("[","").replace("]","").replace("|",",")
                composition = composition.split(",")
                composition_list = []
                for element in composition:
                    if element != '':
                        composition_list.append(element)
                exec(f"asset_object = {asset_class_name}({line_parsed[3]},{composition_list})")
                exec("nation.load_asset(asset_object)")


        


load()    
menu()