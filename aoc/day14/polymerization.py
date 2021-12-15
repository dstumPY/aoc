"""Solution for day 14 puzzle (see https://adventofcode.com/2021/day/14)."""
from aoc.io.data_load import load_input_day14
from typing import Tuple, List
from collections import Counter


class Polimerization:
    def __init__(self, raw_input: List[Tuple[str, str]], template: str):
        self.raw_input = raw_input
        self.template = template
        self.len = len(self.template)
        self.rules = {char_from: char_to for char_from, char_to in self.raw_input}

    def __repr__(self) -> str:
        return self.template_raw

    def __init_frequencies(self):
        self.poly_freq = Counter(self.template)
        self.pair_freq = Counter()
        for idx in range(self.len - 1):
            pair = self.template[idx : idx + 2]
            self.pair_freq[pair] += 1

    def __polymerization_step(self):
        new_pair_freq = Counter()
        for key in self.pair_freq:
            added_polymer = self.rules[key]
            pair1, pair2 = key[0] + added_polymer, added_polymer + key[1]
            self.poly_freq[added_polymer] += self.pair_freq[key]
            new_pair_freq[pair1] += self.pair_freq[key]
            new_pair_freq[pair2] += self.pair_freq[key]
        return new_pair_freq

    def __run_polimerization(self, steps: int):
        for _ in range(steps):
            self.pair_freq = self.__polymerization_step()

        max_freq = self.poly_freq.most_common()[0][1]
        min_freq = self.poly_freq.most_common()[-1][1]
        return max_freq - min_freq

    def solve1(self):
        self.__init_frequencies()
        solution1 = self.__run_polimerization(steps=10)
        print("Solution PART1:", solution1)

    def solve2(self):
        self.__init_frequencies()
        solution2 = self.__run_polimerization(steps=40)
        print("Solution Part2:", solution2)


if __name__ == "__main__":
    input_raw, template = load_input_day14()

    # PART1
    Polimerization(input_raw, template).solve1()

    # PART2
    Polimerization(input_raw, template).solve2()