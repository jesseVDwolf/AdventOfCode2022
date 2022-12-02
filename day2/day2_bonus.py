from pathlib import Path

CONST_LOOSES_FROM = {
    'A': 'B',       # rock looses from paper
    'B': 'C',       # paper looses from scissors
    'C': 'A'        # scissors looses from rock
}

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
        
        # update the rps_match based on having to win, draw or loose
        match rps_match[1]:

            case 'X':   # loose
                rps_match[1] = next(k for (k, v) in CONST_LOOSES_FROM.items() if v == rps_match[0])

            case 'Y':   # draw
                rps_match[1] = rps_match[0]

            case 'Z':   # wins
                rps_match[1] = CONST_LOOSES_FROM[rps_match[0]]

        # add the points for the type of draw (1, 2 or 3)
        total_points += CONST_TYPE_POINTS[rps_match[1]]
        match rps_match:

            case ["A", "A"] | ["B", "B"] | ["C", "C"]:
                total_points += CONST_DRAW_POINTS
            
            case ["A", "B"] | ["B", "C"] | ["C", "A"]:
                total_points += CONST_WIN_POINTS

print(total_points)

