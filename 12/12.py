import copy

def get_data(data_file):
    lines = []
    with open(data_file) as data:
        for line in data.readlines():
            line = line.rstrip()
            c = line[0]
            n = int(line[1:])
            lines.append([c, n])
    return lines

def get_new_dir(facing, direction, degree):
    if degree % 90 != 0: return False
    degree = int((degree % 360) / 90) # 0 = no change, 1, 2, 3
    
    compass = 'NESW' if direction == 'R' else 'NWSE'
    start_index = compass.index(facing)
    new_facing_index = (start_index + degree) % 4
    return compass[new_facing_index]


def get_manhattan_position(steps, facing='E'):
    east = 0
    south = 0
    for step in steps:
        if step[0] == 'L' or step[0] == 'R':
            facing = get_new_dir(facing, step[0], step[1])
            # print(step)
            # print('new facing: '+facing)
        elif step[0] == 'F':
            if facing == 'E': east += step[1]
            elif facing == 'W': east -= step[1]
            elif facing == 'S': south += step[1]
            elif facing == 'N': south -= step[1]
        else:
            if step[0] == 'E': east += step[1]
            elif step[0] == 'W': east -= step[1]
            elif step[0] == 'S': south += step[1]
            elif step[0] == 'N': south -= step[1]
    return abs(east) + abs(south)

# print(get_data('example.txt'))
print(get_manhattan_position(get_data('example.txt')))
print(get_manhattan_position(get_data('input.txt')))
