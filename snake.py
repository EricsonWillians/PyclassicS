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

import g
import pygame

class Snake():

    def __init__(self,food):

        self.speed = 16
        self.size = 16
        self.dir = g.directions[0]
        self.gridIndex = []
        self.realPos = []
        for i in range(0,48):
            self.gridIndex.append(i)
            self.realPos.append(i*16)
        self.gridKeys = dict(zip(self.gridIndex,self.realPos))
        self.length = [[24,24],[24,23]]

        self.food = food

    def draw(self):

        map(lambda tail: pygame.draw.rect(g.screen,g.colors.get("GAME"),(self.gridKeys.get(tail[0]),
            self.gridKeys.get(tail[1]),self.size,self.size)),[tail for tail in self.length])

    def default(self): # Defaults the whole game when Death comes.

        del self.length[:]
        self.food.respawn()
        g.score = 0
        print "GAME OVER!\n"*100

    def giveLife(self): # An abstract method that makes the snake the snake.

        global score
        self.length.pop()
        next = self.length[0]
        pygame.draw.rect(g.screen,g.colors.get("GAME"),(self.gridKeys.get(self.food.pos[0]),
            self.gridKeys.get(self.food.pos[1]),self.size,self.size))
        self.draw()
        print "Positions: " + str(self.length)
        if self.dir == "NORTH":
            next = (next[0],next[1]-1)
            if ((next[0] == self.food.pos[0]) and (next[1] == self.food.pos[1])):
                self.length.append((self.length[len(self.length)-1][0],self.length[len(self.length)-1][1]-1))
                self.food.respawn()
                g.score += 1
        elif self.dir == "SOUTH":
            next = (next[0],next[1]+1)
            if ((next[0] == self.food.pos[0]) and (next[1] == self.food.pos[1])):
                self.length.append((self.length[len(self.length)-1][0],self.length[len(self.length)-1][1]+1))
                self.food.respawn()
                g.score += 1
        elif self.dir == "WEST":
            next = (next[0]-1, next[1])
            if ((next[0] == self.food.pos[0]) and (next[1] == self.food.pos[1])):
                self.length.append((self.length[len(self.length)-1][0]-1,self.length[len(self.length)-1][1]))
                self.food.respawn()
                g.score += 1
        elif self.dir == "EAST":
            next = (next[0]+1, next[1])
            if ((next[0] == self.food.pos[0]) and (next[1] == self.food.pos[1])):
                self.length.append((self.length[len(self.length)-1][0]+1,self.length[len(self.length)-1][1]))
                self.food.respawn()
                g.score += 1

        if g.bounds == True:
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