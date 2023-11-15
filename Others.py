#def move_zeros(lst):
#    count = 0
#    listt = []
#    for i in range(0, len(lst)):
#        if lst[i] == 0:
#            count += 1
#        else:
#            listt.append(lst[i])
#    for i in range(0, count): listt.append(0)
#    return listt

#print(move_zeros([1, 0, 1, 2, 0, 1, 3, 0, 5]))

def count(s):
    lstt = {}
    for i in range(0, len(s)):
       lstt.update(s[i], i)
    return lstt

print(count('aba'))