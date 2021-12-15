"""Solution for day 14 puzzle (see https://adventofcode.com/2021/day/14)."""
from aoc.io.data_load import load_input_day14
from typing import Tuple, List
from collections import Counter


class Polimerization:
    def __init__(self, raw_input: List[Tuple[str, str]], template: str):
        """Initialize Polimerization setup.

        Arguments:
            raw_input {List[Tuple[str, str]]} -- polimerization rules
            template {str} -- given polimerization template
        """
        self.raw_input = raw_input
        self.template = template
        self.len = len(self.template)
        self.rules = {char_from: char_to for char_from, char_to in self.raw_input}

    def __repr__(self) -> str:
        """Print out representation."""
        return self.template_raw

    def __init_frequencies(self):
        """Generate initial frequencies before running
        any polimerization step.
        """
        # count char frequency at given template string
        self.poly_freq = Counter(self.template)

        # count frequency of 2-char bag-of-words strings
        self.pair_freq = Counter()
        for idx in range(self.len - 1):
            pair = self.template[idx : idx + 2]
            self.pair_freq[pair] += 1

    def __polymerization_step(self):
        """Generate frequencies after applying the
        polimerization rule to the given state.

        Returns:
            Counter -- frequencies of all 2-tuple partial strings
        """
        new_pair_freq = Counter()

        # Iterate through every known pair frequency and apply
        # the given rules to those 2-char-strings (=polymerization).
        # A polymerization rule AB -> C uses the already known
        # frequencies for "AB", splits this polymer into "AC" and "CB"
        # and updates the frequency for "C" and also the frequencies for
        # "AC" and "CB"
        for key in self.pair_freq:
            added_polymer = self.rules[key]
            pair1, pair2 = key[0] + added_polymer, added_polymer + key[1]
            self.poly_freq[added_polymer] += self.pair_freq[key]
            new_pair_freq[pair1] += self.pair_freq[key]
            new_pair_freq[pair2] += self.pair_freq[key]
        return new_pair_freq

    def __run_polimerization(self, steps: int):
        """Generate solution for a given number of polimerization steps.

        Arguments:
            steps {int} -- number of polymerization steps.

        Returns:
            int -- max frequenices - min frequencies
        """
        for _ in range(steps):
            self.pair_freq = self.__polymerization_step()

        max_freq = self.poly_freq.most_common()[0][1]
        min_freq = self.poly_freq.most_common()[-1][1]
        return max_freq - min_freq

    def solve1(self):
        """Solution function to PART1."""
        self.__init_frequencies()
        solution1 = self.__run_polimerization(steps=10)
        print("Solution PART1:", solution1)

    def solve2(self):
        """Solution function to PART2."""
        self.__init_frequencies()
        solution2 = self.__run_polimerization(steps=40)
        print("Solution Part2:", solution2)


if __name__ == "__main__":
    # load input data
    input_raw, template = load_input_day14()

    # PART1
    Polimerization(input_raw, template).solve1()

    # PART2
    Polimerization(input_raw, template).solve2()