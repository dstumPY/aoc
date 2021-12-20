from typing import List, Tuple
from aoc.config import PUZZLE_INPUT_FOLDER
import re


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
    FILE = PUZZLE_INPUT_FOLDER / "day6_input_data.txt"

    # read file
    with FILE.open("r") as fh:
        lines = fh.readline()

        # clean input from newlines, split by comma and cast values to int
        lines = [int(lanternfish) for lanternfish in lines.strip("\n").split(",")]

    return lines


def load_input_day7() -> list:
    """Load and process the input data.

    Returns:
        list -- crab positions
    """
    # locate file
    FILE = PUZZLE_INPUT_FOLDER / "day7_input_data.txt"

    # read file
    with FILE.open("r") as fh:
        lines = fh.readline()

        # clean input from newlines, split by comma and cast values to int
        lines = [int(lanternfish) for lanternfish in lines.strip("\n").split(",")]

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
    lines = FILE.open("r").readlines()

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


def load_input_day10() -> List[List[str]]:
    """Generate character list based on an input file.

    Returns:
        List[List[str]] -- Separated character list
    """
    FILE = PUZZLE_INPUT_FOLDER / "day10_input_data.txt"

    lines = FILE.open("r").readlines()

    output = []
    for line in lines:
        output.append(list(line.strip("\n")))

    return output


def load_input_day11() -> List[List[int]]:
    """Generate map with encoded intensity of glowing octopusses.

    Returns:
        List[List[str]] -- glowing octopus intensity
    """
    FILE = PUZZLE_INPUT_FOLDER / "day11_input_data.txt"

    raw_input = []
    with FILE.open("r") as fh:
        for line in fh.readlines():
            encoded_line = [int(intensity) for intensity in list(line.strip("\n"))]
            raw_input.append(encoded_line)

    return raw_input


def load_input_day12():
    """Generate cave connections from input file.

    Returns:
        List[List[str]] --
    """
    FILE = PUZZLE_INPUT_FOLDER / "day12_input_data.txt"

    raw_input = []
    with FILE.open("r") as fh:
        lines = fh.readlines()
        for line in lines:
            from_cave, to_cave = line.strip("\n").split("-")
            raw_input.append((from_cave, to_cave))

    return raw_input


def load_input_day13(
    size: str = None,
) -> Tuple[List[Tuple[int, int]], List[Tuple[str, int]]]:
    """Generate transparent map and folding instructions.

    Keyword Arguments:
        size {str} -- whether to load the "small" example or target puzzle
                                                input(None)  (default: {None})

    Returns:
        Tuple[List[Tuple[int, int],List[Tuple[str, int]]]:
                                                    First argument: points
                                                    (x, y) at transparent map.
                                                    Second, folding position
                                                    vertically (x) or horizontally
                                                    (y) including line number.
    """
    size = "_" + size if size else ""
    FILE = PUZZLE_INPUT_FOLDER / f"day13_input_data{size}.txt"

    dot_positions = []
    raw_folding = []
    with FILE.open("r") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        for line in lines:
            if "," in line:
                x, y = line.split(",")
                dot_positions.append((int(x), int(y)))
            elif "=" in line:
                begin, line_no = line.split("=")
                raw_folding.append((begin[-1], int(line_no)))

    return dot_positions, raw_folding


def load_input_day14(size: str = None) -> Tuple[List[Tuple[str, str]], str]:
    """Generate raw_input for day 14 puzzle.

    Keyword Arguments:
        size {str} -- whether to load the "small" example or target puzzle
                                                input(None)  (default: {None})

    Returns:
        Tuple[List[Tuple[int, int],List[Tuple[str, int]]]:
                                                    First argument: points
                                                    (x, y) at transparent map.
                                                    Second, folding position
                                                    vertically (x) or horizontally
                                                    (y) including line number.
    """
    size = "_" + size if size else ""
    FILE = PUZZLE_INPUT_FOLDER / f"day14_input_data{size}.txt"

    with FILE.open("r") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]

        raw_input = []
        for line in lines:
            if "->" in line:
                char_from, char_to = line.split(" -> ")
                raw_input.append((char_from, char_to))
            elif line == '':
                continue
            else:
                init_word = line

        return raw_input, init_word


def load_input_day17():
    FILE = PUZZLE_INPUT_FOLDER / "day17_input_data.txt"

    with open(FILE, "r") as fh:
        line = fh.readline().strip()
        xrange, yrange = re.findall('\=(.*)\,.*\=(.*)', line)[0]
        x_min, x_max = xrange.split("..")
        y_min, y_max = yrange.split("..")
        x_min, x_max = int(x_min), int(x_max)
        y_min, y_max = int(y_min), int(y_max)

        return ((x_min, y_min), (x_max, y_max))
