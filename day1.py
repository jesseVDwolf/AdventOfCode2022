import os
from dotenv import load_dotenv

from day import AdventOfCodeDay


class AOCDayOne(AdventOfCodeDay):
    def __init__(self, session_key: str, day: int = 1, year: int = 2022) -> None:
        super().__init__(session_key, day, year)

    def _get_elve_totals(self) -> list[int]:
        if self._stream_input is None:
            raise ValueError("Stream is not set. Use .set_stream_input() first.")

        elve_sum: int = 0
        elve_totals: list[int] = []
        for chunk in self._stream_input.iter_lines(decode_unicode=True):
            if len(chunk) == 0:
                elve_totals.append(elve_sum)
                elve_sum = 0
            else:
                elve_sum += int(chunk)

        return elve_totals

    def solve_part_one(self) -> str:
        return str(max(self._get_elve_totals()))

    def solve_part_two(self) -> str:
        return str(sum(sorted(self._get_elve_totals())[-3:]))


def main() -> None:
    if not load_dotenv(override=True):
        raise ValueError("Could not find .env file")
    aoc = AOCDayOne(session_key=os.environ["AOC_SESSION_KEY"])
    aoc.set_input_stream()

    print(aoc.solve_part_one())
    aoc.reset_input_stream()
    print(aoc.solve_part_two())


if __name__ == "__main__":
    main()
