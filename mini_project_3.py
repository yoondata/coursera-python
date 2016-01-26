#######################################################
#############  Mini-Project 3: Stopwatch  #############
#######################################################

import simplegui

current_time = 0
trial_total = 0
trial_correct = 0

def format(t):
    A = t // 600
    B = (t % 600) // 100
    C = ((t % 600) % 100) // 10
    D = (t % 600) % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)

def button_start():
    timer.start()

def button_stop():
    global trial_total, trial_correct
    if current_time < 6000 and timer.is_running():
        trial_total += 1
        if (current_time % 10) == 0:
            trial_correct += 1
    timer.stop()

def button_reset():
    global current_time, trial_total, trial_correct
    current_time = 0
    trial_total = 0
    trial_correct = 0

def timer_handler():
    global current_time
    if current_time < 6000:
        current_time += 1
    else:
        timer.stop()

def draw_handler(canvas):
    time_message = format(current_time)
    score = str(trial_correct) + "/" + str(trial_total)
    if current_time < 6000:
        canvas.draw_text(time_message, [90, 120], 50, 'White')
        canvas.draw_text(score, [250, 30], 20, 'Yellow')
    else:
        canvas.draw_text("Time is up. Good effort!", [30, 100], 25, 'Red')
        canvas.draw_text("Your final score is: " + score, [30, 130], 25, 'Red')

frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)

frame.add_button("Start", button_start, 120)
frame.add_button("Stop", button_stop, 120)
frame.add_button("Reset", button_reset, 120)
frame.set_draw_handler(draw_handler)

timer = simplegui.create_timer(100, timer_handler)

frame.start()
