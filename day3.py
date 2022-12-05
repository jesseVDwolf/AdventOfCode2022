import os
from functools import reduce
from dotenv import load_dotenv

from day import AdventOfCodeDay, raise_if_stream_not_set


class AOCDayThree(AdventOfCodeDay):
    def __init__(self, session_key: str, day: int = 3, year: int = 2022) -> None:
        super().__init__(session_key, day, year)

    @raise_if_stream_not_set
    def solve_part_one(self) -> str:
        sum_priorities = 0
        for line in self._stream_input.iter_lines(decode_unicode=True):
            rucksack_items = list(line)
            compartment_a = rucksack_items[: len(rucksack_items) // 2]
            compartment_b = rucksack_items[len(rucksack_items) // 2 :]

            set_a, set_b = set(compartment_a), set(compartment_b)

            appears_in_both = (set_a & set_b).pop()
            assert appears_in_both.islower() or appears_in_both.isupper()
            priority = (
                ord(appears_in_both) - ord("a") + 1
                if appears_in_both.islower()
                else ord(appears_in_both) - ord("A") + 27
            )

            sum_priorities += priority

        return str(sum_priorities)

    @raise_if_stream_not_set
    def solve_part_two(self) -> str:
        data = self._stream_input.content.decode("utf-8")
        rucksack_data = [line for line in data.split("\n") if line != ""]

        # create partions
        sum_priority_groups = 0
        rucksack_groups = [
            rucksack_data[x : x + 3] for x in range(0, len(rucksack_data), 3)
        ]
        for group in rucksack_groups:
            compartment_sets = [set(items) for items in group]

            badge_item = reduce(lambda x, y: x & y, compartment_sets).pop()
            assert badge_item.islower() or badge_item.isupper()
            priority = (
                ord(badge_item) - ord("a") + 1
                if badge_item.islower()
                else ord(badge_item) - ord("A") + 27
            )

            sum_priority_groups += priority

        return str(sum_priority_groups)


def main() -> None:
    if not load_dotenv(override=True):
        raise ValueError("Could not find .env file")
    aoc = AOCDayThree(session_key=os.environ["AOC_SESSION_KEY"])
    aoc.set_input_stream()

    print(aoc.solve_part_one())
    aoc.reset_input_stream()
    print(aoc.solve_part_two())


if __name__ == "__main__":
    main()
