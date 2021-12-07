"""Solution for day 7 puzzle (see https://adventofcode.com/2021/day/7)."""
import pandas as pd

from aoc.io.data_load import load_input_day7

# prepare ranges
crabs_positions: list = np.array(load_input_day7())
min_position = np.min(crabs_positions)
max_position = np.max(crabs_positions)


## PART1

diff_position_list: list = []
for current_position in range(min_position, max_position + 1):
    diff_position_list.append(abs(crabs_positions - current_position))

# store distances from local position to crabs position at tabular DataFrame
# with potential local positions as index and the crabs position as column
df = pd.DataFrame()
df = pd.DataFrame(diff_position_list, index=range(min_position, max_position + 1))
min_argument = np.argmin(df.sum(axis=1))
print(f"PART1: your fuel consumption is {df.filter([min_argument]).sum().iat[0]}")


## PART2

# as fuel consumption is stationary per step, create dict lookup which follows
# the given consumption rules from that puzzle
additive_fuel_consumption = {0: 0}
for i in range(1, max_position + 1):
    additive_fuel_consumption[i] = i + additive_fuel_consumption[i - 1]

# create all possible scenarios, meaning that every possible position tests all crab positions
scenarios = {i: crabs_positions for i in range(min_position, max_position + 1)}

# calculate fuel consumption for all scenarios
result_scenarios = {}
for scenario_position, crabs_positions in scenarios.items():
    result_scenarios[scenario_position] = sum(
        [
            additive_fuel_consumption[abs(scenario_position - crab_pos)]
            for crab_pos in crabs_positions
        ]
    )

solution2 = sorted(result_scenarios.items(), key=lambda x: x[1])[0]
print(f"PART2: your fuel consumption is {solution[1]} at position {solution[0]}")
