# Room.py
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

Left = (-1, 0)
Right = (1, 0)
Up = (0, -1)
Down = (0, 1)


class Room:
    def __init__(self, x, y, resource_handler):
        self.x = x
        self.y = y
        self.rh = resource_handler
        self.name = "Room"
        self.background = resource_handler.get("room_background_empty")
        self.exits = {
            Left: None,
            Right: None,
            Up: None,
            Down: None
        }
        self.bombs = {
            Left: False,
            Right: False,
            Up: False,
            Down: False
        }
        self.open_walls = {
            Left: False,
            Right: False,
            Up: False,
            Down: False
        }
        self.alpha = 96
        self.linkedrooms = []

    def is_linked(self):
        return len(self.linkedrooms) > 0

    def add_link(self, room):
        for link in self.linkedrooms:
            link.linkedrooms.append(room)
            room.linkedrooms.append(link)
        self.linkedrooms.append(room)
        room.linkedrooms.append(self)

    def num_open_walls(self):
        num = 0
        for wall in self.open_walls.values():
            if wall:
                num += 1
        return num

    def highlight(self, select=None):
        """
        Toggles highlighting on for room.
        :param select: optional boolean specifying highlight status, acts as toggle if omitted
        :return:
        """
        dim_alpha = 96
        if select is not None:
            if select:
                self.alpha = 0
            else:
                self.alpha = dim_alpha
        else:
            self.alpha = dim_alpha if self.alpha == 0 else 0
        for room in self.linkedrooms:
            room.alpha = self.alpha

    def debug(self):
        print("Room")
        print("X: {0}".format(self.x))
        print("Y: {0}".format(self.y))
        exits = "Exits: "
        exits += "1" if self.exits[Left] is not None else "0"
        exits += "1" if self.exits[Right] is not None else "0"
        exits += "1" if self.exits[Up] is not None else "0"
        exits += "1" if self.exits[Down] is not None else "0"
        print(exits)
        bombs = "Bombs: "
        bombs += "1" if self.bombs[Left] else "0"
        bombs += "1" if self.bombs[Right] else "0"
        bombs += "1" if self.bombs[Up] else "0"
        bombs += "1" if self.bombs[Down] else "0"
        print(bombs)

    def translate(self, direction):
        """
        Returns the map (x, y) coordinates if we were to move in this direction.
        Does not perform any actual movement
        :param direction: one of Left, Right, Up, Down constants
        :return: (x, y) coordinates of the resulting movement
        """
        newx = self.x + direction[0]
        newy = self.y + direction[1]
        return newx, newy

    def can_move(self, direction):
        """
        Tests if a move in direction is possible
        :param direction: one of Left, Right, Up, Down constants
        :return: True if a move is possible
        """
        return self.exits[direction] is not None

    def move(self, direction):
        """
        Returns the room located in exit direction
        :param direction: one of Left, Right, Up, Down constants
        :return: Room located in direction
        """
        if self.exits[direction] is not None:
            return self.exits[direction]
        else:
            return self

    def remove_exit(self, direction):
        r = self.exits[direction]
        self.exits[direction] = None
        return r
