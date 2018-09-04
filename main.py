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

size = width, height = 800, 600
black = 200, 200, 200

screen = pygame.display.set_mode(size)
menu = pygame.Surface(size)
menu.fill((255, 0, 0))

rh = ResourceHandler(pathlib.Path("images"))
game_map = Map(Room.Room(0, 0, rh), rh)
current_room = game_map.start
current_room.highlight(True)

running = True
map_draw = True
menu_draw = False

EXITMODE = 1
BOMBMODE = 2
wasd_mode = EXITMODE

while running:
    dx = 0
    dy = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                if not pygame.key.get_mods() & pygame.KMOD_CAPS:
                    wasd_mode = BOMBMODE if wasd_mode == EXITMODE else EXITMODE
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_mods() & pygame.KMOD_CAPS:
                wasd_mode = BOMBMODE
            if event.key == pygame.K_ESCAPE:
                running = False
                continue
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                wasd_mode = BOMBMODE
            elif event.key == pygame.K_DOWN:
                dy -= 1
            elif event.key == pygame.K_UP:
                dy += 1
            elif event.key == pygame.K_LEFT:
                dx += 1
            elif event.key == pygame.K_RIGHT:
                dx -= 1
            elif event.key == pygame.K_w:
                game_map.toggle_room_exit(current_room, Room.Up, wasd_mode)
            elif event.key == pygame.K_a:
                game_map.toggle_room_exit(current_room, Room.Left, wasd_mode)
            elif event.key == pygame.K_s:
                game_map.toggle_room_exit(current_room, Room.Down, wasd_mode)
            elif event.key == pygame.K_d:
                game_map.toggle_room_exit(current_room, Room.Right, wasd_mode)
            elif event.key == pygame.K_SPACE:
                current_room.debug()

    if map_draw:
        screen.fill(black)
        game_map.draw(screen, rh)
        if dx != 0 or dy != 0:
            game_map.move(dx, dy)
            current_room.highlight()
            current_room = current_room.move((-dx, -dy))
            current_room.highlight()
    elif menu_draw:
        screen.blit(menu, (0, 0))

    pygame.display.flip()
    pygame.time.delay(1000 // 60)
