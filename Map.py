# Map.py
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
import pygame
from Room import Room


class Map:
    def __init__(self, start, rh):
        self.rooms = [start]
        self.rh = rh
        self.width = 1
        self.height = 1
        self.start = start
        self.start.background = self.start.rh.get("room_background_origin")

    def draw(self, screen, rh):
        width = screen.get_width()
        height = screen.get_height()

        for room in self.rooms:
            # 0, 0   -----> width // 2 - 16  , height // 2 - 16
            (x, y) = room.x, room.y
            drawx = width // 2 - 16 + (x * 32)
            drawy = height // 2 - 16 + (y * 32)
            subscreen_rect = pygame.Rect(drawx, drawy, 32, 32)
            rh.draw_room(screen.subsurface(subscreen_rect), room)

    def move(self, dx, dy):
        for room in self.rooms:
            room.x += dx
            room.y += dy

    def mirror(self, direction):
        mx = -1 * direction[0]
        my = -1 * direction[1]
        return mx, my

    def add_room(self, source_room, direction):
        newx, newy = source_room.translate(direction)
        new_room = Room(newx, newy, self.rh)
        source_room.exits[direction] = new_room
        source_room.bombs[direction] = False
        new_room.exits[self.mirror(direction)] = source_room
        self.rooms.append(new_room)

    def toggle_room_exit(self, source_room, direction, wasd_mode):
        EXITMODE = 1
        BOMBMODE = 2

        if wasd_mode == EXITMODE:
            if source_room.exits[direction] is None:
                self.add_room(source_room, direction)
            else:
                deleted_room = source_room.remove_exit(direction)
                self.rooms.remove(deleted_room)
        elif wasd_mode == BOMBMODE:
            source_room.bombs[direction] = not source_room.bombs[direction]
