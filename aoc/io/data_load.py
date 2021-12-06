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