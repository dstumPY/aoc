import pandas as pd
from pathlib import Path
from aoc.day4.choices import CHOICES

ROOT = Path(".")
DIR = ROOT / "aoc/day4/boards" / "boards.csv"


def process_input_data() -> Dict[pd.DataFrame]:
    """Read boards.csv and store data as list of DFs

    Returns:
        Dict[pd.DataFrame] -- List of DataFrame boards
    """
    # remove newlines, spaces and cast numbers to int
    with DIR.open("r") as file:
        lines = [
            line.rstrip("\n").rstrip(" ").lstrip(" ").replace("  ", " ")
            for line in file.readlines()
        ]

    # store every block as DataFrame into
    boards = []
    current_board = []
    for line in lines:
        # skip empty lines
        if line == "":
            boards.append(current_board)
            current_board = []
            continue

        tmp_line = [int(number) for number in line.split(" ")]
        current_board.append(tmp_line)

    # store blocks as DataFrames
    boards_df = [pd.DataFrame(board) for board in boards]
    boards_dict = dict(zip(range(1, 200), boards_df))

    return boards_dict


boards_dict = process_input_data()
print("The first found board solves the first part of the puzzle:")

# replace choices ar DataFrame with zeros
for choice in CHOICES:

    # data update is required since dict resizing is not allowed during
    # loops (see winning board dropping)
    tmp_boards_dict = boards_dict.copy()

    for idx, board in tmp_boards_dict.items():

        # replace found choices with zeros
        boards_dict[idx] = board.replace(choice, 0)

        current = boards_dict[idx]
        # test if board has zero col or zero row
        if current.sum(axis=0).eq(0).any() or current.sum(axis=1).eq(0).any():
            board_sum = current.sum(axis=1).sum(axis=0)
            print("i:", idx)
            print("choice: ", choice)
            print(tmp_board)
            print("sum:", board_sum)
            print(
                "Result: ",
                choice * board_sum,
            )

            # drop winning board
            del boards_dict[idx]

print("The last board (above) solves the second part of the puzzle.")