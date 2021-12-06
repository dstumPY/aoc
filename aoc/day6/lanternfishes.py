"""Solution for day 6 puzzle (see https://adventofcode.com/2021/day/6)."""
from collections import Counter
from aoc.io.data_load import load_input_day6


def get_new_day_ages(lanternfish_ages_cnt: Counter) -> Counter:
    """Simulate a day and calculate lanternfish ages for new day.

    Arguments:
        lanternfish_ages_cnt {Counter} -- lanternfish ages (0-8)

    Returns:
        Counter -- lantern fish ages for new day
    """    
    tmp_cnt = lanternfish_ages_cnt.copy()

    # change popultions age by shifting 
    # the previous day keys
    cnt[0] = tmp_cnt[1]
    cnt[1] = tmp_cnt[2]
    cnt[2] = tmp_cnt[3]
    cnt[3] = tmp_cnt[4]
    cnt[4] = tmp_cnt[5]
    cnt[5] = tmp_cnt[6]
    cnt[6] = tmp_cnt[7] + tmp_cnt[0]
    cnt[7] = tmp_cnt[8]
    cnt[8] = tmp_cnt[0]

    return cnt
    

## PART 1:

# load lanternfish ages and create Counter
lanternfish_ages_input = load_input_day6()
cnt = Counter(lanternfish_ages_input)
print("PART1")
print(f"The population starts with {sum(cnt.values())} fishes.")

# simulate days
for day in range(80):
    cnt = get_new_day_ages(cnt)

print(f"The population ends with {sum(cnt.values())} fishes after 80 days.\n")


## PART 2:

# load lanternfish ages and create Counter
lanternfish_ages_input = load_input_day6()
cnt = Counter(lanternfish_ages_input)
print("PART2")
print(f"The population starts with {sum(cnt.values())} fishes.")

# simulate days
for i in range(256):
    cnt = get_new_day_ages(cnt)

print(f"The population ends with {sum(cnt.values())} fishes after 256 days.")
