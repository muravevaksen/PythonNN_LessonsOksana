def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    elif boolean == False:
        return "No"

print(bool_to_word(True))

def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print((even_or_odd(5)))

def make_negative( number ):
    if number > 0:
        return number*(-1)
    else:
        return number

print((make_negative(-5)))

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

print((basic_op('-', 15, 18)))