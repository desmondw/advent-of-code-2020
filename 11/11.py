import copy

def get_data(data_file):
    lines = []
    with open(data_file) as data:
        for line in data.readlines():
            line = line.rstrip()
            line = list(line)
            lines.append(line)
    return lines

def get_adjacent_seats(data, x, y):
    seats = []
    for i in [y-1, y, y+1]:
        for j in [x-1, x, x+1]:
            if i == y and j == x: continue
            if i < 0 or j < 0: continue
            if i >= len(data) or j >= len(data[0]): continue
            seats.append(data[i][j])
    return seats

def get_seat_from_line(data, x, y, dir_x, dir_y):
    cur_x = x + dir_x
    cur_y = y + dir_y
    while (0 <= cur_y and cur_y < len(data) and 0 <= cur_x and cur_x < len(data[0])):
        if data[cur_y][cur_x] != '.':
            return data[cur_y][cur_x]
        cur_x += dir_x
        cur_y += dir_y
    return False

# seats in line of sight
def get_los_seats(data, x, y):
    seats = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0: continue
            seat = get_seat_from_line(data, x, y, j, i)
            if (seat):
                seats.append(seat)
    return seats

def shift_people(data, los=False):
    data_init = copy.deepcopy(data)
    max_neighbors = 4
    if los:
        max_neighbors = 5

    for i,row in enumerate(data_init):
        for j,tile in enumerate(row):
            if tile != '.':
                if los:
                    neighbors = get_los_seats(data_init, j, i)
                else:
                    neighbors = get_adjacent_seats(data_init, j, i)
                if tile == 'L' and neighbors.count('#') == 0:
                    data[i][j] = '#'
                elif tile == '#' and neighbors.count('#') >= max_neighbors:
                    data[i][j] = 'L'
    return data_init != data

def count_people(data):
    count = 0
    for row in data:
        count += row.count('#')
    return count

def print_seats(data):
    for row in data:
        print(''.join(row))

def count_occupied_seats(data, los=False):
    while shift_people(data, los):
        pass
    return count_people(data)

# print_seats(get_data('input.txt'))
print(count_occupied_seats(get_data('example.txt')))
print(count_occupied_seats(get_data('input.txt')))

print(count_occupied_seats(get_data('example.txt'), True))
print(count_occupied_seats(get_data('input.txt'), True))