import os
from typing import Iterable
from dotenv import load_dotenv

from day import AdventOfCodeDay, raise_if_stream_not_set


class AOCDayEight(AdventOfCodeDay):
    def __init__(self, session_key: str, day: int = 8, year: int = 2022) -> None:
        super().__init__(session_key, day, year)

    @raise_if_stream_not_set
    def _get_input(self) -> list[list[int]]:
        matrix: list[list[int]] = [
            list(map(int, list(line.strip())))
            for line in self._stream_input.iter_lines(decode_unicode=True)
            if line
        ]
        return matrix

    def solve_part_one(self) -> str:
        matrix = self._get_input()

        # all trees on the edge are already seen by default
        column_amount = len(matrix[0])
        row_amount = len(matrix)

        transposed = list(zip(*matrix))

        trees_outside = (row_amount * 2) + (column_amount * 2) - 4

        # for each tree except those on the edge
        trees_visible = trees_outside
        for row_idx in range(row_amount):

            for col_idx in range(column_amount):

                # check if not on the edge
                if 0 < row_idx < (row_amount - 1) and 0 < col_idx < (column_amount - 1):

                    height = matrix[row_idx][col_idx]

                    # check up
                    before = transposed[col_idx][:row_idx]
                    if len([v for v in before if v >= height]) == 0:
                        trees_visible += 1
                        continue

                    # check down
                    after = transposed[col_idx][row_idx + 1 :]
                    if len([v for v in after if v >= height]) == 0:
                        trees_visible += 1
                        continue

                    # check left
                    before = matrix[row_idx][:col_idx]
                    if len([v for v in before if v >= height]) == 0:
                        trees_visible += 1
                        continue

                    # check right
                    after = matrix[row_idx][col_idx + 1 :]
                    if len([v for v in after if v >= height]) == 0:
                        trees_visible += 1
                        continue

        return str(trees_visible)

    def solve_part_two(self) -> str:
        def count_smaller_trees_between(height: int, trees: Iterable[int]) -> int:
            count = 0
            for v in trees:
                count += 1
                if v >= height:
                    break

            return count

        matrix = self._get_input()

        # all trees on the edge are already seen by default
        column_amount = len(matrix[0])
        row_amount = len(matrix)

        scenic_scores: list[int] = []
        transposed = list(zip(*matrix))
        for row_idx in range(row_amount):

            for col_idx in range(column_amount):

                # check if not on the edge
                if 0 < row_idx < (row_amount - 1) and 0 < col_idx < (column_amount - 1):
                    height = matrix[row_idx][col_idx]

                    # check up
                    before = reversed(transposed[col_idx][:row_idx])
                    a = count_smaller_trees_between(height, before)

                    # check down
                    after = transposed[col_idx][row_idx + 1 :]
                    b = count_smaller_trees_between(height, after)

                    # check left
                    before = reversed(matrix[row_idx][:col_idx])
                    c = count_smaller_trees_between(height, before)

                    # check right
                    after = matrix[row_idx][col_idx + 1 :]
                    d = count_smaller_trees_between(height, after)

                    scenic_scores.append(a * b * c * d)

        return str(max(scenic_scores))


def main() -> None:
    if not load_dotenv(override=True):
        raise ValueError("Could not find .env file")
    aoc = AOCDayEight(session_key=os.environ["AOC_SESSION_KEY"])
    aoc.set_input_stream()

    print(aoc.solve_part_one())
    aoc.reset_input_stream()
    print(aoc.solve_part_two())


if __name__ == "__main__":
    main()
