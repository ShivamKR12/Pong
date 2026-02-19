import pygame, sys, random


# general setup
pygame.init()
clock = pygame.time.Clock()

# create a screen width and height constant to be used for the size of the window
# but also for later maths calculations
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# setup the pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

# create the ball for the game using the a rectangle
# and place it in exact center of the pygame screen
ball = pygame.Rect(SCREEN_WIDTH / 2 - 15, SCREEN_HEIGHT / 2 - 15, 30, 30)
# then create a player and place it in the middle of the right side of the screen
player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2 - 70, 10, 140)
# and the opponent on the left side of the screen
opponent = pygame.Rect(10, SCREEN_HEIGHT / 2 - 70, 10, 140)

# create the color objects for the background, player and the opponent
BG_COLOR = pygame.Color('grey12')
LIGHT_GREY = (200, 200, 200)

# ( the random.choice((-1, 1)) decides if the ball will start moving to the left or the right 
# when the game starts )
# horizontal speed of the ball
BALL_SPEED_X = 7 * random.choice((-1, 1))
# verticle speed of the ball
BALL_SPEED_Y = 7 * random.choice((-1, 1))

# create a variable to declare the speed of the player,
# and using it, decide on the direction of the motion of the player later on
PLAYER_SPEED = 0
# declare the speed for the opponent's paddle
OPPONENT_SPEED = 7

# text variables
PLAYER_SCORE = 0
OPPONENT_SCORE = 0
game_font = pygame.font.Font(None, 32)

# score timer variable
score_time = True


def ball_animation():
    global BALL_SPEED_X, BALL_SPEED_Y, PLAYER_SCORE, OPPONENT_SCORE, score_time

    # move the ball to the right each frame, based on BALL_SPEED_X and BALL_SPEED_Y
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # check if the ball collides with any of the 4 sides of the screen
    # if they do, then flip their direction of velocity and hence the movement
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        BALL_SPEED_Y *= -1
    
    # if the ball hits the left or right sides of the screen, then reset the ball
    if ball.left <= 0:
        # if the ball hit's the left side of screen, then increase the player's score
        PLAYER_SCORE += 1
        # update the score time
        score_time = pygame.time.get_ticks()
    if ball.right >= SCREEN_WIDTH:
        # if the ball hit's the right side of screen, then increase the opponent's score
        OPPONENT_SCORE += 1
        # update the score time
        score_time = pygame.time.get_ticks()
    
    # check if the ball is colliding with any of the paddles or not
    # if it is, then flip the direction of the motion of the ball
    if ball.colliderect(player) and BALL_SPEED_X > 0: 
        if abs(ball.right - player.left) < 10:
            BALL_SPEED_X *= -1
        elif abs(ball.bottom - player.top) < 10 and BALL_SPEED_Y > 10:
            BALL_SPEED_X *= -1
        elif abs(ball.top - player.bottom) < 10 and BALL_SPEED_Y < 10:
            BALL_SPEED_X *= -1
    if ball.colliderect(opponent) and BALL_SPEED_X < 0:
        if abs(ball.left - opponent.right) < 10:
            BALL_SPEED_X *= -1
        elif abs(ball.bottom - opponent.top) < 10 and BALL_SPEED_Y > 10:
            BALL_SPEED_X *= -1
        elif abs(ball.top - opponent.bottom) < 10 and BALL_SPEED_Y < 10:
            BALL_SPEED_X *= -1

def player_animation():
    player.y += PLAYER_SPEED
    
    # check if the player is colliding with the top and bottom sides of the window or not
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += OPPONENT_SPEED
    if opponent.bottom > ball.y:
        opponent.bottom -= OPPONENT_SPEED
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT

