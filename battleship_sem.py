# Intro

welcome_msg = "Welcome to the Ultimate Battleship Experience"
print(welcome_msg)
print("Who dares to enter the battle? Immediately state your name!")
player1 = input()
print("Ok then, " + player1 +", let's begin.")

# Rules (need to be refined)
rules = "I will hide 10 battleships in total. More on that later."
print("First things first. Are you familiar with the rules? (y/n)")
answer_rules = input().lower()
if answer_rules == "y":
    print("Looks like we are good to go.")    
elif answer_rules == "n":
    print(rules)
else:
    print("Come again? Please enter y for yes or n for no.")

# Setting up playing field

playing_field_empty = """
 ____ ____ ____ ____ ____ ____ ____ ____ ____ ____
|    |    |    |    |    |    |    |    |    |    |
| A0 | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | A9 |
|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |
| B0 | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 |
|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |
| C0 | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |
|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |
| D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 |
|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |
| E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 | E9 |
|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |
| F0 | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 |
|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |
| G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |
| H0 | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 | H9 |
|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |
| I0 | I1 | I2 | I3 | I4 | I5 | I6 | I7 | I8 | I9 |
|____|____|____|____|____|____|____|____|____|____|
|    |    |    |    |    |    |    |    |    |    |
| J0 | J1 | J2 | J3 | J4 | J5 | J6 | J7 | J8 | J9 |
|____|____|____|____|____|____|____|____|____|____|
"""

print("Press enter so that I can set up our playing field.")
input()
print("Let the battle begin!")

playing_field_rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
playing_field_columns = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
playing_fields = []

for letter in playing_field_rows:
    for i in range(10):
        playing_fields.append(letter + playing_field_columns[i])

# define hidden ships
# 1 carrier: 4 spaces
# 2 battleships: 3 spaces
# 3 cruisers: 2 spaces
# 4 destroyers: 1 space

# create function to randomly populate playing field

import random
distribution = ["horizontal", "vertical"]
up_down = ["up", "down"]
left_right = ["left", "right"]
def select_random_field(selection):
    return random.choice(selection)
def select_random_distribution():
    return random.choice(distribution)
def select_random_up_down():
    return random.choice(up_down)
def select_random_left_right():
    return random.choice(left_right)

available_choices = playing_fields

# define place_ship function that takes parameter of how many spaces a ship occupies

def place_ship(num):
    ship = []
    for i in range(num):
        ship.append("")
    if num < 1 or num > 4:
            print("Error. A ship needs to occupy at least one and a maximum of 4 playing fields. Set num equal to an integer between 1 and 4.")
    ship[0] = select_random_field(playing_fields)
    if num > 1:     
        index_counter = playing_fields.index(ship[0])
        dist = select_random_distribution()
        if dist == "horizontal":
            if str(num-2) in ship[0] or str(num-3) in ship[0] or str(num-4) in ship[0]:
                dir = "right"
            elif str(num+3) in ship[0] or str(num+4) in ship[0] or str(num+5) in ship[0]:
                dir = "left"
            else:
                dir = select_random_left_right()
            for i in range(num-1):
                if dir == "right":
                    index_counter += 1
                    ship[i+1] = playing_fields[index_counter]
                else:
                    index_counter -=1
                    ship[i+1] = playing_fields[index_counter]
        else:
            if index_counter < (num-1)*10:
                dir = "down"
            elif index_counter > (len(playing_fields)-1) - (num-1)*10:
                dir = "up"
            else:
                dir = select_random_up_down()
            for i in range(num-1):
                if dir == "down":
                    index_counter += 10
                    ship[i+1] = playing_fields[index_counter]
                else:
                    index_counter -=10
                    ship[i+1] = playing_fields[index_counter]
    return ship

def place_carrier():
    carrier = ["","","",""]
    carrier[0] = select_random_field(playing_fields)
    index_counter = playing_fields.index(carrier[0])
    dist = select_random_distribution()
    if dist == "horizontal":
        if "0" in carrier[0] or "1" in carrier[0] or "2" in carrier[0]:
            dir = "right"
        if "9" in carrier[0] or "8" in carrier[0] or "7" in carrier[0]:
            dir = "left"
        dir = select_random_left_right()
        if dir == "right":
            for i in range(3):
                index_counter += 1
                carrier[i+1] = playing_fields[index_counter]
        else:
            for i in range(3):
                index_counter -=1
                carrier[i+1] = playing_fields[index_counter]
    else:
        if "A" in carrier[0] or "B" in carrier[0] or "C" in carrier[0]:
            dir = "down"
        if "J" in carrier[0] or "I" in carrier[0] or "H" in carrier[0]:
            dir = "up"
        dir = select_random_up_down()
        if dir == "down":
            for i in range(3):
                index_counter += 10
                carrier[i+1] = playing_fields[index_counter]
        else:
            for i in range(3):
                index_counter -=10
                carrier[i+1] = playing_fields[index_counter]
    return carrier

