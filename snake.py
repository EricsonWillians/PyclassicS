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

import _global
import pygame

class Snake():

    def __init__(self, food):

        self.speed = 16
        self.size = 16
        self.dir = _global.directions[0]
        self.grid_index = []
        self.real_pos = []
        for i in range(0, 48):
            self.grid_index.append(i)
            self.real_pos.append(i*16)
        self.grid_keys = dict(zip(self.grid_index,self.real_pos))
        self.length = [
                      [24, 24],
                      [24, 24],
        ]

        self.food = food
        self.step = 1

    def draw(self):

        map(lambda tail: pygame.draw.rect(
                _global._screen,
                _global.colors.get("GAME"),
                (self.grid_keys.get(tail[0]),
                 self.grid_keys.get(tail[1]),
                 self.size,self.size)),
            [tail for tail in self.length])

    # Defaults the whole game when Death comes.
    def default(self):

        del self.length[:]
        self.food.respawn()
        _global.score = 0
        print "GAME OVER!\n"*100

    # An abstract method that makes the snake the snake.
    def give_life(self):

        self.length.pop()
        next = self.length[0]

        pygame.draw.rect(
                _global._screen,
                _global.colors.get("GAME"),
            (self.grid_keys.get(self.food.pos[0]),
             self.grid_keys.get(self.food.pos[1]),self.size,self.size))

        self.draw()
        print str(self.length).replace('[','').replace(']','').replace(', ','-'+str(len(self.length))+'-').replace('(','[').replace(')',']')

        if self.dir == "NORTH":
            if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_KP0]:
                next = (next[0], next[1]-self.step)
            else:
                next = (next[0], next[1]-1)
            if ((next[0] == self.food.pos[0])
                    and (next[1] == self.food.pos[1])):
                self.length.append((self.length[len(self.length)-1][0],
                    self.length[len(self.length)-1][1]-1))
                self.food.respawn()
                _global.score += 1

        elif self.dir == "SOUTH":
            if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_KP0]:
                next = (next[0],next[1]+self.step)
            else:
                next = (next[0],next[1]+1)
            if ((next[0] == self.food.pos[0])
                    and (next[1] == self.food.pos[1])):
                self.length.append((self.length[len(self.length)-1][0],
                    self.length[len(self.length)-1][1]+1))
                self.food.respawn()
                _global.score += 1

        elif self.dir == "WEST":
            if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_KP0]:
                next = (next[0]-self.step, next[1])
            else:
                next = (next[0]-1, next[1])
            if ((next[0] == self.food.pos[0])
                    and (next[1] == self.food.pos[1])):
                self.length.append((self.length[len(self.length)-1][0]-1,
                    self.length[len(self.length)-1][1]))
                self.food.respawn()
                _global.score += 1

        elif self.dir == "EAST":
            if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_KP0]:
                next = (next[0]+self.step, next[1])
            else:
                next = (next[0]+1, next[1])
            if ((next[0] == self.food.pos[0])
                    and (next[1] == self.food.pos[1])):
                self.length.append((self.length[len(self.length)-1][0]+1,
                    self.length[len(self.length)-1][1]))
                self.food.respawn()
                _global.score += 1

        if _global.bounds == True:
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
                    if ((next[0] == i[0])
                        and (next[1] == i[1])):
                        self.default()

            self.length.insert(0, next)

        if pygame.key.get_pressed()[pygame.K_KP1]:
            self.step = 1
        if pygame.key.get_pressed()[pygame.K_KP2]:
            self.step = 2
        if pygame.key.get_pressed()[pygame.K_KP3]:
            self.step = 3
        if pygame.key.get_pressed()[pygame.K_KP4]:
            self.step = 4
        if pygame.key.get_pressed()[pygame.K_KP5]:
            self.step = 5
        if pygame.key.get_pressed()[pygame.K_KP6]:
            self.step = 6
        if pygame.key.get_pressed()[pygame.K_KP7]:
            self.step = 7
        if pygame.key.get_pressed()[pygame.K_KP8]:
            self.step = 8
        if pygame.key.get_pressed()[pygame.K_KP9]:
            self.step = 9
