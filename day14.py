# load data from input
with open("input.txt", mode="r") as input_file:

    # each line represents a line of rock
    # these lines are either vertical or horizontal
    paths: list[list[str]] = [v.split("->") for v in input_file.read().splitlines()]
    coords: list[list[tuple[int, int]]] = [
        [tuple(map(int, v.strip().split(","))) for v in x] for x in paths
    ]

max_x, _ = max([x for s in coords for x in s], key=lambda x: x[0])
min_x, _ = min([x for s in coords for x in s], key=lambda x: x[0])
_, max_y = max([x for s in coords for x in s], key=lambda x: x[1])
_, min_y = min([x for s in coords for x in s], key=lambda x: x[1])


print(max_y - min_y, max_y, min_y)

CANVAS_WIDTH = 20 + (max_x - min_x)
CANVAS_HEIGHT = max_y + 1
canvas = [["." for _ in range(CANVAS_WIDTH)] for _ in range(CANVAS_HEIGHT)]


def print_canvas(canvas):
    # create canvas base
    for i, r in enumerate(canvas):
        for j, _ in enumerate(r):
            print(canvas[i][j], end="")
        print()


# fill in the rocks
rock_coords: list[tuple[int, int]] = []
for c in coords:

    for i, _ in enumerate(c):

        # create list of tuples from current to next
        if i < (len(c) - 1):

            x = c[i]
            y = c[i + 1]

            # print(x,y, end='\t')
            if x[0] == y[0]:
                t = [(x[0], i) for i in range(min(x[1], y[1]), max(x[1], y[1]) + 1)]
            else:
                t = [(i, x[1]) for i in range(min(x[0], y[0]), max(x[0], y[0]) + 1)]

            rock_coords.extend(t)

# just apply the move to all coords
move = 480
rock_coords = list(map(lambda t: (t[0] - move, t[1]), rock_coords))

# canvas is 30 by 30 but coords are around 500
for coord in rock_coords:
    x, y = coord
    canvas[y][x] = "#"

# sand falls down from (500, 0)
START_POS = (20, 0)
grains_rested = 0
sand_fall_through = False
while not sand_fall_through:

    at_rest = False
    pos = list(START_POS)
    while not at_rest:

        x, y = pos
        print(x, y, CANVAS_HEIGHT)
        if y == (CANVAS_HEIGHT - 1):
            sand_fall_through = True
            break

        if canvas[y + 1][x] == ".":
            # sand falls down
            pos = [pos[0], pos[1] + 1]
        else:
            # next block is rock or other sand
            # down and left
            if canvas[y + 1][x - 1] == ".":
                pos = [pos[0] - 1, pos[1] + 1]

            # down and right
            elif canvas[y + 1][x + 1] == ".":
                pos = [pos[0] + 1, pos[1] + 1]

            # at rest and solidify
            else:
                canvas[y][x] = "o"
                at_rest = True
                grains_rested += 1

print_canvas(canvas)
print(grains_rested)
