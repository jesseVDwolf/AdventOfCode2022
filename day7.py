import os
import shutil
from pathlib import Path
from itertools import groupby
from dotenv import load_dotenv

from day import AdventOfCodeDay, raise_if_stream_not_set


class AOCDaySeven(AdventOfCodeDay):

    TMP_DIR = ".tmp"

    PROJ_DIR = Path(__file__).parent.resolve()
    ROOT_DIR = PROJ_DIR.joinpath(TMP_DIR)

    TOTAL_DISK_SIZE_AVAILABLE = 70_000_000
    UNUSED_SPACE_NEEDED = 30_000_000

    def __init__(self, session_key: str, day: int = 7, year: int = 2022) -> None:
        super().__init__(session_key, day, year)

    @raise_if_stream_not_set
    def solve_part_one(self) -> str:
        lines = [
            line.strip() for line in self._stream_input.iter_lines(decode_unicode=True)
        ]
        self._build_file_system(input_lines=lines)
        dir_sizes = self._get_dir_sizes()
        return str(sum([v for _, v in dir_sizes.items() if v <= 100_000]))

    @raise_if_stream_not_set
    def solve_part_two(self) -> str:
        lines = [
            line.strip() for line in self._stream_input.iter_lines(decode_unicode=True)
        ]
        self._build_file_system(input_lines=lines)
        dir_sizes = self._get_dir_sizes()

        unused_space = (
            self.TOTAL_DISK_SIZE_AVAILABLE - dir_sizes[self.TMP_DIR.replace(".", "")]
        )
        to_be_deleted = self.UNUSED_SPACE_NEEDED - unused_space
        return str(next(v for v in sorted(dir_sizes.values()) if v > to_be_deleted))

    def _build_file_system(self, input_lines: list[str]) -> None:
        # clean it up first
        shutil.rmtree(str(self.ROOT_DIR))

        base_path = self.ROOT_DIR
        groups = groupby(input_lines, key=lambda x: x.startswith("$"))
        for is_cmd_group, groups in groups:

            group_list = list(groups)
            if is_cmd_group:
                # assuming the first elements are `cd` commands and the last one is always `ls`
                join_paths = [cmd.split()[2] for cmd in group_list[:-1]]

                join_paths = [
                    str(self.ROOT_DIR) if path == "/" else path for path in join_paths
                ]
                base_path = base_path.joinpath(*join_paths)
            else:
                base_path.mkdir(parents=True, exist_ok=True)

                for file_line in group_list:
                    size_or_dir, name = file_line.split()

                    if size_or_dir == "dir":
                        base_path.joinpath(name).mkdir(exist_ok=True)
                    else:
                        with base_path.joinpath(name).open(mode="w") as f:
                            f.write("0" * int(size_or_dir))

    def _get_dir_sizes(self) -> dict[str, int]:
        dir_sizes: dict[str, int] = {self.TMP_DIR.replace(".", ""): 0}
        for file in self.ROOT_DIR.relative_to(self.PROJ_DIR).glob("**/*"):

            if file.is_dir():
                key = "-".join([p.replace(".", "") for p in file.parts])
                dir_sizes[key] = 0
            else:
                # add size to all parents
                parents = [p.replace(".", "") for p in file.parts[:-1]]
                for i in range(len(parents)):
                    key = "-".join(parents[: len(parents) - i])
                    dir_sizes[key] += file.stat().st_size

        return dir_sizes


def main() -> None:
    if not load_dotenv(override=True):
        raise ValueError("Could not find .env file")
    aoc = AOCDaySeven(session_key=os.environ["AOC_SESSION_KEY"])
    aoc.set_input_stream()

    print(aoc.solve_part_one())
    aoc.reset_input_stream()
    print(aoc.solve_part_two())


if __name__ == "__main__":
    main()
