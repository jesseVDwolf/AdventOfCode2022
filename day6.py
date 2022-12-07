import os
from dotenv import load_dotenv

from day import AdventOfCodeDay, raise_if_stream_not_set


class AOCDaySix(AdventOfCodeDay):
    def __init__(self, session_key: str, day: int = 6, year: int = 2022) -> None:
        super().__init__(session_key, day, year)

    def _solve(self, window_size: int) -> str:
        raw_chars = list(self._stream_input.content.decode("utf-8"))
        for i in range(len(raw_chars) - window_size + 1):

            window = raw_chars[i : i + window_size]
            if len(set(window)) == window_size:

                return str(i + window_size)

    @raise_if_stream_not_set
    def solve_part_one(self) -> str:
        return self._solve(window_size=4)

    @raise_if_stream_not_set
    def solve_part_two(self) -> str:
        return self._solve(window_size=14)


def main() -> None:
    if not load_dotenv(override=True):
        raise ValueError("Could not find .env file")
    aoc = AOCDaySix(session_key=os.environ["AOC_SESSION_KEY"])
    aoc.set_input_stream()

    print(aoc.solve_part_one())
    aoc.reset_input_stream()
    print(aoc.solve_part_two())


if __name__ == "__main__":
    main()
