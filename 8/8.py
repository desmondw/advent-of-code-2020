import copy

def get_data(data_file):
    lines = []
    with open(data_file) as data:
        for line in data.readlines():
            line = line.rstrip().split(' ')
            line[1] = int(line[1])
            lines.append(line)
    return lines

def first_iter_acc(cmds):
    i = 0
    acc = 0
    hit_cmds = [False]*len(cmds)
    while 0 <= i and i < len(cmds):
        if hit_cmds[i] == True:
            return [acc, False]
        hit_cmds[i] = True
        
        if cmds[i][0] == 'jmp':
            i += cmds[i][1]
        else:
            if cmds[i][0] == 'acc':
                acc += cmds[i][1]
            i += 1
    return [acc, True]

def acc_fixed_loop(cmds):
    res = first_iter_acc(cmds)
    if res[1]: return res[0]

    for i,cmd in enumerate(cmds):
        if cmd[0] == 'acc': continue
        elif cmd[0] == 'nop': cmd[0] = 'jmp'
        elif cmd[0] == 'jmp': cmd[0] = 'nop'

        if i == 7: print(cmds)
        res = first_iter_acc(cmds)
        if res[1]: return res[0]

        if cmd[0] == 'nop': cmd[0] = 'jmp'
        elif cmd[0] == 'jmp': cmd[0] = 'nop'

    return False


# print(get_data('example.txt'))
print(first_iter_acc(get_data('example.txt'))[0])
print(first_iter_acc(get_data('input.txt'))[0])

print(acc_fixed_loop(get_data('example.txt')))
print(acc_fixed_loop(get_data('input.txt')))
