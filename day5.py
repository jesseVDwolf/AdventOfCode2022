import os
from dotenv import load_dotenv
from functools import reduce
from itertools import groupby

from day import AdventOfCodeDay, raise_if_stream_not_set


class AOCDayFive(AdventOfCodeDay):
    def __init__(self, session_key: str, day: int = 5, year: int = 2022) -> None:
        super().__init__(session_key, day, year)

    @raise_if_stream_not_set
    def solve_part_one(self) -> str:
        lines = list(self._stream_input.iter_lines(decode_unicode=True))

        stack_data, instructions = [
            list(group) for k, group in groupby(lines, bool) if k
        ]

        matrix: list[list[str]] = []
        for line in stack_data[:-1]:
            row = [line[x : x + 4] for x in range(0, len(line), 4)]
            row = list(map(lambda x: x.strip(), row))

            matrix.append(row)

        tranposed: list[list[str]] = list(map(list, zip(*matrix)))
        stacks = [[v for v in stack if v != ""][::-1] for stack in tranposed]

        instructions = [ins.strip() for ins in instructions]
        for ins in instructions:

            _, amount, _, from_stack, _, to_stack = ins.split()
            for _ in range(int(amount)):
                stacks[int(to_stack) - 1].append(stacks[int(from_stack) - 1].pop())

        result_string = reduce(lambda x, y: x + y.pop()[1:2], stacks, "")
        return result_string

    @raise_if_stream_not_set
    def solve_part_two(self) -> str:
        lines = list(self._stream_input.iter_lines(decode_unicode=True))

        stack_data, instructions = [
            list(group) for k, group in groupby(lines, bool) if k
        ]

        matrix: list[list[str]] = []
        for line in stack_data[:-1]:
            row = [line[x : x + 4] for x in range(0, len(line), 4)]
            row = list(map(lambda x: x.strip(), row))

            matrix.append(row)

        tranposed: list[list[str]] = list(map(list, zip(*matrix)))
        stacks = [[v for v in stack if v != ""][::-1] for stack in tranposed]

        instructions = [ins.strip() for ins in instructions]
        for ins in instructions:

            _, amount, _, from_stack, _, to_stack = ins.split()

            idx_from = int(from_stack) - 1
            idx_to = int(to_stack) - 1

            crates = stacks[idx_from][-int(amount) :]
            stacks[idx_from] = stacks[idx_from][: -int(amount)]
            stacks[idx_to] = stacks[idx_to] + crates

        result_string = reduce(lambda x, y: x + y.pop()[1:2], stacks, "")
        return result_string


def main() -> None:
    if not load_dotenv(override=True):
        raise ValueError("Could not find .env file")
    aoc = AOCDayFive(session_key=os.environ["AOC_SESSION_KEY"])
    aoc.set_input_stream()

    print(aoc.solve_part_one())
    aoc.reset_input_stream()
    print(aoc.solve_part_two())


if __name__ == "__main__":
    main()
