import math

def get_data(data_file):
    lines = []
    with open(data_file) as data:
        for line in data.readlines():
            lines.append(line.rstrip())
    return lines

def get_seat_position(data, rows, seats):
    min = 0
    max = rows - 1

    for m in data[:-3]:
        if m == 'F': max -= math.ceil((max - min) / 2)
        elif m == 'B': min += math.ceil((max - min) / 2)
        else: return None
    if min != max: return None
    row = max

    min = 0
    max = seats - 1
    for m in data[-3:]:
        if m == 'L': max -= math.ceil((max - min) / 2)
        elif m == 'R': min += math.ceil((max - min) / 2)
        else: return None
    if min != max: return None
    seat = max

    return [row, seat]

def get_highest_seat_id(data, rows, seats):
    highest = 0
    for d in data:
        p = get_seat_position(d, rows, seats)
        id = p[0] * seats + p[1]
        if highest < id: highest = id
    return highest

def get_sead_id(data, rows, seats):
    ids = {}
    for d in data:
        p = get_seat_position(d, rows, seats)
        ids[p[0] * seats + p[1]]=True
    # ids.sort()
    for x in range(min(ids), max(ids)):
        if x not in ids: return x
    return None

print(get_highest_seat_id(get_data('example.txt'), 128, 8))
print(get_highest_seat_id(get_data('input.txt'), 128, 8))

print(get_sead_id(get_data('input.txt'), 128, 8))
