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
from menu import Menu
import Room
from constants import Direction

pygame.init()

window_size = window_width, window_height = 800, 600

map_size = map_width, map_height = 800, 545

black = 200, 200, 200

window = pygame.display.set_mode(window_size)
map_screen = window.subsurface((0, 0), map_size)
# screen = pygame.display.set_mode(window_size)
menu_bar_screen = window.subsurface((0, 545), (800, 55))

menu_bar = Menu()

rh = ResourceHandler(pathlib.Path("images"))
game_map = Map(Room.Room(0, 0, rh), rh)
current_room = game_map.start
current_room.highlight(True)

running = True
map_draw = True
menu_draw = False

EXITMODE = 1
BOMBMODE = 2
LINKMODE = 3
wasd_mode = EXITMODE


def toggle_wasd_mode(b=None):
    global wasd_mode
    if b is not None:
        if b == EXITMODE:
            wasd_mode = EXITMODE
            menu_bar.highlight(False)
        elif b == BOMBMODE:
            wasd_mode = BOMBMODE
            menu_bar.highlight(True)
    else:
        wasd_mode = BOMBMODE if wasd_mode == EXITMODE else EXITMODE
        menu_bar.highlight()


while running:
    delta = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                if not pygame.key.get_mods() & pygame.KMOD_CAPS:
                    toggle_wasd_mode()
            if event.key == pygame.K_CAPSLOCK:
                toggle_wasd_mode(EXITMODE)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                continue
            elif event.key == pygame.K_CAPSLOCK:
                toggle_wasd_mode(BOMBMODE)
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                if not pygame.key.get_mods() & pygame.KMOD_CAPS:
                    toggle_wasd_mode()
            elif event.key == pygame.K_DOWN:
                delta = Direction.DOWN
            elif event.key == pygame.K_UP:
                delta = Direction.UP
            elif event.key == pygame.K_LEFT:
                delta = Direction.LEFT
            elif event.key == pygame.K_RIGHT:
                delta = Direction.RIGHT
            elif event.key == pygame.K_w:
                game_map.toggle_room_exit(current_room, Direction.UP, wasd_mode)
            elif event.key == pygame.K_a:
                game_map.toggle_room_exit(current_room, Direction.LEFT, wasd_mode)
            elif event.key == pygame.K_s:
                game_map.toggle_room_exit(current_room, Direction.DOWN, wasd_mode)
            elif event.key == pygame.K_d:
                game_map.toggle_room_exit(current_room, Direction.RIGHT, wasd_mode)
            elif event.key == pygame.K_LEFTBRACKET:
                game_map.toggle_room_exit(current_room, Direction.LEFT, LINKMODE)
                # current_room.open_walls[Room.Left] = not current_room.open_walls[Room.Left]
            elif event.key == pygame.K_RIGHTBRACKET:
                game_map.toggle_room_exit(current_room, Direction.RIGHT, LINKMODE)
                # current_room.open_walls[Room.Right] = not current_room.open_walls[Room.Right]
            elif event.key == pygame.K_PAGEUP:
                game_map.toggle_room_exit(current_room, Direction.UP, LINKMODE)
                # current_room.open_walls[Room.Up] = not current_room.open_walls[Room.Up]
            elif event.key == pygame.K_PAGEDOWN:
                game_map.toggle_room_exit(current_room, Direction.DOWN, LINKMODE)
                # current_room.open_walls[Room.Down] = not current_room.open_walls[Room.Down]
            elif event.key == pygame.K_DELETE:
                # TODO - figure out how to delete a room
                pass
            elif event.key == pygame.K_SPACE:
                current_room.debug()

    if map_draw:
        map_screen.fill(black)
        game_map.draw(map_screen, rh)
        menu_bar.draw(menu_bar_screen)
        if delta is not None:
            # check if movement is possible (i.e. a room exits)
            if current_room.can_move(delta):
                current_room.highlight()
                # TODO - make sure this works with delta
                current_room = current_room.move(delta)
                current_room.highlight()
                # TODO - make sure this works with delta
                game_map.move(delta)
    elif menu_draw:
        # TODO - full screen option menu here?
        pass

    pygame.display.flip()
    pygame.time.delay(1000 // 60)

pygame.quit()
