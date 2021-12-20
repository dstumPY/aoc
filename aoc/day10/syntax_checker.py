"""Solution for day 10 puzzle (see https://adventofcode.com/2021/day/10)."""

from collections import deque
from typing import List, Tuple

from aoc.io.data_load import load_input_day10

# check syntax line
OPENING_CHAR = set(("{", "(", "[", "<"))
CLOSING_CHAR = set(("}", ")", "}", ">"))
OPEN_TO_CLOSE = {"{": "}", "(": ")", "[": "]", "<": ">"}
CLOSE_TO_OPEN = {"}": "{", ")": "(", "]": "[", ">": "<"}
SCORING = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def get_score(line: deque) -> int:
    """Get scoring for a sequence of brackets.

    Arguments:
        line {deque} -- score sequence of brackets
                        according to the puzzles scoring rule.

    Returns:
        int -- score
    """
    total_score = 0
    for char in line:
        total_score *= 5
        total_score += SCORING[char]
    return total_score


def solve1(lines: List[List[str]]) -> Tuple[List[str], List[Tuple[int, int]]]:
    """Find syntax errors given a sequence of brackets.

    A stack (deque) data structure is used in order to place every
    opening bracket and wait for the corresponding closing part.

    Arguments:
        lines {List[List[str]]} -- sequence of single-string brackets

    Returns:
        Tuple[List[str], List[Tuple[int,int]] -- found misplaced brackets and
                                                misplaced bracket list positions
    """
    # use a stack data structure to remember every opening character
    # that hasn't been already closed
    stack = deque()
    syntax_error_char = []
    syntax_error_position = []

    # Scan all lines for opening chars and add them to the stack.
    # Remove the last added char in case closing char was found.
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in OPENING_CHAR:
                stack.append(char)
            elif stack[-1] == CLOSE_TO_OPEN[char]:
                stack.pop()
            else:
                print(
                    f"Wrong syntax input: Expected {OPEN_TO_CLOSE[stack[-1]]}"
                    f"but found {char} instead at position {[(i, j)]}"
                )
                syntax_error_char.append(char)
                syntax_error_position.append((i, j))

                # stop current iteration
                break

    return syntax_error_char, syntax_error_position


def solve2(syntax_error_position: List[Tuple[int, int]]) -> List[deque]:
    """[summary]

    Arguments:
        syntax_error_position {List[Tuple[int,int]]} -- [description]

    Returns:
        List[deque] -- [description]
    """
    # keep only error-free lines which are just missing closing brackets
    syntax_error_lines = [line_no for line_no, _ in syntax_error_position]
    incomplete_lines = [
        line for i, line in enumerate(lines) if i not in syntax_error_lines
    ]
    remaining_chars = []
    for i, line in enumerate(incomplete_lines):
        # stacks to store opening and closing brackets
        stack_open = deque()
        stack_close = deque()
        for j, char in enumerate(line):

            # If only an open bracket occurs just add open and closed char
            # to referring staacks, if the closing bracket occurs which coincides
            # with the latest openi-stack-added bracket both brackets can be removed
            # from those stacks since they are valid closed brackets
            if char in OPENING_CHAR:
                stack_open.append(char)
                stack_close.append(OPEN_TO_CLOSE[char])
            # check if the previous and current chars ar matching open and closing chars
            elif (stack_open[-1] == CLOSE_TO_OPEN[char]) and (stack_close[-1] == char):
                stack_open.pop()
                stack_close.pop()
            elif stack_open[-1] == CLOSE_TO_OPEN[char]:
                stack_open.pop()
            else:
                print(
                    f"Wrong syntax input: Expected {OPEN_TO_CLOSE[stack_close[-1]]},",
                    " but found {char} instead at position {[(i, j)]}",
                )
                syntax_error_char.append(char)
                break

        # get latest found bracket first
        stack_close.reverse()
        remaining_chars.append(stack_close)

    return remaining_chars


if __name__ == "__main__":
    # initialize data load
    lines = load_input_day10()

    # PART1

    # run syntax check and list all conflicting bracket syntax errors
    syntax_error_char, syntax_error_position = solve1(lines=lines)

    mapping = {")": 3, "]": 57, "}": 1197, ">": 25137}
    result = [mapping[i] for i in syntax_error_char]
    print("Solution PART1: ", sum(result))

    # PART2

    # find all missing closing brackets and score them using the scoring function
    remaining_chars = solve2(syntax_error_position=syntax_error_position)
    result = sorted([get_score(residual) for residual in remaining_chars])
    middle_value = result[int(len(result) / 2)]
    print("Solution PART2: ", middle_value)
