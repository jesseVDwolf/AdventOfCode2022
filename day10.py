with open("input.txt", mode="r") as input_file:
    instructions = input_file.read().splitlines()


"""
Instructions look like the following:
<instruction> <argument>

The following instructions are available:
* noop
  * Nothing happens
* addx <argument>
  * Add <argument> to X

X in this case is a register
"""
CONST_CRT_WIDTH = 40
CONST_CRT_HEIGHT = 6


cycles = 0
cycle_amount = 0
register_x_value = 1
signal_strengths = 0

instructions.reverse()
to_exec: list[tuple[str, str]] = []
while instructions or to_exec:

    if cycles == 20 or (cycles >= 60 and ((cycles - 20) % 40 == 0)):
        signal_strengths += cycles * register_x_value

    if cycle_amount == 0:

        if to_exec:
            _, arg = to_exec.pop()
            register_x_value += int(arg)

        if instructions:
            instruction = instructions.pop().split()

            match instruction:

                case [ins]:
                    cycle_amount += 1

                case [ins, arg]:
                    cycle_amount += 2
                    to_exec.append(tuple(instruction))

    cycle_amount -= 1
    cycles += 1

print(register_x_value, cycles, signal_strengths)
