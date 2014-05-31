"""

====================================================================

PYCLASSICS 1.1 - Snake Game
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

import pygame
from random import randrange

pygame.init()
clock = pygame.time.Clock()
screenSize = 768
screen = pygame.display.set_mode((screenSize,screenSize))
pygame.display.set_caption("PyclassicS 1.1")
fullscreen = False
gameFont = pygame.font.SysFont("helvetica", 16, True)
creditFont = pygame.font.SysFont("helvetica", 10, True)
done = False
pause = False
bounds = True # Enable "death" when outside the screen's boundaries.

colors = {"BG": (0,0,0), "GAME": (255,255,255), "ON": (0,255,0), "OFF": (255,0,0)}
directions = ["NORTH","SOUTH","WEST","EAST"]
score = 0

class Food():

    def __init__(self):

        self.pos = [randrange(0,48),randrange(0,48)]

    def respawn(self):

        self.pos[0] = randrange(0,48)
        self.pos[1] = randrange(0,48)

class Snake():

    def __init__(self,food):

        self.speed = 16
        self.size = 16
        self.dir = directions[0]
        self.gridIndex = []
        self.realPos = []
        for i in range(0,48):
            self.gridIndex.append(i)
            self.realPos.append(i*16)
        self.gridKeys = dict(zip(self.gridIndex,self.realPos))
        self.length = [[24,24],[24,23]]

        self.food = food

    def draw(self):

        for tail in self.length:
            try:
                pygame.draw.rect(screen,colors.get("GAME"),(self.gridKeys.get(tail[0]),
                    self.gridKeys.get(tail[1]),self.size,self.size))
            except:
                pass

    def default(self):

        global score
        del self.length[:]
        self.food.respawn()
        score = 0
        print "GAME OVER!\n"*100

    def move(self):

        global score
        self.length.pop()
        next = self.length[0]
        pygame.draw.rect(screen,colors.get("GAME"),(self.gridKeys.get(self.food.pos[0]),
            self.gridKeys.get(self.food.pos[1]),self.size,self.size))
        for tail in self.length:
            try:
                pygame.draw.rect(screen,colors.get("GAME"),(self.gridKeys.get(tail[0]),
                    self.gridKeys.get(tail[1]),self.size,self.size))
            except:
                pass
        print "Positions: " + str(self.length)
        if self.dir == "NORTH":
            next = (next[0],next[1]-1)
            if ((next[0] == self.food.pos[0]) and (next[1] == self.food.pos[1])):
                self.length.append((self.length[len(self.length)-1][0],self.length[len(self.length)-1][1]-1))
                self.food.respawn()
                score += 1
        elif self.dir == "SOUTH":
            next = (next[0],next[1]+1)
            if ((next[0] == self.food.pos[0]) and (next[1] == self.food.pos[1])):
                self.length.append((self.length[len(self.length)-1][0],self.length[len(self.length)-1][1]+1))
                self.food.respawn()
                score += 1
        elif self.dir == "WEST":
            next = (next[0]-1, next[1])
            if ((next[0] == self.food.pos[0]) and (next[1] == self.food.pos[1])):
                self.length.append((self.length[len(self.length)-1][0]-1,self.length[len(self.length)-1][1]))
                self.food.respawn()
                score += 1
        elif self.dir == "EAST":
            next = (next[0]+1, next[1])
            if ((next[0] == self.food.pos[0]) and (next[1] == self.food.pos[1])):
                self.length.append((self.length[len(self.length)-1][0]+1,self.length[len(self.length)-1][1]))
                self.food.respawn()
                score += 1

        if bounds == True:
            if next[1] < 0:
                self.default()
            elif next[1] > 47:
                self.default()
            elif next[0] < 0:
                self.default()
            elif next[0] > 47:
                self.default()

            if len(self.length) > 2:
                for i in self.length:
                    if ((next[0] == i[0]) and (next[1] == i[1])):
                        self.default()

        self.length.insert(0,next)

snake = Snake(Food())

def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False

while not done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or keyPressed(pygame.K_ESCAPE):
            done = True
        if keyPressed(pygame.K_p) and pause == False:
            pause = True
            print "Paused Game."
        elif keyPressed(pygame.K_p) and pause == True:
            pause = False
            print "Game resumed..."
        if keyPressed(pygame.K_F10):
            screen = pygame.display.set_mode((screenSize,screenSize),pygame.FULLSCREEN)
            fullscreen = True
        if keyPressed(pygame.K_F11):
            screen = pygame.display.set_mode((screenSize, screenSize))
            fullScreen = False

        if keyPressed(pygame.K_UP) or keyPressed(pygame.K_w):
            snake.dir = directions[0]
        if keyPressed(pygame.K_DOWN) or keyPressed(pygame.K_s):
            snake.dir = directions[1]
        if keyPressed(pygame.K_LEFT) or keyPressed(pygame.K_a):
            snake.dir = directions[2]
        if keyPressed(pygame.K_RIGHT) or keyPressed(pygame.K_d):
            snake.dir = directions[3]
        if keyPressed(pygame.K_KP_MINUS):
            snake.speed /= 2
        if keyPressed(pygame.K_KP_PLUS):
            snake.speed *= 2
        if (keyPressed(pygame.K_b) and (bounds == True)):
            bounds = False
        elif (keyPressed(pygame.K_b) and (bounds == False)):
            bounds = True

    pygame.draw.rect(screen,colors.get("BG"),(0,0,screenSize,screenSize))

    if pause == False:
        try:
            snake.move()
        except:
            if bounds == True:
                snake.length = [[24, 24],[24, 23]]
            else:
                pass

    scoreText = gameFont.render("Score: " + str(score), True, colors.get("GAME"))
    speedText = gameFont.render("Speed: " + str(snake.speed), True, colors.get("GAME"))
    if bounds == True:
        boundsText = gameFont.render("Bounds: ON", True, colors.get("ON"))
        screen.blit(boundsText, (10, 50))
    elif bounds == False:
        boundsText = gameFont.render("Bounds: OFF", True, colors.get("OFF"))
        coordinates = gameFont.render("x: " + str(snake.length[len(snake.length)-1][0]) + " " + "y: " + str(snake.length[len(snake.length)-1][1]), True, colors.get("OFF"))
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
    screen.blit(scoreText,(10,10))
    screen.blit(speedText,(10,30))
    screen.blit(keysText,(10,750))
    screen.blit(creditText,(620,750))
    pygame.display.flip()
    clock.tick(snake.speed)

print "Exiting..."
pygame.quit()