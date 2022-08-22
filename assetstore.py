""" AssetStore class

Contains all buyable assets, loads them up on program start
"""
# from assets.abilityfolder import *
# from assets.abilityfolder import example_ability
# from assets.infrastructurefolder import *
# from assets.unitgroupfolder import *


class AssetStore():

    def __init__(self, list_nation):
        
        self.list_nation = list_nation

        asset_file = open("saves/assetlist.txt","r")
        self.asset_list = []
        for line in asset_file:
            #Below code formats the assetlist file to be read correctly
            line = line.replace("\n","")
            line_parsed = line.split(",")
            line_parsed.append(line_parsed[0].replace("_"," "))
            line_parsed[2] = line_parsed[2].title()
            line_parsed[2] = line_parsed[2].replace(" ","")
            code = (f"from assets.{line_parsed[1]}folder.{line_parsed[0]} import {line_parsed[2]}")
            # The above string is executed, this allows the code to parse together the path needed to be accessed on the fly.
            
            exec(code)
            
            if line_parsed[1] == "ability" or line_parsed[1] == "infrastructure":
                code = (f"self.asset_list.append([{line_parsed[2]},'{line_parsed[1]}',{line_parsed[2]}('No Location')])")
            elif line_parsed[1] == "unitgroup":
                code = (f"self.asset_list.append([{line_parsed[2]},'{line_parsed[1]}',{line_parsed[2]}()])")
            # Adds to a list with  class, asset type and an example object of the class
            exec(code)

    def menu(self, accessing_nation: object) -> object:
        # To be called by nation needing to get asset

        print("Wealth Assets:")
        for asset in self.asset_list:
            if asset[2].get_stattype() == "wealth":
                print(f"[{self.asset_list.index(asset)}] {asset[2].get_name()}")

        print("\nPolitical Assets:")
        for asset in self.asset_list:
            if asset[2].get_stattype() == "political":
                print(f"[{self.asset_list.index(asset)}] {asset[2].get_name()}")

        print("\nForce Assets:")
        for asset in self.asset_list:
            if asset[2].get_stattype() == "force":
                print(f"[{self.asset_list.index(asset)}] {asset[2].get_name()}")

        choice = int(input(f"\nInput index of item you'd like to add or type [{len(self.asset_list)}] to quit"))
        if choice == len(self.asset_list):
            print("Exiting menu")
        elif choice < 0 or choice > len(self.asset_list):
            print("Choice is out of range")
        else:
            if self.asset_list[choice][1] == "ability" or self.asset_list[choice][1] == "infrastructure":
                print("\nSelect target nation\n")
                nation_choice = self.nation_picker()
                if nation_choice == None:
                    print("Target nation selection failed, returning...")
                    return(None)
                else:
                    return self.asset_list[choice][0](nation_choice)

            else:
                return self.asset_list[choice][0]()

    def nation_picker(self) -> object:
        for nation in self.list_nation:
            print(f"[{self.list_nation.index(nation)}] {nation.get_name()}")
        try:
            choice = int(input(f"Select nation via index or type {len(self.list_nation)} to go cancel"))
        except:
            print("Unidentified option, returning...")
            return(None)
        else:
            if choice < 0 or choice > len(self.list_nation):
                print("Out of index error, returning...")
                return(None)
            elif choice == len(self.list_nation):
                print("Returning... ")
                return(None)
            else:
                return self.list_nation[choice]