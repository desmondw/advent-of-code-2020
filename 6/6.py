
def get_data(data_file):
    lines = []
    with open(data_file) as data:
        section = ''
        for line in data.readlines():
            fline = line.rstrip()
            if fline: section += fline + ' '
            else:
                lines.append(section.rstrip())
                section = ''
        if section: lines.append(section.rstrip())
    return lines

def count_answered_q_group(people, all=False):
    answered = {}
    for person in people:
        for answer in person:
            if answer not in answered:
                answered[answer] = 0
            answered[answer] += 1
    if not all:
        return len(answered)

    return len([x for x in answered if answered[x] == len(people)])

def count_answered_q_all(groups, all=False):
    tally = 0
    for group in groups:
        tally += count_answered_q_group(group.split(' '), all)
    return tally

# print(get_data('example.txt'))
print(count_answered_q_all(get_data('example.txt')))
print(count_answered_q_all(get_data('input.txt')))

print(count_answered_q_all(get_data('example.txt'), True))
print(count_answered_q_all(get_data('input.txt'), True))
