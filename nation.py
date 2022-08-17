"""Nation Class

Used to store data about a nation including all assets it has and its stats 
"""


class Nation():

    def __init__(self, name: str, stat_wealth: int, stat_force: int, stat_political: int, object_economy: object):

        self.name = name
        self.stat_wealth = stat_wealth
        self.stat_force = stat_force
        self.stat_political = stat_political
        self.object_economy = object_economy
        self.list_assets = []

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
                print("Exiting menu")
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
            print(f"\nExiting {self.name}'s menu")
        else:
            self.list_assets[choice].menu


    def acquire_asset(self, asset, list_asset):

        pass

    def access_economy(self):

        self.object_economy.menu()

    def tick(self):

        pass