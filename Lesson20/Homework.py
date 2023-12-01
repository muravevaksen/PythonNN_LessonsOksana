def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
        else: pass
    return sum

print(positive_sum([1,-4,7,12]))

def string_to_number(s):
    return int(s)

print(string_to_number('-7'))

def abbrev_name(name):
    initials = str(name[0])
    for i in range(1, len(name)+1):
        if name[i-1] == ' ':
            initials += f'.{name[i]}'
    return initials.upper()

print(abbrev_name('patrick feeney'))