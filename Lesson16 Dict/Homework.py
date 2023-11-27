def opposite(number):
    return number*(-1)

print(opposite(-34))

def count_sheeps(sheep):
    return sum([1 for x in sheep if x == True])

print(count_sheeps([True,  True,  True,  False,
                    True,  True,  True,  True ,
                    True,  False, True,  False,
                    False,  False, False, True ,
                    True,  True,  True,  True ,
                    False, False, True,  True]))

def maps(a):
    return [x*2 for x in a]

print(maps([1, 2, 3]))

