#goals of the game
"""
add more planets(2 more)
add inventory
each journey makes you lose gas and energy
import old staship fighting file
add stuff to do on the planets
add ship health that scales with ship fights
fix energy lvls
add things to do on the planets 
"""
#importing in libs
import random
import numpy
#presets
gas = 1000
energy = 500
ship_health_status = 6000

#int --> str
def instr():
    global gas_string
    global ship_health_status_string
    global gas
    global energy_string
    global energy
    global ship_health_status
    gas_string = str(gas)
    energy_string = str(energy)
    ship_health_status_string = str(ship_health_status)
#styling stuff
def bars():
    print("-0=-------------------------------=0-")
    
#copy past formats for the art
#....................
#====================
#[][][][][][][][][][]

#gas can art
def gas_cas():
    instr()
    bars()
    global gas_string
    print("...........[|]......")
    print("......./####[]......")
    print("....../#######\.....")
    print("......|##" + gas_string +"###\....")
    print("......|#########|...")
    print("====================")
#energy regen art
def energy_self():
    instr()
    bars()
    print("........"+ energy_string +".........")
    print("....................")
    print("...==......(o)......")
    print("..|%%|..../|#|\.....")
    print("..|%%|.....|#|......")
    print("..|__|...../.\......")
    print("....................")
#ship traveling art
def ship_travel_art():
    instr()
    bars()
    global ship_health_status_string
    print("....[Ship health is " + ship_health_status_string +"]..")
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
    print("..................+..")
    print("......==========.....")
    print("..+.=------===--=....")
    print("....=---=---===--=...")
    print(".....=--==-------=...")
    print("......===========....")
    print("..+..................")
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
        planet_one_code()
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
    print("[----No mans code----]")
    bars()
#gas menu art
def gas_menu():
    global gas
    gas_cas()
    print("==gas levels==")
    print(gas)
    print("==============")
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
        energy_self()
        print("you sleep and increase your energy levels to: ")
        energy = energy + 100
        print(energy)
        bars()
        space_ship_code()
        

def planet_one_code():
    global gas
    while True:
        p_one_choice = int(input("Do you wanna restock gas(1) get a bounty(2) learn some planet lore(3) or go back to your ship(4):"))
        if p_one_choice == 1:
            print("Re-stocked!")
            gas = 1000
            continue
        elif p_one_choice == 2:
            print("Next time youre back in your ship if you type 35718 you will activate a ship fight")
            continue
        elif p_one_choice == 3:
            print("This planet is 20000 light years old and was founded by the creator of the first space ship once he left earth due to the bomb")
            continue
        else:
            break
    ship_travel_art()
    space_ship_code()

#start menu
def starting():
    start_menu()
    x = input("Press enter to go to the spaceship: ")
    space_ship_code()
starting()
