from pathlib import Path

CONST_WIN_POINTS = 6
CONST_DRAW_POINTS = 3
CONST_TYPE_POINTS = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

file_path = Path(__file__).parent.joinpath('input.txt').resolve()
with open(file_path, mode='r') as input_file:

    total_points = 0
    for line in input_file:
        rps_match = line.strip().split()

        # add the points for the type of draw (1, 2 or 3)
        total_points += CONST_TYPE_POINTS[rps_match[1]]
        match rps_match:

            case ["A", "X"] | ["B", "Y"] | ["C", "Z"]:
                total_points += CONST_DRAW_POINTS
            
            case ["A", "Y"] | ["B", "Z"] | ["C", "X"]:
                total_points += CONST_WIN_POINTS

print(total_points)
