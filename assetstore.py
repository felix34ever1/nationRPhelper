""" AssetStore class

Contains all buyable assets, loads them up on program start
"""
# from assets.abilityfolder import *
# from assets.abilityfolder import example_ability
# from assets.infrastructurefolder import *
# from assets.unitgroupfolder import *


class AssetStore():

    def __init__(self, temp_location):
        asset_file = open("saves/assetlist.txt","r")
        self.asset_list = []
        for line in asset_file:
            line = line.replace("\n","")
            line_parsed = line.split(",")
            line_parsed.append(line_parsed[0].replace("_"," "))
            line_parsed[2] = line_parsed[2].title()
            line_parsed[2] = line_parsed[2].replace(" ","")
            code = (f"from assets.{line_parsed[1]}folder.{line_parsed[0]} import {line_parsed[2]}")
            exec(code)
            if line_parsed[1] == "ability" or line_parsed[1] == "infrastructure":
                code = (f"self.asset_list.append({line_parsed[2]}(temp_location))")
            elif line_parsed[1] == "unitgroup":
                code = (f"self.asset_list.append({line_parsed[2]}())")

            exec(code)

            # if line_parsed[1] == "ability":
            #     if line_parsed[0] == "example_ability":
            #         self.asset_list.append(example_ability.ExampleAbility())

            # elif line_parsed[1] == "infrastructure":
            #     pass

            # elif line_parsed[1] == "unitgroup":
            #     pass


        for object in self.asset_list:
            print(object.name,object.stattype,object.description)