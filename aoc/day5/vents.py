"""Solution for day 5 puzzle (see https://adventofcode.com/2021/day/5)"""
from collections import Counter
from typing import List, Tuple

from aoc.config import PUZZLE_INPUT_FOLDER


def load_input_day5() -> list:
    """Load and process the input data.

    Returns:
        list -- List directions given by [(from_x, from_y) (to_x, to_y)]
    """    
    file = PUZZLE_INPUT_FOLDER / "day5_input_data.txt"

    # load complete input file
    with file.open("r") as fh:
        lines = fh.readlines()

    # remove newlines
    lines = [line.strip("\n") for line in lines]

    result = []
    for line in lines:
        # split at ' -> ' character
        vent_from, vent_to = line.split(" -> ")

        # extract coordinates by splitting at ','
        # and converting to int
        from_x = int(vent_from.split(",")[0])
        from_y = int(vent_from.split(",")[1])

        to_x = int(vent_to.split(",")[0])
        to_y = int(vent_to.split(",")[1])

        result.append([(from_x, from_y), (to_x, to_y)])

    return result


def get_horizontal_vertical_vents(
    from_tuple: Tuple[int, int], to_tuple: Tuple[int, int]
) -> List[int]:
        """Explode horizontal and vertical directions to coordiante sequence.

        Example:
        Given directions as (9,7) -> (9,5) will be exploded to [(9,7), (9,6), (9,5)]

        Arguments:
            from_tuple {Tuple[int, int]} -- Tuple the vent starts from.
            to_tuple {Tuple[int, int]} -- Tuple the vent ends.

        Returns:
            List[int] -- Exploded directions given by coordinates.
        """
    from_x, from_y = from_tuple
    to_x, to_y = to_tuple

    # detect diagonals
    if (from_x != to_x) and (from_y != to_y):
        return None

    # detect horizontal or vertical vents
    if from_x == to_x:
        # calculate difference and iteration steps
        diff = to_y - from_y
        it_steps = range(diff + 1) if diff > 0 else [-i for i in range(-diff + 1)]

        vent_result = [(from_x, from_y + step) for step in it_steps]

    elif from_y == to_y:
        # calculate difference and iteration steps
        diff = to_x - from_x
        it_steps = range(diff + 1) if diff > 0 else [-i for i in range(-diff + 1)]

        vent_result = [(from_x + step, from_y) for step in it_steps]

    return vent_result


def get_all_vents(from_tuple: Tuple[int, int], to_tuple: Tuple[int, int]) -> List[int]:
    """Similar to get_horizontal_vertical_vents explode directions (incl. diagonals).

    Example:    
    Given directions as (9,7) -> (7,9) will be exploded to [(9,7), (8,8), (7,9)]

    Arguments:
        from_tuple {Tuple[int, int]} -- Tuple the vent starts from.
        to_tuple {Tuple[int, int]} -- Tuple the vent ends.

    Returns:
        Returns:
            List[int] -- Exploded directions given by coordinates.
    """    
    from_x, from_y = from_tuple
    to_x, to_y = to_tuple

    # detect diagonals
    if (from_x != to_x) and (from_y != to_y):
        diff_x = to_x - from_x
        diff_y = to_y - from_y

        it_steps_x = (
            range(diff_x + 1) if diff_x > 0 else [-i for i in range(-diff_x + 1)]
        )
        it_steps_y = (
            range(diff_y + 1) if diff_y > 0 else [-i for i in range(-diff_y + 1)]
        )

        vent_result = [
            (from_x + step_x, from_y + step_y)
            for step_x, step_y in zip(it_steps_x, it_steps_y)
        ]

    # detect horizontal or vertical vents
    elif from_x == to_x:
        # calculate difference and iteration steps
        diff = to_y - from_y
        it_steps = range(diff + 1) if diff > 0 else [-i for i in range(-diff + 1)]

        vent_result = [(from_x, from_y + step) for step in it_steps]

    elif from_y == to_y:
        # calculate difference and iteration steps
        diff = to_x - from_x
        it_steps = range(diff + 1) if diff > 0 else [-i for i in range(-diff + 1)]

        vent_result = [(from_x + step, from_y) for step in it_steps]

    return vent_result


# Load input data
vent_data = load_input_day5()

## PART 1

# explode vent encodings to complete lines
exploded_vents = []
for item in vent_data:

    # return complete vent for horizontal and vertical
    # input directions [(from_x, from_y),(to_x, to_y)]
    straight_line = get_horizontal_vertical_vents(*item)

    if straight_line:
        exploded_vents.extend(straight_line)


straights = Counter(exploded_vents)
crossed_vents = {key: value for key, value in straights.items() if value >= 2}
print("Result part 1 (for only horizontal and vertical vents):", len(crossed_vents))

## PART 2

# go on including also diagonal vents
# explode vent encodings to complete lines
all_vents = []
for item in vent_data:

    # return complete vent for ALL horizontal, vertical and diagonal
    # input directions [(from_x, from_y),(to_x, to_y)]
    straight_line = get_all_vents(*item)

    if straight_line:
        all_vents.extend(straight_line)

all_directions = Counter(all_vents)
crossed_vents = {key: value for key, value in all_directions.items() if value >= 2}
print("Result part 1 (for only horizontal and vertical vents):", len(crossed_vents))
