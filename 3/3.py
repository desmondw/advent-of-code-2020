
def get_data(data_file):
    lines = []
    with open(data_file) as data:
        for line in data.readlines():
            lines.append(line.rstrip())
    return lines

def tree_encounter_count(map, mx, my):
    tally = 0
    x, y = 0, 0
    while (y < len(map)):
        if map[y][x] == '#': tally += 1
        x += mx
        x %= len(map[0])
        y += my
    return tally

def multiply_all_slopes(map):
    tally = 1
    tally *= tree_encounter_count(map, 1, 1)
    tally *= tree_encounter_count(map, 3, 1)
    tally *= tree_encounter_count(map, 5, 1)
    tally *= tree_encounter_count(map, 7, 1)
    tally *= tree_encounter_count(map, 1, 2)
    return tally

print(tree_encounter_count(get_data('example.txt'), 3, 1))
print(tree_encounter_count(get_data('input.txt'), 3, 1))

print(multiply_all_slopes(get_data('example.txt')))
print(multiply_all_slopes(get_data('input.txt')))
