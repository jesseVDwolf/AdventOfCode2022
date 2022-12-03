import os
from dotenv import load_dotenv

from day import AdventOfCodeDay


class AOCDayTwo(AdventOfCodeDay):
    CONST_LOOSES_FROM = {
        "A": "B",  # rock looses from paper
        "B": "C",  # paper looses from scissors
        "C": "A",  # scissors looses from rock
    }

    CONST_WIN_POINTS = 6
    CONST_DRAW_POINTS = 3
    CONST_TYPE_POINTS = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

    def __init__(self, session_key: str, day: int = 2, year: int = 2022) -> None:
        super().__init__(session_key, day, year)

    def solve_part_one(self) -> str:
        if self._stream_input is None:
            raise ValueError("Stream is not set. Use .set_stream_input() first.")

        line: str
        total_points = 0
        for line in self._stream_input.iter_lines(decode_unicode=True):
            rps_match = line.strip().split()

            # add the points for the type of draw (1, 2 or 3)
            total_points += self.CONST_TYPE_POINTS[rps_match[1]]
            match rps_match:

                case ["A", "X"] | ["B", "Y"] | ["C", "Z"]:
                    total_points += self.CONST_DRAW_POINTS

                case ["A", "Y"] | ["B", "Z"] | ["C", "X"]:
                    total_points += self.CONST_WIN_POINTS

        return str(total_points)

    def solve_part_two(self) -> str:
        if self._stream_input is None:
            raise ValueError("Stream is not set. Use .set_stream_input() first.")

        line: str
        total_points = 0
        for line in self._stream_input.iter_lines(decode_unicode=True):
            rps_match = line.strip().split()

            # update the rps_match based on having to win, draw or loose
            if rps_match[1] == "X":  # loose
                rps_match[1] = next(
                    k for (k, v) in self.CONST_LOOSES_FROM.items() if v == rps_match[0]
                )

            if rps_match[1] == "Y":  # draw
                rps_match[1] = rps_match[0]

            if rps_match[1] == "Z":  # wins
                rps_match[1] = self.CONST_LOOSES_FROM[rps_match[0]]

            # add the points for the type of draw (1, 2 or 3)
            total_points += self.CONST_TYPE_POINTS[rps_match[1]]
            match rps_match:

                case ["A", "A"] | ["B", "B"] | ["C", "C"]:
                    total_points += self.CONST_DRAW_POINTS

                case ["A", "B"] | ["B", "C"] | ["C", "A"]:
                    total_points += self.CONST_WIN_POINTS

        return str(total_points)


def main() -> None:
    if not load_dotenv(override=True):
        raise ValueError("Could not find .env file")
    aoc = AOCDayTwo(session_key=os.environ["AOC_SESSION_KEY"])
    aoc.set_input_stream()

    print(aoc.solve_part_one())
    aoc.reset_input_stream()
    print(aoc.solve_part_two())


if __name__ == "__main__":
    main()
