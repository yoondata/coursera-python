########################################################
### Mini-Project 1: Rock-paper-scissors-lizard-Spock ###
########################################################

import random

def name_to_number(name):
    if name == "rock":
        player_choice_num = 0
    elif name == "Spock":
        player_choice_num = 1
    elif name == "paper":
        player_choice_num = 2
    elif name == "lizard":
        player_choice_num = 3
    elif name == "scissors":
        player_choice_num = 4
    else:
        print "name_to_number got an invalid input:", name
        return
    return player_choice_num

def number_to_name(number):
    if number == 0:
        player_choice_name = "rock"
    elif number == 1:
        player_choice_name = "Spock"
    elif number == 2:
        player_choice_name = "paper"
    elif number == 3:
        player_choice_name = "lizard"
    elif number == 4:
        player_choice_name = "scissors"
    else:
        print "number_to_name got an invalid input:", number
        return
    return player_choice_name

def rpsls(player_choice):
    print
    player_number = name_to_number(player_choice)
    if type(player_number) != int:
        print "rpsls got an invalid input:", player_choice
    else:
        print "Player chooses", player_choice
        comp_number = random.randrange(0, 5)
        comp_choice = number_to_name(comp_number)
        print "Computer chooses", comp_choice        
        difference = (comp_number - player_number) % 5
        if difference == 1 or difference == 2:
            print "Computer wins!"
        elif difference == 3 or difference == 4:
            print "Player wins!"
        else:
            print "Player and computer tie!"
    return


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# additional test for the case of invalid input
rpsls("ruck")
