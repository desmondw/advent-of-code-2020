import copy

def get_data(data_file):
    lines = []
    with open(data_file) as data:
        for line in data.readlines():
            line = line.rstrip()
            line = int(line)
            lines.append(line)
    return lines

def check_for_sum(nums, sum):
    for i,n in enumerate(nums):
        for n2 in nums[i+1:]:
            if n + n2 == sum:
                return True
    return False

def get_first_break(list, preamble):
    for i,n in enumerate(list[preamble:]):
        if not check_for_sum(list[i:preamble+i], n):
            return n

    return None

def get_set_for(list, target):
    for i in range(len(list)):
        j = i+1
        acc = list[i]
        while j < len(list):
            acc += list[j]
            if acc == target:
                sub_list = list[i:j+1]
                return min(sub_list) + max(sub_list)
            j += 1
    
    return None


print(get_data('example.txt'))
break_num_1 = get_first_break(get_data('example.txt'), 5)
break_num_2 = get_first_break(get_data('input.txt'), 25)
print(break_num_1)
print(break_num_2)

print(get_set_for(get_data('example.txt'), break_num_1))
print(get_set_for(get_data('input.txt'), break_num_2))
