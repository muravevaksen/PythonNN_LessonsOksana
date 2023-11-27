def merge_arrays(first, second):
    return sorted(list(set(second) | set(first)))

print(merge_arrays([1, 3, 4, 7], [-1, 2, 3, 7, 8, 9]))

def hero(bullets, dragons):
    return True if dragons*2 <= bullets else False

print(hero(65, 29))