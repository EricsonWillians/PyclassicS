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

import _global
from food import Food
from snake import Snake

_snake = Snake(Food())

def key_pressed(input_key):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[input_key]:
        return True
    else:
        return False

while not _global.done:

    for e in pygame.event.get():

        if e.type == pygame.QUIT or key_pressed(pygame.K_ESCAPE):
            _global.done = True

        if key_pressed(pygame.K_p) and pause == False:
            pause = True
            print "Paused Game."

        elif key_pressed(pygame.K_p) and pause == True:
            pause = False
            print "Game resumed..."

        if key_pressed(pygame.K_F10):
            _global.screen = pygame.display.set_mode(
                                (_global.screenSize,
                                 _global.screenSize),
                                 pygame.FULLg.screen)
            fullscreen = True

        if key_pressed(pygame.K_F11):
            _global.screen = pygame.display.set_mode((_global.screenSize,
                                                      _global.screenSize))
            fullscreen = False

        if (key_pressed(pygame.K_UP)
                or key_pressed(pygame.K_w)):
            snake.dir = _global.directions[0]

        if (key_pressed(pygame.K_DOWN)
                or key_pressed(pygame.K_s)):
            snake.dir = _global.directions[1]

        if (key_pressed(pygame.K_LEFT)
                or key_pressed(pygame.K_a)):
            snake.dir = _global.directions[2]

        if (key_pressed(pygame.K_RIGHT)
                or key_pressed(pygame.K_d)):
            snake.dir = _global.directions[3]

        if key_pressed(pygame.K_KP_MINUS):
            snake.speed /= 2

        if key_pressed(pygame.K_KP_PLUS):
            snake.speed *= 2

        if (key_pressed(pygame.K_b)
                and (g.bounds == True)):
            _global.bounds = False

        elif (key_pressed(pygame.K_b)
                and (_global.bounds == False)):
            _global.bounds = True

    pygame.draw.rect(
        _global._screen,
        _global.colors.get("BG"),
        (0,0,_global.screen_size,_global.screen_size))

    if _global.pause == False:
        try:
            snake.give_life()
        except:
            if _global.bounds == True:
                _snake.length = [
                               [24, 24],
                               [24, 23],
                ]
            else:
                pass

    scoreText = _global._game_font.render("Score: " + str(_global.score), True, _global.colors.get("GAME"))
    speedText = _global._game_font.render("Speed: " + str(_snake.speed), True, _global.colors.get("GAME"))
    if _global.bounds == True:
        boundsText = _global._game_font.render("Bounds: ON", True, _global.colors.get("ON"))
        _global._screen.blit(boundsText, (10, 50))
    elif bounds == False:
        boundsText = _global._game_font.render("Bounds: OFF", True, _global.colors.get("OFF"))
        coordinates = _global._game_font.render("x: " + str(snake.length[len(_snake.length)-1][0]) + " " + "y: " + str(snake.length[len(snake.length)-1][1]), True, colors.get("OFF"))
        _global._screen.blit(boundsText, (10, 50))
        _global._screen.blit(coordinates, (690, 10))
    if _global.fullscreen == False:
        fullscreenText = _global._game_font.render("Fullg.screen: OFF", True, _global.colors.get("OFF"))
        _global._screen.blit(fullscreenText, (10, 70))
    elif fullg._screen == True:
        fullg.screenText = _global._game_font.render("Fullg.screen: ON", True, _global.colors.get("ON"))
        _global._screen.blit(fullscreenText, (10, 70))
    keysText = _global._credit_font.render("Keys: ARROWS, WASD, KP +-, B, F10, F11.", True, _global.colors.get("GAME"))
    creditText = _global._credit_font.render("Developed by Ericson Willians.", True, _global.colors.get("GAME"))
    _global._screen.blit(scoreText,(10,10))
    _global._screen.blit(speedText,(10,30))
    _global._screen.blit(keysText,(10,750))
    _global._screen.blit(creditText,(620,750))
    pygame.display.flip()
    _global._clock.tick(_snake.speed)

print "Exiting..."
pygame.quit()