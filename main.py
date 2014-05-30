"""

====================================================================

PYCLASSICS - Snake Game
Copyright (C) <2014>  <Ericson Willians.>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

====================================================================
Game written by Ericson Willians, a brazilian composer and programmer.

CONTACT: ericsonwrp@gmail.com
AS A COMPOSER: https://soundcloud.com/r-p-ericson-willians
YOUTUBE CHANNEL: http://www.youtube.com/user/poisonewein

====================================================================
"""

__author__ = 'EricsonWillians'

from pygame import *
from random import *

init() #Pygame Init Function

speed = 16 # An arbitrary speed value to be used in clock.tick()
squareSize = 16 # The default size of every game element (Each snake piece, and the food).
screenSize = squareSize*48 # The size of the screen: 768 by 768 pixels (16 based).
screen = display.set_mode((screenSize, screenSize)) # Pygame screen-creating function.
display.set_caption("PyclassicS")
gameFont = font.SysFont("helvetica", 16, True)
creditFont = font.SysFont("helvetica", 10, True)

done = False # Variable to handle the game's main loop.
pause = False # Variable to handle the pause option (We'll draw and deal with everything IF pause equals to false).
bounds = True # Enable "death" when outside the screen's boundaries.
fullscreen = False
clock = time.Clock() # Creating an instance of pygame.time.Clock() class to deal with "tick" method later on.
colors = {"BG": (0, 0, 0), "GAME": (255, 255, 255), "ON": (0, 255, 0), "OFF": (255, 0, 0)} # BG = BLACK, GAME = WHITE.
directions = ["NORTH", "SOUTH", "WEST", "EAST"] # Directions.
food = [randrange(0, 48), randrange(0, 48)] # Food's random initial coordinates.
snakeDirection = directions[0]
gridIndex = [] # The list to store every "grid index".
realPos = [] # The real position of each "grid index" in the screen, in terms of pixels.
# The grid has 48 squares of 16 by 16 pixels. I'll use the same indexes for the Y axis (The whole screen is a square).
for i in range(0, 48):
    gridIndex.append(i) # Stores the 48 index (0 to 47).
    realPos.append(i*16) # Stores the actual positions in the screen (0 to 752).
gridKeys = dict(zip(gridIndex, realPos)) # Transforms every index into a key, with its corresponding real position.
score = 0
# THE VERY SNAKE:
snakeLength = [[24, 24],[24, 23]]

def drawSnake():
        # It loops through snakeLength list, and then I access each individual x and y keys inside each list (Each "snake piece").
    for i in snakeLength:
        try:
            draw.rect(screen, colors.get("GAME"), (gridKeys.get(i[0]), gridKeys.get(i[1]), squareSize, squareSize))
        except:
            pass

def drawBackground():
    # The default screen color is already black, but it's necessary to REALLY DRAW each "ground" in order not to make a "tron game".
    for i in range(0, 48): # The principle here is pretty straight-foward: For each collumn (48),
        for j in range(0, 48): # draw 46 16 by 16 squares (Filling the entire 768 by 768 screen).
            draw.rect(screen, colors.get("BG"), (i*16, j*16, squareSize, squareSize))

# The "updateGame()" procedure is called inside the main loop.
# It's more organized than just throwing code inside the game loop.

def updateGame():

    def respawnFood():
        food[0] = randrange(0, 48)
        food[1] = randrange(0, 48)

    # Now things get quite complicated. Here's the snake-movement part, a beast quite hard to grasp at first.
    # Basically, the snake is just a FIFO-QUEUE.

    def default():
        global score
        del snakeLength[:]
        respawnFood()
        score = 0
        print "GAME OVER!\n"*100

    def moveSnake():
        global score # Avoiding python scope problems.
        snakeLength.pop() # "pop()" removes the last list-element and returns it (But I don't use the returned element (It falls into the Void.))
        next = snakeLength[0] # Here I create a variable to store the very first snake index (List with x and y coordinates).
        drawBackground() # Draws the background at each frame.
        draw.rect(screen, colors.get("GAME"), (gridKeys.get(food[0]), gridKeys.get(food[1]), squareSize, squareSize)) # It draws the food.
        drawSnake() # Draws the snake after the background at each frame.
        print "Positions: " + str(snakeLength) # Print the snake for debugging purposes.
        if snakeDirection == "NORTH": # If the snake's current direction equals to NORTH:
            next = (next[0], next[1]-1) # That first index of the snake has it's y coordinate subtracted by 1.
            if ((next[0] == food[0]) and (next[1] == food[1])): # If the snake pos is equal to the food pos.
                snakeLength.append((snakeLength[len(snakeLength)-1][0], snakeLength[len(snakeLength)-1][1]-1)) # Append a new tuple-snake-piece in front of the last.
                respawnFood()
                score += 1
        elif snakeDirection == "SOUTH": # The same for the rest...
            next = (next[0], next[1]+1)
            if ((next[0] == food[0]) and (next[1] == food[1])):
                snakeLength.append((snakeLength[len(snakeLength)-1][0], snakeLength[len(snakeLength)-1][1]+1))
                respawnFood()
                score += 1
        elif snakeDirection == "WEST":
            next = (next[0]-1, next[1])
            if ((next[0] == food[0]) and (next[1] == food[1])):
                snakeLength.append((snakeLength[len(snakeLength)-1][0]-1, snakeLength[len(snakeLength)-1][1]))
                respawnFood()
                score += 1
        elif snakeDirection == "EAST":
            next = (next[0]+1, next[1])
            if ((next[0] == food[0]) and (next[1] == food[1])):
                snakeLength.append((snakeLength[len(snakeLength)-1][0]+1, snakeLength[len(snakeLength)-1][1]))
                respawnFood()
                score += 1
        # If the head of the snake gets off-screen, it defaults the game.
        if bounds == True:
            if next[1] < 0:
                default()
            elif next[1] > 47:
                default()
            elif next[0] < 0:
                default()
            elif next[0] > 47:
                default()
        # This part defaults the game if the snake collides with its own tail.
            if len(snakeLength) > 2:
                for i in snakeLength:
                    if ((next[0] == i[0]) and (next[1] == i[1])):
                        default()
        snakeLength.insert(0, next) # It inserts to the first position of the snake that very old-first one, forcing it to the new position.

    moveSnake() # I've made this procedure just for the "moveSnake()" name. It's easier to understand than throwing movement-code up there at random.

