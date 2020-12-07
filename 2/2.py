
def get_data(data_file):
    lines = []
    with open(data_file) as data:
        for line in data.readlines():
            lines.append(line.rstrip())
    return lines

def validate_password(pwd, char, min, max, new=False):
    if new:
        count = 0
        if pwd[min-1] == char: count += 1
        if pwd[max-1] == char: count += 1
        return count == 1
    else:
        count = pwd.count(char)
        return min <= count and count <= max

def valid_password_count(data, new=False):
    tally = 0
    for line in data:
        [count, char, pwd] = line.split(' ')
        count = count.split('-')
        if validate_password(pwd, char[0], int(count[0]), int(count[1]), new):
            tally += 1
    return tally


print(valid_password_count(get_data('example.txt')))
print(valid_password_count(get_data('input.txt')))

print(valid_password_count(get_data('example.txt'), True))
print(valid_password_count(get_data('input.txt'), True))