#######################################################
#########  Mini-Project 2: Guess the number!  #########
#######################################################

import simplegui
import random

secret_number = 0
chances_remaining = 0
range_mode = 0

def new_game():
    if range_mode == 0:
        range100()
    else:
        range1000()

def range100():
    global range_mode
    if range_mode != 0:
        range_mode = 0
    global secret_number
    secret_number = random.randrange(0, 100)
    global chances_remaining
    chances_remaining = 7
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is 7"
    print ""

def range1000():
    global range_mode
    if range_mode != 1:
        range_mode = 1
    global secret_number
    secret_number = random.randrange(0, 1000)
    global chances_remaining
    chances_remaining = 10
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is 10"
    print ""

def input_guess(guess):
    guess_number = int(guess)
    print "Guess was", guess_number
    global chances_remaining
    chances_remaining -= 1
    print "Number of remaining guesses is", chances_remaining
    if guess_number < secret_number:
        print "Higher!"
        print ""
    elif guess_number > secret_number:
        print "Lower!"
        print ""
    else:
        print "Correct!"
        print ""
        new_game()
    if chances_remaining == 0:
        print "Sorry, you have used up all your guesses. You lost."
        print ""
        new_game()

frame = simplegui.create_frame("Guess the number!", 300, 300)
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

frame.start()

new_game()

# Please note that I have created another global variable 
# "range_mode" so the game restarts with the same range 
# as the one for the immediately preceding round.