carrier = place_ship(4)
battleship_1 = ["C5", "D5", "E5"]
battleship_2 = ["I5", "I6", "I7"]
battleships = battleship_1 + battleship_2
cruiser_1 = ["G1", "H1"]
cruiser_2 = ["D8", "E8"]
cruiser_3 = ["G4", "G5"]
cruisers = cruiser_1 + cruiser_2 + cruiser_3
destroyer_1 = ["J0"]
destroyer_2 = ["B7"]
destroyer_3 = ["H9"]
destroyer_4 = ["D2"]
destroyers = destroyer_1 + destroyer_2 + destroyer_3 + destroyer_4
occupied_fields = carrier + battleships + cruisers + destroyers

# function to display solved playing field

def display_solution():
    playing_field_solution = playing_field_empty
    for field in playing_fields:
        playing_field_progress = """"""
        if field in occupied_fields:
            playing_field_progress = playing_field_solution.replace(" " + field + " ", "OOOO")
        else:
            playing_field_progress = playing_field_solution.replace(" " + field + " ", "~~~~")
        playing_field_solution = playing_field_progress
    return playing_field_progress

# game itself

def battleship_game():
    print(playing_field_empty)
    print("I have hidden my ships well. If at any point during the game you would like to review the rules, enter '?', otherwise give me your next target.")
    hit_list = []
    print(carrier)
    miss_list = []
    total_missiles = 0
    total_hits = 0
    # create function to reprint the playing field with hits and misses marked after each shot
    playing_field_updated = playing_field_empty 
    def playing_field_update(aim, hit_or_miss):
        playing_field_progress = """"""
        if hit_or_miss == "MISS":
            playing_field_progress = playing_field_updated.replace(" " + aim + " ", "~~~~")
        elif hit_or_miss == "HIT":
            playing_field_progress = playing_field_updated.replace(" " + aim + " ", "OOOO")
        else:
            playing_field_progress = playing_field_updated
        return playing_field_progress
    # create function to detect if a ship has been sunk (start with carrier)
    def ship_sunk(aim):
        if aim in occupied_fields:
            if aim in destroyers:
                print("*** SHIP SUNK ***")
                print("You have sunk one of my destroyers.")
                if all(field in hit_list for field in destroyers):
                    print("All destroyers down.")
            elif aim in carrier:
                if all(field in hit_list for field in carrier):
                    print("*** SHIP SUNK ***")
                    print("You have sunk my carrier.")
            elif aim in battleship_1:
                if all(field in hit_list for field in battleship_1):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my battleships.")
                    if all(field in hit_list for field in battleships):
                        print("All battleships down.")
            elif aim in battleship_2:
                if all(field in hit_list for field in battleship_2):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my battleships.")
                    if all(field in hit_list for field in battleships):
                        print("All battleships down.")
            elif aim in cruiser_1:
                if all(field in hit_list for field in cruiser_1):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my cruisers.")
                    if all(field in hit_list for field in cruisers):
                        print("All cruisers down.")
            elif aim in cruiser_2:
                if all(field in hit_list for field in cruiser_2):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my cruisers.")
                    if all(field in hit_list for field in cruisers):
                        print("All cruisers down.")
            elif aim in cruiser_3:
                if all(field in hit_list for field in cruiser_3):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my cruisers.")
                    if all(field in hit_list for field in cruisers):
                        print("All cruisers down.")            
    for i in range(75):
        target = input().upper()
        outcome = ""
        if target == "?":
            print(rules)
            total_missiles -= 1
        elif target in hit_list or target in miss_list:
            outcome = "HAHAHA"
            print("You're wasting ammunition. You already hit this target.")
        elif target not in playing_fields:
            outcome = "PATHETIC"
            print("You are way outside the target area. Try again.")
        elif target in occupied_fields:
            outcome = "HIT"
            hit_list.append(target)
            total_hits += 1
        else:
            outcome = "MISS"
            miss_list.append(target)
        total_missiles +=1
        playing_field_updated = playing_field_update(target, outcome)
        print("*** " + outcome + " ***")
        ship_sunk(target)
        print(playing_field_updated)

        if total_hits < 20:
            print("You have launched " + str(total_missiles) + " missiles, " + str(75-total_missiles) + " missiles left.")
            print("So far your missiles hit my ships " + str(total_hits) + " times: " + str(hit_list))
            print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.")
        else:
            break
    if total_hits == 20:
        print("Congratulations. You won. It took " + str(total_missiles) + " missiles to take all my ships down. Well done!")
    else:
        print("Sorry. You didn't manage to destroy all my ships with the number of missiles at your disposal. You lost.")
        print("Here is the solution:")
        print(display_solution())
        print("You managed to hit " + str(total_hits) + " targets. Here is the complete list: " + str(hit_list))

battleship_game()

# Ask for new round

print("Wanna play another round? (y/n)")
answer_new_round = input().lower()
if answer_new_round == "y":
    print("Ok, " + player1 + ". Here we go.") 
    battleship_game()  
elif answer_new_round == "n":
    print("Good-bye then.")
else:
    print("Come again? Please enter y for yes or n for no.")

