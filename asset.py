""" Asset class

Used as a parent class for the basic data about assets,
no objects of this should therefore exist
"""


class Asset():

    def __init__(self, name: str, assettype: str, stattype: str,description: str):
        
            self.name = name
            self.assettype = assettype
            self.stattype = stattype
            self.description = description
            
    def get_name(self) -> str:
        return(self.name)

    def get_assettype(self) -> str:
        return(self.assettype)

    def get_stattype(self) -> str:
        return(self.stattype)

    def get_description(self) -> str:
        return(self.description)

    def tick(self):
        pass

    def save(self, parent_nation: object):
        pass
    #     file = open(f"saves/nation/{parent_nation.get_name()}.txt")
    #     line_number = 0
    #     line_array = []
    #     final_line_number = -1
    #     for line in file:
    #         # Scan the entire file for if entity already exists
    #         line_array.append(line)
    #         if line.rfind(str(self.get_name())) != -1:
    #             final_line_number = line_number
    #         line_number += 1
    #         file.close
    #     if final_line_number == -1:
    #         # If the entity doesn't already exist, just append at end of file
    #         file = open("saves/nationlist.txt","a")
    #         file.write(f"{self.get_name()},{self.stat_wealth},{self.stat_political},{self.stat_force},{self.turns}\n")
    #     else:
    #         # If entity already exists, rewrite entire file and make the specifc line it was on changed again
    #         file = open("saves/nationlist.txt","w")
    #         for line in line_array:
    #             if line_array.index(line) != final_line_number:
    #                 file.write(line)
    #             else:
    #                 file.write(f"{self.get_name()},{self.stat_wealth},{self.stat_political},{self.stat_force},{self.turns}\n")
    #     file.close()