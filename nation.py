""" Nation Class

Used to store data about a nation including all assets it has and its stats 
"""


class Nation():

    def __init__(self, name: str, stat_wealth: int, stat_force: int, stat_political: int, object_economy: object, object_store: object):

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

        self.list_assets.append(self.object_store.menu(self))
        self.menu()

    def access_economy(self):

        self.object_economy.menu()
        self.menu()

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