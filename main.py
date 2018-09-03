# main.py
# Written by Michael Gallagher <mcgallag@gmail.com>
# Copyright 2018, Michael Gallagher

# This file is part of IsaacMapper.
#
# IsaacMapper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# IsaacMapper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with IsaacMapper.  If not, see <https://www.gnu.org/licenses/>.

import pathlib
import pygame
from ResourceHandler import ResourceHandler
from Map import Map
import Room

pygame.init()

size = width, height = 1024, 768
black = 200, 200, 200

screen = pygame.display.set_mode(size)
menu = pygame.Surface(size)
menu.fill((255, 0, 0))

rh = ResourceHandler(pathlib.Path("images"))
game_map = Map(Room.Room(1, 1, rh))

running = True
map_draw = True
menu_draw = False

while running:
    dx = 0
    dy = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                continue
            elif event.key == pygame.K_DOWN:
                dy -= 1
            elif event.key == pygame.K_UP:
                dy += 1
            elif event.key == pygame.K_LEFT:
                dx += 1
            elif event.key == pygame.K_RIGHT:
                dx -= 1
            elif event.key == pygame.K_w:
                game_map.start.open_exit(Room.Up)
            elif event.key == pygame.K_a:
                game_map.start.open_exit(Room.Left)
            elif event.key == pygame.K_s:
                game_map.start.open_exit(Room.Down)
            elif event.key == pygame.K_d:
                game_map.start.open_exit(Room.Right)
            elif event.key == pygame.K_SPACE:
                map_draw = not map_draw
                menu_draw = not menu_draw

    if map_draw:
        screen.fill(black)
        game_map.draw(screen, rh)
        if dx != 0 or dy != 0:
            print("({0},{1})".format(dx, dy))
            game_map.move(dx, dy)
    elif menu_draw:
        screen.blit(menu, (0, 0))

    pygame.display.flip()
    pygame.time.delay(1000 // 60)
