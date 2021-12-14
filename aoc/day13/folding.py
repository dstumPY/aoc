"""Solution for day 13 puzzle (see https://adventofcode.com/2021/day/13)."""
from itertools import product
from typing import List

from aoc.day11.glowing_octopus import Point
from aoc.io.data_load import load_input_data13


class PaperPoints:
    def __init__(self, raw_input):
        """Generate PaperPoint board.

        Args:
            raw_input ([type]): Coordinates of points according to
            puzzle description.
        """
        self.width = max(line[0] for line in raw_input)
        self.height = max(line[1] for line in raw_input)

        # first set "." globally, then "#" for raw_input
        self.board = {}
        for item in product(range(self.width + 1), range(self.height + 1)):
            self.board[item] = Point(item[0], item[1], ".")
        for item in raw_input:
            self.board[item] = Point(item[0], item[1], "#")


        # store number of
        self.number_dot = len(self.get_dots())
        self.number_sharp = len(self.get_sharps())

    def __repr__(self) -> str:
        """Visualize board.

        Returns:
            str: concatenation of single board lines
        """
        lines = ""
        for y in range(self.height + 1):
            line = ""
            for x in range(self.width + 1):
                line += self.board[(x, y)].value
            lines += line + "\n"
        return lines

    def get_dots(self) -> List[Point]:
        """Generate all board positions with "." as value.

        Returns:
            List[Point]: List of board Points.
        """
        return [i for i in self.board.values() if i.value == "."]

    def get_sharps(self):
        """Generate all board positions with "#" as value.

        Returns:
            List[Point]: List of board Points.
        """
        return [i for i in self.board.values() if i.value == "#"]

    def fold_vertical(self, at_x: int):
        """Fold current board from right to left fold.

        Args:
            at_x (int): x-position to fold at.
        """
        # set new width after folding
        self.width = at_x - 1

        # get remaining points from other fold with "#"
        other_fold = {}
        for key, point in self.board.items():
            if (key[0] > at_x) and (point.value == "#"):
                other_fold[key] = point

        # project points to current rest board to mirrored
        # remaining board
        for key, point in other_fold.items():
            dx = abs(at_x - point.x) * 2
            self.board[(key[0] - dx, key[1])].value = '#'

        # remove points contained at rest board
        droppable_keys = [k for k in self.board.keys() if k[0] >= at_x]
        for key in droppable_keys:
            del self.board[key]

        # set current dots and sharps after folding
        self.number_dot = len(self.get_dots())
        self.number_sharp = len(self.get_sharps())

    def fold_horizontal(self, at_y: int):
        """Fold current board from bottom to uppper fold.

        Args:
            at_x (int): y-position to fold at.
        """
        # set new width after folding
        self.height = at_y - 1

        # get remaining points from other fold with ":"
        other_fold = {}
        for k, v in self.board.items():
            if (k[1] > at_y) and (v.value == "#"):
                other_fold[k] = v

        # project points to current rest board to mirrored
        # remaining board
        for k, v in other_fold.items():
            dy = abs(at_y - v.y) * 2
            self.board[(k[0], k[1] - dy)].value = "#"

        # remove points contained at rest board
        droppable_keys = [k for k in self.board.keys() if k[1] >= at_y]
        for key in droppable_keys:
            del self.board[key]

        # set current dots and sharps after folding
        self.number_dot = len(self.get_dots())
        self.number_sharp = len(self.get_sharps())


if __name__ == '__main__':
    dot_positions, raw_folding = load_input_data13()

    ## PART1

    x = PaperPoints(dot_positions)
    x.fold_vertical(at_x=655)
    print(f"Solution for PART1:", x.number_sharp)

    ## PART2

    for direction, position in raw_folding[1:]:
        if direction == 'y':
            x.fold_horizontal(at_y=position)
        else:
            x.fold_vertical(at_x=position)
    print(f"Solution for PART2:")
    print(x)
