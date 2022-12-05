import os
import posixpath
import requests as re
from typing import Optional
from urllib.parse import urljoin


class AdventOfCodeDay:
    AOC_BASE_URL = "https://adventofcode.com"

    def __init__(self, session_key: str, day: int = -1, year: int = 2022) -> None:
        self._session = f"session={session_key}"

        self._stream_input: Optional[re.Response] = None
        self._cached_url: Optional[str] = None
        self._day = day
        self._year = year

    def set_input_stream(self) -> None:
        path = posixpath.join(str(self._year), "day", str(self._day), "input")
        url = urljoin(self.AOC_BASE_URL, path)

        response_stream = re.get(
            url=url, headers={"Cookie": self._session}, stream=True
        )
        response_stream.raise_for_status()

        self._cached_url = url
        self._stream_input = response_stream

    def reset_input_stream(self) -> None:
        if self._cached_url is None:
            raise ValueError("Can not reset stream since it was never set")

        response_stream = re.get(
            url=self._cached_url, headers={"Cookie": self._session}, stream=True
        )
        response_stream.raise_for_status()

        self._stream_input = response_stream

    def solve_part_one(self) -> str:
        raise NotImplementedError("Should implement solve_part_one()")

    def solve_part_two(self) -> str:
        raise NotImplementedError("Should implement solve_part_two()")


def raise_if_stream_not_set(f):
    def wrap(day: AdventOfCodeDay):
        if day._stream_input is None:
            raise ValueError("Stream is not set. Use .set_stream_input() first.")
        return f(day)

    return wrap
