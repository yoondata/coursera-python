##########################################################
################  Mini-Project 5: Memory  ################
##########################################################

import simplegui
import random

cards_1 = range(8)
cards_2 = range(8)
deck = cards_1 + cards_2
exposed = []
state = 0
num_1_idx = 0
num_2_idx = 0
turns = 0

def new_game():
    global deck, exposed, state, num_1_idx, num_2_idx, turns 
    random.shuffle(deck)
    exposed = [False for n in range(16)]
    state = 0
    num_1_idx = 0
    num_2_idx = 0
    turns = 1
    label.set_text("Turns = 0")

def mouseclick(pos):
    global state, num_1_idx, num_2_idx, turns
    if pos[0] >= 0 and pos[0] <= 800 and pos[1] >= 0 and pos[1] <= 100:
        index = pos[0] // 50
        if not exposed[index]:
            exposed[index] = True
            if state == 0:
                state = 1
                num_1_idx = index
            elif state == 1:
                state = 2
                num_2_idx = index
                label.set_text("Turns = " + str(turns))
            elif state == 2:
                if deck[num_1_idx] != deck[num_2_idx]:
                    exposed[num_1_idx] = False
                    exposed[num_2_idx] = False
                num_1_idx = index
                state = 1
                turns += 1
                
def draw(canvas):
    idx = 0
    for n in deck:
        if exposed[idx]:
            canvas.draw_text(str(n), [12 + 50 * idx, 70], 50, "White")
        else:
            canvas.draw_polygon([[50 * idx, 0], [50 * (idx + 1), 0], 
                                 [50 * (idx + 1), 100], [50 * idx, 100]], 
                                1, "Black", "Green")
        idx += 1

frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()
