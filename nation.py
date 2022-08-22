""" Nation Class

Used to store data about a nation including all assets it has and its stats 
"""


class Nation():

    def __init__(self, name: str, stat_wealth: int, stat_political: int, stat_force: int, object_economy: object, object_store: object):

        self.turns = 0
        self.name = name
        self.stat_wealth = stat_wealth
        self.stat_force = stat_force
        self.stat_political = stat_political
        self.object_economy = object_economy
        self.object_store = object_store
        self.list_assets = []

    def get_name(self) -> str:
        return(self.name)

    def get_economy(self) -> object:
        return(self.object_economy)

    def load_asset(self, asset: object):
        self.list_assets.append(asset)

    def menu(self):

        print(f"{self.name}'s menu\n")

        print(
'''1: Access Assets
2: Aquire Assets
3: Access economy
4: Back
        ''')
        try:
            choice = int(input(""))
        except:
            print("Answer unexpected, exiting menu")
        else:
            if choice == 1:
                self.access_asset()
            elif choice == 2:
                self.acquire_asset()
            elif choice == 3:
                self.access_economy()
            elif choice == 4:
                print(f"Exiting {self.name}'s menu")
            else:
                print("Out of index, exiting menu")

    def access_asset(self):

        print(f"{self.name}'s assets\n")
        
        counter = 0
        for asset in self.list_assets:
            print(f"{counter}: {asset.get_name()} - {asset.get_description()}")
            counter+=1
        print(f"{counter}: Exit selector")
        exit_number = counter
        choice = int(input("\nSelect an asset using corresponding index number: "))

        if choice > exit_number:
            print("\nOut of index error: Exiting menu")
        elif choice < 0:
            print("\nOut of index error: Exiting menu")            
        elif choice == exit_number:
            print("\nExiting asset menu")
        else:
            self.list_assets[choice].menu
        self.menu()


    def acquire_asset(self) -> object:

        acquired_asset = (self.object_store.menu(self))
        if acquired_asset != None:
            self.list_assets.append(acquired_asset)
        self.menu()

    def access_economy(self):

        self.object_economy.menu()
        self.menu()

    def save(self):
        # Save economy details
        self.object_economy.save(self)
        
        # Save asset details
        asset_file = open(f"saves/nations/{self.get_name()}", "w")
        for asset in self.list_assets:
            if asset.get_assettype() == "ability":
                asset_file.write(f"{asset.get_name()},{asset.get_assettype()},{asset.get_duration()},{asset.get_location().get_name()}\n")
            elif asset.get_assettype() == "infrastructure":
                asset_file.write(f"{asset.get_name()},{asset.get_assettype()},{asset.get_location().get_name()},{asset.get_health}\n")
            elif asset.get_assettype() == "unitgroup":
                composition = str(asset.get_composition()).replace(",","|") # commas get read as string breakers when loading file so they will be changed so that composition stays as one string
                asset_file.write(f"{asset.get_name()},{asset.get_assettype()},{composition},{asset.get_health()}\n")
        asset_file.close()

        # Save Nation details
        file = open("saves/nationlist.txt","r")
        line_number = 0
        line_array = []
        final_line_number = -1
        for line in file:
            # Scan the entire file for if entity already exists
            line_array.append(line)
            if line.rfind(str(self.get_name())) != -1:
                final_line_number = line_number
            line_number +=1
            file.close
        if final_line_number == -1:
            # If the entity doesn't already exist, just append at end of file
            file = open("saves/nationlist.txt","a")
            file.write(f"{self.get_name()},{self.stat_wealth},{self.stat_political},{self.stat_force},{self.turns}\n")
        else:
            # If entity already exists, rewrite entire file and make the specifc line it was on changed again
            file = open("saves/nationlist.txt","w")
            for line in line_array:
                if line_array.index(line) != final_line_number:
                    file.write(line)
                else:
                    file.write(f"{self.get_name()},{self.stat_wealth},{self.stat_political},{self.stat_force},{self.turns}\n")
        file.close()


    def tick(self, phase: int=1):
        # The tick is called upon a nation twice, once to process phase one and then again for phase 2.
        #  Phase 1: Processes economy update
        #  Phase 2: Processes assets + nation assets

        if phase == 1:
            self.object_economy.tick()


        elif phase == 2:
            for asset in self.list_assets:
                asset.tick()
            self.turns += 1