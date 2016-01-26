########################################################
################  Mini-Project 4: Pong  ################
########################################################

import simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
RIGHT = True
LEFT = False

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

paddle1_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_pos = HEIGHT / 2
paddle2_vel = 0

score1 = 0
score2 = 0

def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]
    if direction == RIGHT:
        ball_vel[0] = random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 3)    
    elif direction == LEFT:
        ball_vel[0] = -random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 3)

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, score1, score2, RIGHT, LEFT
    paddle1_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_pos = HEIGHT / 2
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    if RIGHT:
        spawn_ball(RIGHT)
        RIGHT = False
        LEFT = True
    elif LEFT:
        spawn_ball(LEFT)
        RIGHT = True
        LEFT = False

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel) >= HALF_PAD_HEIGHT and (paddle1_pos + paddle1_vel) <= (HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
    if (paddle2_pos + paddle2_vel) >= HALF_PAD_HEIGHT and (paddle2_pos + paddle2_vel) <= (HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel

    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos - HALF_PAD_HEIGHT],[PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],[PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT],[0, paddle1_pos + HALF_PAD_HEIGHT]], 1, "Yellow", "Yellow")
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],[WIDTH, paddle2_pos - HALF_PAD_HEIGHT],[WIDTH, paddle2_pos + HALF_PAD_HEIGHT],[WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]], 1, "Yellow", "Yellow")

    # determine whether paddle and ball collide
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):
        if ball_pos[1] >= (paddle1_pos - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0]
        else:
            score2 += 1
            spawn_ball(RIGHT)
    elif ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        if ball_pos[1] >= (paddle2_pos - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0]
        else:
            score1 += 1
            spawn_ball(LEFT)

    # draw scores
    canvas.draw_text(str(score1), (200, 100), 50, "Red")
    canvas.draw_text(str(score2), (370, 100), 50, "Red")

def keydown(key):
    global paddle1_vel, paddle2_vel
    paddle_acc = 5
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= paddle_acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += paddle_acc
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= paddle_acc        
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += paddle_acc

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 200)

new_game()
frame.start()