def keyPressed(inputKey): # Just a function to deal with inputs more efficiently.
    keysPressed = key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False

while not done: # WHILE NOT DONE... While done equals to that False up there.
    for e in event.get(): # For each event in whatever-that-pygame-function-returns (A list, probably).
        if e.type == QUIT or keyPressed(K_ESCAPE): # If that "e" variable equals to pygame QUIT (Some inner/default value) or to the escape key.
            done = True # FINISH THE LOOP! (For it runs only while done is equal to that False up there).
        if keyPressed(K_p) and pause == False: # Pretty straight-foward pause logic.
            pause = True
            print "Paused Game."
        elif keyPressed(K_p) and pause == True:
            pause = False
            print "Game resumed..."
        if keyPressed(K_F10): # Enter fullscreen.
            screen = display.set_mode((screenSize, screenSize), FULLSCREEN)
            fullscreen = True
        if keyPressed(K_F11): # Exit fullscreen.
            screen = display.set_mode((screenSize, screenSize))
            fullScreen = False
        # It changes the direction (What changes the snakeDirection up there)
        if keyPressed(K_UP) or keyPressed(K_w):
            snakeDirection = directions[0]
        if keyPressed(K_DOWN) or keyPressed(K_s):
            snakeDirection = directions[1]
        if keyPressed(K_LEFT) or keyPressed(K_a):
            snakeDirection = directions[2]
        if keyPressed(K_RIGHT) or keyPressed(K_d):
            snakeDirection = directions[3]
        if keyPressed(K_KP_MINUS):
            speed /= 2
        if keyPressed(K_KP_PLUS):
            speed *= 2
        if (keyPressed(K_b) and (bounds == True)):
            bounds = False
        elif (keyPressed(K_b) and (bounds == False)):
            bounds = True

    if  pause == False:
        try:
            updateGame() # Much better than all that code down here, isn't it?
        except:
            # The default procedure just clears the snakeLength list. It's here that it is set to its original value.
            # When a TypeError is found.
            if bounds == True:
                snakeLength = [[24, 24],[24, 23]]
            else:
                pass

    scoreText = gameFont.render("Score: " + str(score), True, colors.get("GAME"))
    speedText = gameFont.render("Speed: " + str(speed), True, colors.get("GAME"))
    if bounds == True:
        boundsText = gameFont.render("Bounds: ON", True, colors.get("ON"))
        screen.blit(boundsText, (10, 50))
    elif bounds == False:
        boundsText = gameFont.render("Bounds: OFF", True, colors.get("OFF"))
        coordinates = gameFont.render("x: " + str(snakeLength[len(snakeLength)-1][0]) + " " + "y: " + str(snakeLength[len(snakeLength)-1][1]), True, colors.get("OFF"))
        screen.blit(boundsText, (10, 50))
        screen.blit(coordinates, (690, 10))
    if fullscreen == False:
        fullscreenText = gameFont.render("Fullscreen: OFF", True, colors.get("OFF"))
        screen.blit(fullscreenText, (10, 70))
    elif fullscreen == True:
        fullscreenText = gameFont.render("Fullscreen: ON", True, colors.get("ON"))
        screen.blit(fullscreenText, (10, 70))
    keysText = creditFont.render("Keys: ARROWS, WASD, KP +-, B, F10, F11.", True, colors.get("GAME"))
    creditText = creditFont.render("Developed by Ericson Willians.", True, colors.get("GAME"))
    screen.blit(scoreText, (10, 10))
    screen.blit(speedText, (10, 30))
    screen.blit(keysText, (10, 750))
    screen.blit(creditText, (620, 750))
    display.update() # Pygame default display-thing.
    display.flip() # It updates the whole thing at each frame of the loop, or something like that.
    clock.tick(speed) # The pygame speed, or something like that.

print "Exiting..."
quit() # When done is equal to True, the program reaches this area (It closes).