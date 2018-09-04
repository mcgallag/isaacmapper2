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
        screen.set_alpha(room.alpha)
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

        # bombs
        key = "bomb"
        key += "1" if room.bombs[Room.Left] else "0"
        key += "1" if room.bombs[Room.Right] else "0"
        key += "1" if room.bombs[Room.Up] else "0"
        key += "1" if room.bombs[Room.Down] else "0"
        if key != "bomb0000":
            screen.blit(self.get(key), (0, 0))

        screen.blit(room.background, (0, 0))

        dimmer = pygame.Surface(screen.get_size())
        dimmer.fill((0, 0, 0))
        dimmer.set_alpha(room.alpha)
        old_clip = screen.get_clip()
        screen.blit(dimmer, (0, 0))
        screen.set_clip(old_clip)

# rh = ResourceHandler(pathlib.Path("/home/mike/src/isaacmapper2/images"))
# img = rh.images["bomb0100"]
