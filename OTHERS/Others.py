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

#def count(s):
#    lstt = {}
#    for i in range(0, len(s)):
#       lstt.update(s[i], i)
#    return lstt

#print(count('aba'))

#The marketing team is spending way too much time typing in hashtags.
#Let's help them with our own Hashtag Generator!
#Here's the deal:
#It must start with a hashtag (#).
#All words must have their first letter capitalized.
#If the final result is longer than 140 chars it must return false.
#If the input or the result is an empty string it must return false.

def generate_hashtag(s):
    s = s.title()
    s = s.replace(' ', '')
    if len(s)+1 > 140: return False
    elif len(s) == 0: return False
    else:
        return f'#{s}'


print(generate_hashtag('ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqqq'))