from itertools import groupby
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Operation:

    a: str
    op: str
    b: str

    def exec(self, item: int) -> int:
        _a = item
        _b = item if self.b == "old" else int(self.b)
        return eval(f"{_a} {self.op} {_b}")


@dataclass(slots=True, frozen=True)
class Test:

    divisible_by: int
    monkey_if_true: int
    monkey_if_false: int

    def get_monkey_num(self, item: int) -> int:
        """returns the number of the monkey the item goes to"""
        return (
            self.monkey_if_true
            if (item % self.divisible_by) == 0
            else self.monkey_if_false
        )


@dataclass(slots=True)
class Monkey:

    num: int
    items: list[int]
    operation: Operation
    test: Test
    inspection_count: int = 0


monkeys: list[Monkey] = []
with open("input.txt") as input_file:

    text_groups = input_file.read().split("\n")
    for k, group in groupby(text_groups, bool):
        if k:
            attrs = list(group)
            num = int(attrs[0][-2:-1])
            starting_items = list(
                map(int, attrs[1][attrs[1].index(":") + 2 :].split(","))
            )

            operation = Operation(*(attrs[2][attrs[2].index("=") + 2 :].split()))
            test = Test(
                int(attrs[3].split()[-1]),
                int(attrs[4].split()[-1]),
                int(attrs[5].split()[-1]),
            )
            monkeys.append(Monkey(num, starting_items, operation, test))

CONST_ROUNDS = 10

for i in range(CONST_ROUNDS):

    for monkey in monkeys:

        while monkey.items:
            item = monkey.items.pop()
            item = monkey.operation.exec(item)
            # item //= 3

            to_monkey_num = monkey.test.get_monkey_num(item)
            to_monkey = next(m for m in monkeys if m.num == to_monkey_num)
            to_monkey.items.append(item)

            monkey.inspection_count += 1

top_two_monkeys = sorted(monkeys, key=lambda m: m.inspection_count)[-2:]
print(top_two_monkeys[0].inspection_count * top_two_monkeys[1].inspection_count)
