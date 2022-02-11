"""
add more planets(2 more)
add fighting
add inventory
each journey makes you lose gas and energy
import old staship fighting file
add graphics to energy and gas(battery with percent in it and gas can with percent in it)
add stuff to do on the planets
add ship health
"""



import random
import numpy
gas = 1000
energy = 500

def bars():
    print("-0=-------------------------------=0-")
    

#....................
#====================
#[][][][][][][][][][]

#ship traveling art
def ship_travel_art():
    bars()
    print("...............+.......+...")
    print(".....+.....................")
    print("......_______-\.......33...")
    print("......[[-------|==---333...")
    print("..+....\______/.......33...")
    print("..........+.........+......")
    print(".....+.....................")
    bars()
    x = input(": ")
#planet one art
def planet_one_outside():
    print(".....................")
    print("......==========.....")
    print("....=------===--=....")
    print("....=---=---===--=...")
    print(".....=--==-------=...")
    print("......===========....")
    print(".....................")
def planet_one_inside():
    bars()
    print("========{The forest}")
    print(".................+..")
    print("........0....+......")
    print("...+................")
    print(".............o...+..")
    print(".....+........{}....")
    print("............{}{}{}..")
    print("...............|....")
    print(".v....v........|v...")
    print("--___---____---|--__")
    bars()
#planet 2 art
def planet_two_outside():
    print("........_____........")
    print("...+.../%%%%%\....+..")
    print(".+..../%%(0)%%\......")
    print(".....|%%%%%%%%|..+...")
    print("...+..\%%%%%%/.......")
    print(".......\____/........")
    print("..+...............+..")
def planet_two_inside():
    bars()
    print("========{The streets}")
    print("[]====|.----.|====[]=")
    print("--====|.----.|====--=")
    print("---------------------")
    print("_______|..-..|_______")
    print("=======|..-..|=======")
    print("=====[]|.---.|====[]=")
    print("=====--|-----|====--=")
    print("---------------------")
    bars()
#space map code and art
def space_map():
    print("[____Map____]")
    print("[..+...o.1.+]")
    print("[..^.2..+.+.]")
    print("[.....+.....]")
    print("[.o.3.+..+..]")
    print("[+..+...0.4.]")
    print("[___________]")
def space_map_code():
    space_map()
    pick_planet = int(input("What planet to you wanna go to 1,2,3, or 4: "))
    if pick_planet == 1:
        ship_travel_art()
        planet_one_outside()
        x = input(": ")
        planet_one_inside()
    elif pick_planet == 2:
        ship_travel_art()
        planet_two_outside()
        x = input(": ")
        planet_two_inside()
    else:
        print("coming")
#inside space ship art
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
#start menu art
def start_menu():
    bars()
    print("[][][][][][][][][][+")
    print("[][][+][][]Ethans[][")
    print("[][][][][]Sky[][][][")
    print("[+][][][][][][][][][")
    print("[][][][][][][][][+][")
    print("[][+][][][][+][][][]")
    bars()
#gas menu art
def gas_menu():
    global gas
    bars()
    print("==gas levels==")
    print(gas)
    print("==============")
    bars()
#main space ship info
def space_ship_code():
    global energy
    space_ship_inside()
    x = int(input("Press 1(space map), 2(check ship gas levels), or 3(rest): "))
    if x == 1:
        space_map_code()
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
