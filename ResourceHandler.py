# ResourceHandler.py
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

import Room
import pygame
import pathlib


class ResourceHandler:
    def __init__(self, path):
        self.images = {}
        self.__loadimages(path)

    def get(self, string_id):
        return self.images[string_id]

    def __loadimages(self, path):
        for file in path.iterdir():
            base_name = file.stem
            img = pygame.image.load(str(file))
            self.images[base_name] = img

    def draw_room(self, screen, room):
        key = "room"
        if room.exits[Room.Left] is None:
            key += "0"
        else:
            key += "1"
        if room.exits[Room.Right] is None:
            key += "0"
        else:
            key += "1"
        if room.exits[Room.Up] is None:
            key += "0"
        else:
            key += "1"
        if room.exits[Room.Down] is None:
            key += "0"
        else:
            key += "1"
        screen.blit(self.get(key), (0, 0))
        screen.blit(room.background, (0, 0))


# rh = ResourceHandler(pathlib.Path("/home/mike/src/isaacmapper2/images"))
# img = rh.images["bomb0100"]
