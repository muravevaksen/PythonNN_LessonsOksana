# Write a function that accepts an integer n and a string s as parameters,
# and returns a string of s repeated exactly n times

def repeat_str(repeat, string):
    return repeat * str(string)

print(repeat_str(4, 'abc'))

# Write a function that removes the spaces from the string, then return the resultant string

def no_space(x):
    return x.replace(' ', '')

print(no_space('привет, как     дела 4увалы ффф'))

# Write a function which converts the input string to uppercase

def make_upper_case(s):
    return s.upper()

print(make_upper_case('It\'s okay'))