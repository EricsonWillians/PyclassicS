"""

====================================================================

PYCLASSICS 1.2 - Snake Game
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
AS A COMPOSER: http://www.youtube.com/user/poisonewein

====================================================================
"""

__author__ = 'EricsonWillians'

import pygame

import g
from food import Food
from snake import Snake

snake = Snake(Food())

def k(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False

while not g.done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or k(pygame.K_ESCAPE):
            g.done = True
        if k(pygame.K_p) and pause == False:
            pause = True
            print "Paused Game."
        elif k(pygame.K_p) and pause == True:
            pause = False
            print "Game resumed..."
        if k(pygame.K_F10):
            g.screen = pygame.display.set_mode((g.screenSize,g.screenSize),pygame.FULLg.screen)
            fullg.screen = True
        if k(pygame.K_F11):
            g.screen = pygame.display.set_mode((g.screenSize, g.screenSize))
            fullscreen = False

        if k(pygame.K_UP) or k(pygame.K_w):
            snake.dir = g.directions[0]
        if k(pygame.K_DOWN) or k(pygame.K_s):
            snake.dir = g.directions[1]
        if k(pygame.K_LEFT) or k(pygame.K_a):
            snake.dir = g.directions[2]
        if k(pygame.K_RIGHT) or k(pygame.K_d):
            snake.dir = g.directions[3]
        if k(pygame.K_KP_MINUS):
            snake.speed /= 2
        if k(pygame.K_KP_PLUS):
            snake.speed *= 2
        if (k(pygame.K_b) and (g.bounds == True)):
            g.bounds = False
        elif (k(pygame.K_b) and (g.bounds == False)):
            g.bounds = True

    pygame.draw.rect(g.screen,g.colors.get("BG"),(0,0,g.screenSize,g.screenSize))

    if g.pause == False:
        try:
            snake.giveLife()
        except:
            if g.bounds == True:
                snake.length = [[24, 24],[24, 23]]
            else:
                pass

    scoreText = g.gameFont.render("Score: " + str(g.score), True, g.colors.get("GAME"))
    speedText = g.gameFont.render("Speed: " + str(snake.speed), True, g.colors.get("GAME"))
    if g.bounds == True:
        boundsText = g.gameFont.render("Bounds: ON", True, g.colors.get("ON"))
        g.screen.blit(boundsText, (10, 50))
    elif bounds == False:
        boundsText = g.gameFont.render("Bounds: OFF", True, g.colors.get("OFF"))
        coordinates = g.gameFont.render("x: " + str(snake.length[len(snake.length)-1][0]) + " " + "y: " + str(snake.length[len(snake.length)-1][1]), True, colors.get("OFF"))
        g.screen.blit(boundsText, (10, 50))
        g.screen.blit(coordinates, (690, 10))
    if g.fullscreen == False:
        fullscreenText = g.gameFont.render("Fullg.screen: OFF", True, g.colors.get("OFF"))
        g.screen.blit(fullscreenText, (10, 70))
    elif fullg.screen == True:
        fullg.screenText = g.gameFont.render("Fullg.screen: ON", True, g.colors.get("ON"))
        g.screen.blit(fullscreenText, (10, 70))
    keysText = g.creditFont.render("Keys: ARROWS, WASD, KP +-, B, F10, F11.", True, g.colors.get("GAME"))
    creditText = g.creditFont.render("Developed by Ericson Willians.", True, g.colors.get("GAME"))
    g.screen.blit(scoreText,(10,10))
    g.screen.blit(speedText,(10,30))
    g.screen.blit(keysText,(10,750))
    g.screen.blit(creditText,(620,750))
    pygame.display.flip()
    g.clock.tick(snake.speed)

print "Exiting..."
pygame.quit()