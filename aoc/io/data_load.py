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

def load_input_day6() -> list:
    """Load and process the input data.

    Returns:
        list -- lanternfish ages
    """
    # locate file
    FILE = PUZZLE_INPUT_FOLDER / 'day6_input_data.txt'

    # read file
    with FILE.open('r') as fh:
        lines = fh.readline()

        # clean input from newlines, split by comma and cast values to int
        lines = [int(lanternfish) for lanternfish in lines.strip('\n').split(',')]

    return lines


def load_input_day7() -> list:
    """Load and process the input data.

    Returns:
        list -- crab positions
    """
    # locate file
    FILE = PUZZLE_INPUT_FOLDER / 'day7_input_data.txt'

    # read file
    with FILE.open('r') as fh:
        lines = fh.readline()

        # clean input from newlines, split by comma and cast values to int
        lines = [int(lanternfish) for lanternfish in lines.strip('\n').split(',')]

    return lines


def load_input_day8() -> Tuple[List[str], List[str]]:
    """Load and process input data.

    Returns:
        Tuple[List[str], List[str]]: signals and output splitted 
                                    into different lists.
    """
    # locate file
    FILE = PUZZLE_INPUT_FOLDER / "day8_input_data.txt"

    # read file
    lines = FILE.open('r').readlines()

    head_list = []
    tail_list = []
    for line in lines:

        # split lines at "|" character
        head, tail = line.strip("\n").split(" | ")
        head_list.append(head.split(" "))
        tail_list.append(tail.split(" "))

    return head_list, tail_list


def load_input_day9() -> List[List[int]]:
    """Generate a height map based on an digit input file.

    Returns:
        List[List[int]] -- Separated int heights extracted
                            from input file.
    """
    # locate file
    FILE = PUZZLE_INPUT_FOLDER / "day9_input_data.txt"

    # read file
    with FILE.open("r") as fh:
        lines = fh.readlines()
        lines = [list(line.strip("\n")) for line in lines]
        height_map = [[int(digit_str) for digit_str in line] for line in lines]

    return height_map
