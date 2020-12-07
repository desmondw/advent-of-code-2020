def get_sorted_data(data_file):
    nums = []
    with open(data_file) as data:
        for line in data.readlines():
            nums.append(int(line.rstrip()))
    nums.sort()
    return nums

def sum2(nums, v):
    for n1 in nums:
        for n2 in nums[::-1]:
            if n1 + n2 == v: return n1 * n2
            elif n1 + n2 < v: break
    return False

def sum3(nums, v):
    for i,n in enumerate(nums):
        res = sum2(nums[i:], v - n)
        if res: return n * res
    return False


print(sum2(get_sorted_data('example.txt'), 2020))
print(sum2(get_sorted_data('input.txt'), 2020))

print(sum3(get_sorted_data('example.txt'), 2020))
print(sum3(get_sorted_data('input.txt'), 2020))
