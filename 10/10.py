import functools
import copy

def get_data(data_file):
    lines = []
    with open(data_file) as data:
        for line in data.readlines():
            line = int(line.rstrip())
            lines.append(line)
    lines.sort()
    return lines

def tally_jolt_differences(data):
    jolts = 0
    diff_count = {
        1: 0,
        2: 0,
        3: 1
    }

    for adpt in data:
        diff = adpt - jolts
        jolts += diff
        if diff not in diff_count:
            return False
        diff_count[diff] += 1
    
    return diff_count[1] * diff_count[3]


def tally_adpt_combos(data):
    cache = [-1]*len(data)
    return tally_adpt_combos_r(data, 0, 0, cache)

def tally_adpt_combos_r(data, start_index, v, cache):
    if start_index >= len(data): return 1
    if 0 <= cache[start_index]: return cache[start_index]
    tally = 0
    i = start_index
    for n in data:
        diff = n - v
        if diff < 1: continue
        if 3 < diff: break
        tally += tally_adpt_combos_r(data, i+1, n, cache)
        i += 1
    cache[start_index] = tally
    return tally

print(get_data('example.txt'))
print(tally_jolt_differences(get_data('example.txt')))
print(tally_jolt_differences(get_data('example2.txt')))
print(tally_jolt_differences(get_data('input.txt')))

print(tally_adpt_combos(get_data('example.txt')))
print(tally_adpt_combos(get_data('example2.txt')))
print(tally_adpt_combos(get_data('input.txt')))