with open("test_input.txt", mode="r") as input_file:
    instructions = list(
        map(
            lambda x: (x[0], int(x[1])),
            [v.split() for v in input_file.read().splitlines()],
        )
    )

def print_grid(knots: list[list[int]], visited: set[tuple[int, int]]) -> None:
    print(knots)
    for y in range(-10, 10):
        for x in range(-10, 10):
            if [x, y] == knots[0]:
                print('H', end='')
            elif [x, y] in knots[:-1]:
                idx = next(idx for idx, v in enumerate(knots[:-1]) if v == [x, y])
                print(idx, end='')
            elif (x, y) in visited:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()

CONST_KNOT_AMOUNT = 10
CONST_START_POS = [0, 0]

knots = [CONST_START_POS] * CONST_KNOT_AMOUNT
positions_visited: set[tuple[int, int]] = {tuple(CONST_START_POS)}

# for each instruction
for instruction, steps in instructions:

    # for each step
    for _ in range(steps):
        
        print_grid(knots, positions_visited)
        # check the type of instruction
        match instruction:

            case 'R':
                knots[-1][0] += 1

                # for each knot
                for idx, knot in enumerate(knots):
                    
                    if idx < (len(knots) - 1):
                        if abs(knots[idx][1] - knots[idx + 1][1]) > 1 or  abs(knots[idx][0] - knots[idx + 1][0]) > 1:
                
                            # check if diagonally
                            if abs(knots[idx + 1][1] - knots[idx][1]) > 0:
                                knots[idx][1] = knots[idx + 1][1]
                            
                            knots[idx][0] += 1
                            positions_visited.add(tuple(knots[idx]))

            case 'L':
                pass

            case 'U':
                pass

            case 'D':
                pass
