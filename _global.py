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

import pygame

pygame.init()
_clock = pygame.time.Clock()
screen_size = 768
_screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("PyclassicS 1.2")
fullscreen = False
_game_font = pygame.font.SysFont("helvetica", 16, True)
_credit_font = pygame.font.SysFont("helvetica", 10, True)
done = False
pause = False
bounds = True # Enable "death" when outside the screen's boundaries.

colors = {"BG": (0,0,0), "GAME": (255,255,255), "ON": (0,255,0), "OFF": (255,0,0)}
directions = ["NORTH","SOUTH","WEST","EAST"]
score = 0