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

import _global
import pygame

def drawGameHud(_snake):

	score_text = _global._game_font.render("Score: " + str(_global.score),
		True, _global.colors.get("GAME"))

	speed_text = _global._game_font.render("Speed: " + str(_snake.speed),
		True, _global.colors.get("GAME"))

	if _global.bounds == True:
		bounds_text = _global._game_font.render("Bounds: ON",
						True, _global.colors.get("ON"))
		_global._screen.blit(bounds_text, (10, 50))

	elif _global.bounds == False:
		bounds_text = _global._game_font.render("Bounds: OFF",
			True, _global.colors.get("OFF"))
		try:
			coordinates = _global._game_font.render("x: " +
					str(_snake.length[len(_snake.length)-1][0]) +
					" " +
					"y: " +
					str(_snake.length[len(_snake.length)-1][1]),
				True, _global.colors.get("OFF"))
		except IndexError, v:
			print "IndexError:", v
		_global._screen.blit(boundsText, (10, 50))
		_global._screen.blit(coordinates, (690, 10))

	if _global.fullscreen == False:
		fullscreen_text = _global._game_font.render("Fullscreen: OFF",
			True, _global.colors.get("OFF"))
		_global._screen.blit(fullscreen_text, (10, 70))

	elif fullscreen == True:
		fullscreen_text = _global._game_font.render("Fullscreen: ON",
			True, _global.colors.get("ON"))
		_global._screen.blit(fullscreen_text, (10, 70))

	step_text = _global._game_font.render("Step: " + str(_snake.step),
			True, _global.colors.get("GAME"))
	_global._screen.blit(step_text, (10, 90))

	keys_text = _global._credit_font.render("Keys: ARROWS, WASD, KP +-, B, F10, F11.",
		True, _global.colors.get("GAME"))
	credit_text = _global._credit_font.render("Developed by Ericson Willians.",
		True, _global.colors.get("GAME"))

	_global._screen.blit(score_text,(10,10))
	_global._screen.blit(speed_text,(10,30))
	_global._screen.blit(keys_text,(10,750))
	_global._screen.blit(credit_text,(620,750))
