import pandas as pd

from pathlib import Path

ROOT = Path(".")
DIR = ROOT / "aoc/day4/boards" / "boards.csv"


with DIR.open("r") as file:
    lines = [
        line.rstrip("\n").rstrip(" ").lstrip(" ").replace("  ", " ")
        for line in file.readlines()
    ]

boards = []
current_board = []
for line in lines:
    if line == "":
        boards.append(current_board)
        current_board = []
        continue

    tmp_line = [int(number) for number in line.split(" ")]
    current_board.append(tmp_line)

boards_df = [pd.DataFrame(board) for board in boards]
boards_dict = dict(zip(range(1,200), boards_df))
choices = [
    23,
    91,
    18,
    32,
    73,
    14,
    20,
    4,
    10,
    55,
    40,
    29,
    13,
    25,
    48,
    65,
    2,
    80,
    22,
    16,
    93,
    85,
    66,
    21,
    9,
    36,
    47,
    72,
    88,
    58,
    5,
    42,
    53,
    69,
    52,
    8,
    54,
    63,
    76,
    12,
    6,
    99,
    35,
    95,
    82,
    49,
    41,
    17,
    62,
    34,
    51,
    77,
    94,
    7,
    28,
    71,
    92,
    74,
    46,
    79,
    26,
    19,
    97,
    86,
    87,
    37,
    57,
    64,
    1,
    30,
    11,
    96,
    70,
    44,
    83,
    0,
    56,
    90,
    59,
    78,
    61,
    98,
    89,
    43,
    3,
    84,
    67,
    38,
    68,
    27,
    81,
    39,
    15,
    50,
    60,
    24,
    45,
    75,
    33,
    31,
]

for choice in choices:
    for idx, board in boards_dict.items():
        #print(idx)
        tmp_board = board.replace(choice, 0)
        boards_dict[idx] = board.replace(choice, 0)
        

        # test if board has zero col or zero row
        if tmp_board.sum(axis=0).eq(0).any() or tmp_board.sum(axis=1).eq(0).any():
            board_sum = tmp_board.sum(axis=1).sum(axis=0)
            print('i:', idx)
            print('choice: ', choice)
            print('sum:', board_sum)
            print(tmp_board)
            print('result: ', choice * board_sum,)
            # print()
            # break

