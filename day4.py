import os
from dotenv import load_dotenv

from day import AdventOfCodeDay, raise_if_stream_not_set


class AOCDayFour(AdventOfCodeDay):
    def __init__(self, session_key: str, day: int = 4, year: int = 2022) -> None:
        super().__init__(session_key, day, year)

    @raise_if_stream_not_set
    def solve_part_one(self) -> str:
        total_pairs_fully_containing_other = 0
        for line in self._stream_input.iter_lines(decode_unicode=True):
            pair = line.split(",")

            # convert ['2-4', '6-8'] to [[2,4], [6,8]]
            section_assignments = [[int(x) for x in r.split("-")] for r in pair]

            # range function is inclusive but we need the stop number as well
            section_assignments[0][-1] += 1
            section_assignments[1][-1] += 1

            set_a, set_b = [set(range(*pair)) for pair in section_assignments]
            if set_a.issubset(set_b) or set_b.issubset(set_a):
                total_pairs_fully_containing_other += 1

        return str(total_pairs_fully_containing_other)

    @raise_if_stream_not_set
    def solve_part_two(self) -> str:
        total_pairs_partially_overlapping = 0
        for line in self._stream_input.iter_lines(decode_unicode=True):
            pair = line.split(",")

            # convert ['2-4', '6-8'] to [[2,4], [6,8]]
            section_assignments = [[int(x) for x in r.split("-")] for r in pair]

            # range function is inclusive but we need the stop number as well
            section_assignments[0][-1] += 1
            section_assignments[1][-1] += 1

            set_a, set_b = [set(range(*pair)) for pair in section_assignments]
            intersection = set_a & set_b
            if len(intersection) > 0:
                total_pairs_partially_overlapping += 1

        return str(total_pairs_partially_overlapping)


def main() -> None:
    if not load_dotenv(override=True):
        raise ValueError("Could not find .env file")
    aoc = AOCDayFour(session_key=os.environ["AOC_SESSION_KEY"])
    aoc.set_input_stream()

    print(aoc.solve_part_one())
    aoc.reset_input_stream()
    print(aoc.solve_part_two())


if __name__ == "__main__":
    main()
