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



def rotate_waypoint(facing, direction, degree, east, south):
    # get number of turns
    _degree = degree
    if degree % 90 != 0: return False
    degree = int((degree % 360) / 90) # 0 = no change, 1, 2, 3

    # normalize to right turns
    if direction == 'L':
        if degree == 1: degree = 3
        elif degree == 3: degree = 1

    # turn right x times
    while degree > 0:
        if facing == 'E': # to south
            _south = south
            south = abs(east)
            east = abs(_south)
            facing = 'S'
        elif facing == 'S': # to west
            _south = south
            south = abs(east)
            east = -abs(_south)
            facing = 'W'
        elif facing == 'W': # to north
            _south = south
            south = -abs(east)
            east = -abs(_south)
            facing = 'N'
        elif facing == 'N': # to east
            _south = south
            south = -abs(east)
            east = abs(_south)
            facing = 'E'

        degree -= 1

    return [east, south, facing]

def get_manhattan_position_waypoint(steps, facing='E'):
    east = 10
    south = -1
    ship_east = 0
    ship_south = 0
    for step in steps:
        if step[0] == 'L' or step[0] == 'R':
            [east, south, facing] = rotate_waypoint(facing, step[0], step[1], east, south)
        elif step[0] == 'F':
            ship_east += east * step[1]
            ship_south += south * step[1]
        else:
            if step[0] == 'E': east += step[1]
            elif step[0] == 'W': east -= step[1]
            elif step[0] == 'S': south += step[1]
            elif step[0] == 'N': south -= step[1]
    return abs(ship_east) + abs(ship_south)

# print(get_data('example.txt'))
print(get_manhattan_position(get_data('example.txt')))
print(get_manhattan_position(get_data('input.txt')))

print(get_manhattan_position_waypoint(get_data('example.txt')))
print(get_manhattan_position_waypoint(get_data('input.txt')))
