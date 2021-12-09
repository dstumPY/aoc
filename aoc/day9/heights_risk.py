"""Solution for day 9 puzzle (see https://adventofcode.com/2021/day/9)."""
from itertools import product
from typing import List, Tuple

import numpy as np

from aoc.io.data_load import load_input_day9

HEIGHTS_MAP = load_input_day9()


def get_adjacent(local_pos: Tuple[int, int]) -> Tuple[int, int]:
    """Generate adjacent positions for given local position.

    Arguments:
        local_pos {Tuple[int, int]} -- local position

    Returns:
        Tuple[int, int] -- result adjacents for local_pos
    """
    x, y = local_pos
    adjacents: list = []

    # iterate through all adjacent directions
    for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:

        # calculate adjacent positions
        dx = x + direction[0]
        dy = y + direction[1]

        # prevent adjacent positions crossing the
        # borders (top and left)
        if (dx < 0) or (dy < 0):
            continue

        # add all adjacents
        try:
            adjacents.append(HEIGHTS_MAP[dx][dy])
        except IndexError:
            continue

    return adjacents


def get_enviroment(local_pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Find adjacent for a given position except adjacents with height 9.

    Arguments:
        local_pos {Tuple[int, int]} -- local position to look for adjacents

    Returns:
        List[Tuple[int, int]] -- adjacents results
    """
    x, y = local_pos
    adjacents_positions: list = []

    # iterate through all adjacent directions
    for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:

        # calculate adjacent position
        dx = x + direction[0]
        dy = y + direction[1]

        # prevent adjacent positions crossing the
        # borders (top and left)
        if (dx < 0) or (dy < 0):
            continue

        # add all adjacents except max adjacents with height 9
        try:
            if HEIGHTS_MAP[dx][dy] != 9:
                adjacents_positions.append((dx, dy))
        except IndexError:
            continue

    return adjacents_positions


def get_basin(low_position: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Generate all basin values for a given local low position.

    A basin is an environment close to a local minimum which has
    heights less than 9. All environmental basin positions are
    located next to each other and connected.

    Arguments:
        low_position {Tuple[int, int]} -- local position to search
                                        a basin environment

    Returns:
        List[Tuple[int,int]] -- basin positions for a given low position
    """

    # define list wich collects already visited and unvisited positions
    visited = []
    unvisited = [low_pos]

    # look at every unvisited position and add resulting unseen adjacents
    # ( with height < 9) to the list of unvisited positions until this
    # list is empty
    while len(unvisited) > 0:

        # get last-added unseen position
        local_pos = unvisited.pop()

        # get adjacents for new local position, then add it to visited
        adjacent_positions = get_enviroment(local_pos=local_pos)
        visited.append(local_pos)

        # add only new adjacents to unvisited that are not already visited
        # or already contained
        unvisited.extend(set(adjacent_positions) - set(visited) - set(unvisited))

    return visited


## PART1

# result coordinates and height values list
lowest_positions = []
lowest_heights = []

# Iterate through all input height positions and find all adjacents.
# If a local coordinate is smaller than all adjacent positions a new
# minimum is found.
for pos_x, pos_y in product(range(len(HEIGHTS_MAP)), range(100)):

    # get adjacents and height for given coordinate
    current_adjacents = get_adjacent(local_pos=(pos_x, pos_y))
    current_height = HEIGHTS_MAP[pos_x][pos_y]

    # test for minimum condition
    if current_height < min(current_adjacents):
        lowest_positions.append((pos_x, pos_y))
        lowest_heights.append(current_height)

# Task: Find risk level which is defined as sum over all heights of
# minimal coordinates plus 1
print(
    f"Solution PART1: The risk level is given by ",
    sum(lowest_heights) + len(lowest_heights),
)


## PART2

# loop over all lowest positions
basin_collection = {}
for low_pos in lowest_positions:

    # get basin for local low position
    basin = get_basin(low_position=low_pos)
    basin_collection[low_pos] = basin

# sort basin by number of coordinates
basin_sorted = sorted(basin_collection.items(), key=lambda x: len(x[1]))

# get top 3 basin sizes
top_3_basin_sizes = [len(i[1]) for i in basin_sorted][-3:]

print(f"Solution PART2: {np.product(top_3_basin_sizes)} with sizes {top_3_basin_sizes}")
