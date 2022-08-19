"""The main script of the project.

"""

from tempfile import tempdir
from nation import Nation
from economy import Economy
from asset import Asset
from assetstore import AssetStore


list_nation = []
the_store = AssetStore(list_nation)

France = Nation("French Republic", 4, 3, 5, Economy(67390000000,54000000),the_store)
list_nation.append(France)

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

def save():
    for nation in list_nation():
        nation.save()
        
menu()