def ball_restart():
    global BALL_SPEED_X, BALL_SPEED_Y, score_time

    # the current_time variable, unlike the score_time variable get's updated each frame
    current_time = pygame.time.get_ticks()

    # move the ball of the center of the screen
    ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # when the time difference between current_time and the score_time is less than 700 milliseconds, 
    # then display the number 3 on the screen
    if current_time - score_time < 700:
        number_three = game_font.render('3', False, LIGHT_GREY)
        screen.blit(number_three, (SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 2 + 20))
    # when the difference is in between 700 milliseconds and 1.4 seconds, 
    # display the number 2 
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render('2', False, LIGHT_GREY)
        screen.blit(number_two, (SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 2 + 20))
    # and when it is greater than 1.4 seconds and less than 2.1 seconds, 
    # display the number 1
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render('1', False, LIGHT_GREY)
        screen.blit(number_one, (SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 2 + 20))

    # we need to check if the difference between the score_time and the current_time is less than 2.1 sec
    if current_time - score_time < 2100:
        # if it is less than 2.1 sec, then the ball isn't moving
        BALL_SPEED_X, BALL_SPEED_Y = 0, 0
    else:
        # otherwise the ball move in either of left or right direction randomly
        BALL_SPEED_Y = 7 * random.choice((-1, 1))
        BALL_SPEED_X = 7 * random.choice((-1, 1))
        score_time = None


# create a while loop to run the game
while True:
    # capture all pygame events
    for event in pygame.event.get():
        # if the pygame event is to exit the pygame window
        if event.type == pygame.QUIT:
            # uninitialize the pygame module and close the program
            pygame.quit()
            sys.exit()
        # if a key is pressed down
        if event.type == pygame.KEYDOWN:
            # and if that key is the down arrow key
            if event.key == pygame.K_DOWN:
                # then move the player downwards
                PLAYER_SPEED += 7
            # or if that key is the up arrow key
            if event.key == pygame.K_UP:
                # then move the player up
                PLAYER_SPEED -= 7
        # if a key press is released
        if event.type == pygame.KEYUP:
            # and the released key is the down arrow key
            if event.key == pygame.K_DOWN:
                # stop the player movement
                PLAYER_SPEED -= 7
            # or the released key is the up arrow key
            if event.key == pygame.K_UP:
                # stop the player movement
                PLAYER_SPEED += 7

    # move the ball and check for collisions each frame
    ball_animation()
    # also, move the player and check for it's collisions too
    player_animation()
    # create a simple opponent ai
    opponent_ai()
    
    # fill the background with some color so we don't the drawings of the previous frame
    # ( if the screen.fill() were to be on the bottom on the loop, 
    # then we will only see the background color due to the draw order )
    screen.fill(BG_COLOR)
    
    # draw the player and opponent surfaces
    pygame.draw.rect(screen, LIGHT_GREY, player)
    pygame.draw.rect(screen, LIGHT_GREY, opponent)
    # then draw the ball surface using the .ellipse() method
    # ( the reason why the drawn surface is a circle instead of a streached ellipse, 
    # is because both the lengths passed into it are of equal lengths )
    pygame.draw.ellipse(screen, LIGHT_GREY, ball)

    # draw a verticle line in the middle of the screen, to split the both sides
    # using .aaline() . it takes 4 arguments : 
    # 1. the screen to draw the line on
    # 2. the color of the line
    # 3. a tuple for the start point ( half of the screen's width for the middle and 
    # 0 for the top of the window )
    # 4. a tuple for the end point ( half of the screen's width for the middle and 
    # half of the screen's height for the middle of the bottom of the window )
    pygame.draw.aaline(screen, LIGHT_GREY, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

    # when the score_time variable's type changes to or becames True, 
    # the below statement becomes true and the ball_restart() function is called
    if score_time:
        ball_restart()

    # create the text to be displayed on the screen
    player_text = game_font.render(f'{PLAYER_SCORE}', False, LIGHT_GREY)
    opponent_text = game_font.render(f'{OPPONENT_SCORE}', False, LIGHT_GREY)
    # and set it's position on the screen
    screen.blit(player_text, (410, 300))
    screen.blit(opponent_text, (380, 300))
    
    # update the pygame window
    pygame.display.flip()
    clock.tick(60)