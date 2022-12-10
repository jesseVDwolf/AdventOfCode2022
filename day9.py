import os
from dotenv import load_dotenv

from day import AdventOfCodeDay, raise_if_stream_not_set


class AOCDayNine(AdventOfCodeDay):
    """Most code is from `dmalacov`. See her repository here: https://github.com/dmalac"""

    CONST_DIRECTION: dict[str, tuple[int, int]] = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }

    def __init__(self, session_key: str, day: int = 9, year: int = 2022) -> None:
        super().__init__(session_key, day, year)

    def _move_knot(self, p: list, k: list):
        """Where `p` is the previous knot and `k` the current knot"""
        if abs(k[0] - p[0]) > 1 or abs(k[1] - p[1]) > 1:
            k[0] += 0 if p[0] == k[0] else int((p[0] - k[0]) / abs(p[0] - k[0]))
            k[1] += 0 if p[1] == k[1] else int((p[1] - k[1]) / abs(p[1] - k[1]))

    def _move_rope(self, knots: list, instruction: str, places: set[tuple[int, int]]):
        for idx, knot in enumerate(knots):
            if idx == 0:
                knot[0] += self.CONST_DIRECTION[instruction][0]
                knot[1] += self.CONST_DIRECTION[instruction][1]
            else:
                self._move_knot(knots[idx - 1], knot)
        places.add((knots[-1][0], knots[-1][1]))

    def _solve(self, rope_length: int) -> str:
        instructions = self._stream_input.iter_lines(decode_unicode=True)

        knots = [[0, 0] for _ in range(rope_length)]
        places: set[tuple[int, int]] = set()
        for line in instructions:
            instruction, steps = line.split()
            for _ in range(int(steps)):
                self._move_rope(knots, instruction, places)

        return str(len(places))

    @raise_if_stream_not_set
    def solve_part_one(self) -> str:
        return self._solve(rope_length=2)

    @raise_if_stream_not_set
    def solve_part_two(self) -> str:
        return self._solve(rope_length=10)


def main() -> None:
    if not load_dotenv(override=True):
        raise ValueError("Could not find .env file")
    aoc = AOCDayNine(session_key=os.environ["AOC_SESSION_KEY"])
    aoc.set_input_stream()

    print(aoc.solve_part_one())
    aoc.reset_input_stream()
    print(aoc.solve_part_two())


if __name__ == "__main__":
    main()
