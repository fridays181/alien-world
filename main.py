import random
import numpy
gas = 1000
energy = 500

def bars():
    print("-0=-------------=0-")
#....................
#====================
#[][][][][][][][][][]

#art
def space_map():
    print("[___Map____]")
    print("[..+...oA.+]")
    print("[..0B..+.+.]")
    print("[.oC.+..+..]")
    print("[+..+...0D.]")
    print("[__________]")
def demo_planet():
    bar()
    print(".................+..")
    print("........0....+......")
    print("...+................")
    print(".............o...+..")
    print(".....+........{}....")
    print("............{}{}{}..")
    print("...............|....")
    print(".v....v........|v...")
    print("--___---____---|--__")
    bar()
    
def space_ship_inside():
    bars()
    print("==_____=============")
    print("=|-+--o|1========_==")
    print("=|_____|=========_==")
    print("=================_==")
    print("====================")
    print("=======|////|=======")
    print("========3||====-_-==")
    print("========|//|====|2==")
    print("=======|////|===|===")
    print("======|//////|==|===")
    bars()
def start_menu():
    bars()
    print("[][][][][][][][][][+")
    print("[][][+][][]Ethans[][")
    print("[][][][][]Sky[][][][")
    print("[+][][][][][][][][][")
    print("[][][][][][][][][+][")
    print("[][+][][][][+][][][]")
    bars()
def gas_menu():
    global gas
    bars()
    print("==gas levels==")
    print(gas)
    print("==============")
    bars()

def space_ship_code():
    global energy
    space_ship_inside()
    x = int(input("Press 1(space map), 2(check ship gas levels), or 3(rest): "))
    if x == 1:
        space_map()
    elif x == 2:
        gas_menu()
        space_ship_code()
    else:
        bars()#add true false so you can only sleep once per mission completion
        print("you sleep and increase your energy levels to: ")
        energy = energy + 100
        print(energy)
        bars()
        space_ship_code()



def starting():
    start_menu()
    x = input("Press enter to go to the spaceship: ")
    space_ship_code()
starting()
