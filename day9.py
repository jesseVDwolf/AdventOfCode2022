import copy

with open('input.txt', mode='r') as input_file:
    instructions = list(map(lambda x: (x[0], int(x[1])), [ 
        v.split()
        for v in input_file.read().splitlines()
    ]))

def print_grid(pos_head: list[int], pos_tail: list[int], visited: set[tuple[int, int]]) -> None:
    print(pos_head, pos_tail)
    for y in range(-10, 10):
        for x in range(-10, 10):
            if pos_head[0] == x and pos_head[1] == y:
                print('H', end='')
            elif pos_tail[0] == x and pos_tail[1] == y:
                print('T', end='')
            elif (x, y) in visited:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()
                

# initial state is H and T are at the same position
START_POS = [0, 0]  # x, y

pos_head = copy.copy(START_POS)
pos_tail = copy.copy(START_POS)

positions_visited: set[tuple[int, int]] = {tuple(START_POS)}
# print_grid(pos_head, pos_tail, positions_visited)
for instruction, steps in instructions:

    # print(instruction, steps)
    match instruction:

        # right
        case 'R':
            for _ in range(steps):
                # move head
                pos_head[0] += 1
                # print_grid(pos_head, pos_tail, positions_visited)
                # move tail
                # check if head on top of tail
                if abs(pos_tail[1] - pos_head[1]) > 1 or  abs(pos_tail[0] - pos_head[0]) > 1:
                
                    # check if diagonally
                    if abs(pos_head[1] - pos_tail[1]) > 0:
                        pos_tail[1] = pos_head[1]
                    
                    pos_tail[0] += 1
                    positions_visited.add(tuple(pos_tail))
                
                # print_grid(pos_head, pos_tail, positions_visited)

        # left
        case 'L':
            for _ in range(steps):
                # move head
                pos_head[0] -= 1 
                # print_grid(pos_head, pos_tail, positions_visited)
                # move tail
                # check if head on top of tail
                if abs(pos_tail[1] - pos_head[1]) > 1 or  abs(pos_tail[0] - pos_head[0]) > 1:
                
                    # check if diagonally
                    if abs(pos_head[1] - pos_tail[1]) > 0:
                        pos_tail[1] = pos_head[1]
                    
                    pos_tail[0] -= 1
                    positions_visited.add(tuple(pos_tail))
                
                # print_grid(pos_head, pos_tail, positions_visited)
        
        # up
        case 'U':
            for _ in range(steps):
                # move head
                pos_head[1] += 1
                # print_grid(pos_head, pos_tail, positions_visited)
                # move tail
                # check if head on top of tail
                if abs(pos_tail[1] - pos_head[1]) > 1 or  abs(pos_tail[0] - pos_head[0]) > 1:
                
                    # check if diagonally
                    if abs(pos_head[0] - pos_tail[0]) > 0:
                        pos_tail[0] = pos_head[0]
                    
                    pos_tail[1] += 1
                    positions_visited.add(tuple(pos_tail))
                
                # print_grid(pos_head, pos_tail, positions_visited)


        # down
        case 'D':
            for _ in range(steps):
                # move head
                pos_head[1] -= 1 
                # print_grid(pos_head, pos_tail, positions_visited)
                # move tail
                # check if head on top of tail
                if abs(pos_tail[1] - pos_head[1]) > 1 or  abs(pos_tail[0] - pos_head[0]) > 1:
                
                    # check if diagonally
                    if abs(pos_head[1] - pos_tail[1]) > 0:
                        pos_tail[0] = pos_head[0]
                    
                    pos_tail[1] -= 1
                    positions_visited.add(tuple(pos_tail))
                
                # print_grid(pos_head, pos_tail, positions_visited)

print(len(positions_visited))
