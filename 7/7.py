
def get_data(data_file):
    object = {}
    with open(data_file) as data:
        for line in data.readlines():
            line = format_data_line(line.rstrip())
            object[line[0]] = line[1]
    return object

def format_data_line(data):
    data = data[:-1]
    [parent, children] = data.split(' bags contain ')
    if children == 'no other bags': return [parent, {}]

    children = children.replace(' bags','').replace(' bag','')
    children = children.split(', ')
    fchildren = {}
    for child in children:
        child = child.split(' ',1)
        fchildren[child[1]] = int(child[0])
    return [parent, fchildren]

def get_ancestors(data, bag):
    parents = []
    for parent in data:
        if bag in data[parent]:
            parents.append(parent)
            parents += get_ancestors(data, parent)
    return parents

def count_bag_colors(data):
    return len(set(get_ancestors(data, 'shiny gold')))

def count_descendants(data, bag):
    tally = 1
    children = data[bag]
    for child in children:
        tally += children[child] * count_descendants(data, child)
    return tally

def count_bag_req(data):
    return count_descendants(data, 'shiny gold') - 1


print(get_data('example.txt'))
print(count_bag_colors(get_data('example.txt')))
print(count_bag_colors(get_data('input.txt')))

print('---')

print(get_data('example2.txt'))
print(count_bag_req(get_data('example.txt')))
print(count_bag_req(get_data('example2.txt')))
print(count_bag_req(get_data('input.txt')))