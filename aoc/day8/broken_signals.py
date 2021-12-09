"""Solution for day 8 puzzle (see https://adventofcode.com/2021/day/78)."""
from collections import Counter
from itertools import chain
from typing import Dict, List

from aoc.io.data_load import load_input_day8


def decoding(sequence: List[List[str]]) -> Dict[frozenset, int]:
    """Generate decoding from a given encoding sequence.

    Arguments:
        sequence {List[List[str]]} -- encoded sequence

    Returns:
        Dict[frozenset, int] -- decoding that maps a frozenset
                                to the decoded digit
    """
    # init all sequence decodings to 100
    d = {frozenset(set(seq)): 100 for seq in sequence}

    # first decode the easy one signal decodings since their
    # used segments are unique, e.g. a 1 uses two display segments,
    # a 7 uses 3 display segments
    for k, v in d.items():
        if len(k) == 2:
            d[k] = 1
        elif len(k) == 3:
            d[k] = 7
        elif len(k) == 4:
            d[k] = 4
        elif len(k) == 7:
            d[k] = 8

    # set the already known decodings
    known_dic = {len(k): k for k in d.keys() if len(k) in (2, 3, 4, 7)}

    # decode the more difficult encodings:
    # therefore we measure the number of displayed segments by
    # intersetion of two known numbers, e.g. an encoding with 6
    # display segments must be contained in one of (0, 6, 9).
    # If a display segment intersection of those segments with a
    # 2-segement is equal to one, we know that it must be the
    # number 6 as both display segments have only one segment in
    # common.
    for k, v in d.items():
        if len(k) == 6:
            # test for 6 shape
            if len(k.intersection(known_dic[2])) == 1:
                d[k] = 6
            elif len(k.intersection(known_dic[4])) == 4:
                d[k] = 9
            else:
                d[k] = 0

        # similar argument as above
        if len(k) == 5:
            # test for shape 3
            if len(k.intersection(known_dic[2])) == 2:
                d[k] = 3
            elif len(k.intersection(known_dic[4])) == 3:
                d[k] = 5
            else:
                d[k] = 2

    return d


## PART1

# load preprocessed input data and flatten
# input to single list
signals, output = load_input_day8()
flattened_output = list(chain(*output))

# count signal length
cnt = Counter([len(signal) for signal in flattened_output])
print(f"Solution PART1: {cnt[2] + cnt[4] + cnt[3] + cnt[7]}")


## PART2

# split signals and output into list of chars
signal_char_split = [[list(s) for s in signal] for signal in signals]
output_char_split = [[list(s) for s in signal] for signal in output]

# decode given signal input and store decoding
decodings_list = [decoding(seq) for seq in signal_char_split]

# apply decoding at encoded output
decoded_output = []
for sig, out in zip(signal_char_split, output_char_split):
    current_decoding = decoding(sig)
    decoded = [current_decoding[frozenset(char)] for char in out]
    decoded_output.append(decoded)

result = [
    int("{0}{1}{2}{3}".format(*digit_list)) for digit_list in decoded_output
]

print(f"Solution PART2: {sum(result)}")
