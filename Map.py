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


class Map:
    def __init__(self, start):
        self.rooms = [start]
        self.width = 1
        self.height = 1
        self.start = start
        self.start.background = self.start.rh.get("room_background_origin")

    def draw(self, screen, rh):
        width = screen.get_width()
        height = screen.get_height()

        for room in self.rooms:
            # 1, 1   -----> width // 2 - 16  , height // 2 - 16
            # TODO - Make sure this works for multiple rooms
            (x, y) = room.x, room.y
            drawx = width // 2 - 16 + ((x-1) * 32)
            drawy = height // 2 - 16 + ((y-1) * 32)
            subscreen_rect = pygame.Rect(drawx, drawy, 32, 32)
            rh.draw_room(screen.subsurface(subscreen_rect), room)

    def move(self, dx, dy):
        for room in self.rooms:
            room.x += dx
            room.y += dy
