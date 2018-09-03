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

Left = 0
Right = 1
Up = 2
Down = 3


class Room:
    def __init__(self, x, y, resource_handler):
        self.x = x
        self.y = y
        self.rh = resource_handler
        self.name = "Room"
        self.background = resource_handler.get("room_background_empty")
        self.exits = {
            Left: True,
            Right: None,
            Up: None,
            Down: None
        }
        self.bombs = {
            Left: None,
            Right: None,
            Up: None,
            Down: None
        }

    def open_exit(self, direction):
        if self.exits[direction] is not None:
            self.exits[direction] = None
        else:
            self.exits[direction] = True
