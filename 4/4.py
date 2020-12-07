
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

def validate_byr(byr):
    return not (byr < 1920 or 2002 < byr)

def validate_iyr(iyr):
    return not (iyr < 2010 or 2020 < iyr)

def validate_eyr(eyr):
    return not (eyr < 2020 or 2030 < eyr)

def validate_hgt(hgt):
    # print('hgt')
    # print(hgt)
    if hgt[:-2] == '': return False
    hgt_n = int(hgt[:-2])
    if hgt[-2:] == 'in':
        if hgt_n < 59 or 76 < hgt_n: return False
    elif hgt[-2:] == 'cm':
        if hgt_n < 150 or 193 < hgt_n: return False
    else: return False
    return True

def validate_hcl(hcl):
    if hcl[0] != '#': return False
    if len(hcl) != 7: return False
    try:
        int(hcl[1:], 16)
    except: # except: ValueError
        return False
    return True

def validate_ecl(ecl):
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return False
    return True

def validate_pid(pid):
    if len(pid) != 9: return False
    try:
        int(pid)
    except: # except: ValueError
        return False
    return True

def validate_passport(data, req_fields):
    for x in [f for f in req_fields if f not in data]:
        return False

    data = data.split(' ')
    mapd = {}
    for d in data:
        s = d.split(':')
        mapd[s[0]] = s[1]

    validation = [
        validate_byr(int(mapd['byr'])),
        validate_iyr(int(mapd['iyr'])),
        validate_eyr(int(mapd['eyr'])),
        validate_hgt(mapd['hgt']),
        validate_hcl(mapd['hcl']),
        validate_ecl(mapd['ecl']),
        validate_pid(mapd['pid'])
    ]
    
    print(validation)

    if False in validation: return False
    return True

def count_valid_passports(data, req_fields):
    tally = 0
    for d in data:
        if validate_passport(d, req_fields): tally += 1
    return tally

# print(get_data('example.txt'))
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
print('\n')
print(count_valid_passports(get_data('example.txt'), req_fields))
print(count_valid_passports(get_data('example_invalid.txt'), req_fields))
print(count_valid_passports(get_data('example_valid.txt'), req_fields))
print(count_valid_passports(get_data('input.txt'), req_fields))
