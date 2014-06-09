"""

====================================================================

PyclassicS 1.2 - Snake Game
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

import sys
import pygame

import _global
import gui
from food import Food
from snake import Snake

_snake = Snake(Food())

while not _global.done:

    if pygame.key.get_pressed()[pygame.K_p] and pause == False:
            pause = True
            print "Paused Game."

    elif pygame.key.get_pressed()[pygame.K_p] and pause == True:
        pause = False
        print "Game resumed..."

    if pygame.key.get_pressed()[pygame.K_F10]:
        _global.screen = pygame.display.set_mode(
                            (_global.screen_size,
                             _global.screen_size),
                             pygame.FULLSCREEN)
        fullscreen = True

    if pygame.key.get_pressed()[pygame.K_F11]:
        _global.screen = pygame.display.set_mode((_global.screenSize,
                                                  _global.screenSize))
        fullscreen = False

    if (pygame.key.get_pressed()[pygame.K_UP]
            or pygame.key.get_pressed()[pygame.K_w]):
        _snake.dir = _global.directions[0]

    if (pygame.key.get_pressed()[pygame.K_DOWN]
            or pygame.key.get_pressed()[pygame.K_s]):
        _snake.dir = _global.directions[1]

    if (pygame.key.get_pressed()[pygame.K_LEFT]
            or pygame.key.get_pressed()[pygame.K_a]):
        _snake.dir = _global.directions[2]

    if (pygame.key.get_pressed()[pygame.K_RIGHT]
            or pygame.key.get_pressed()[pygame.K_d]):
        _snake.dir = _global.directions[3]

    if pygame.key.get_pressed()[pygame.K_KP_MINUS]:
        _snake.speed /= 2

    if pygame.key.get_pressed()[pygame.K_KP_PLUS]:
        _snake.speed *= 2

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        _global.done = True

    if (pygame.key.get_pressed()[pygame.K_b]
            and (_global.bounds == True)):
        _global.bounds = False

    elif (pygame.key.get_pressed()[pygame.K_b]
            and (_global.bounds == False)):
        _global.bounds = True

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            _global.done = True

    pygame.draw.rect(
        _global._screen,
        _global.colors.get("BG"),
        (0,0,_global.screen_size,_global.screen_size))


    if _global.pause == False:
        try:
            _snake.give_life()
        except:
            if _global.bounds == True:
                _snake.length = [
                                [24, 24],
                                [24, 24],
                ]
            else:
                pass

    gui.drawGameHud(_snake)
    
    pygame.display.flip()
    _global._clock.tick(_snake.speed)

print "Exiting..."
pygame.quit()
