def multiply(a, b):
    return  a*b

print(multiply(1,2))

def high_and_low(numbers):
    lst = [int(i) for i in numbers.split(" ")]
    return f'{max(lst)} {min(lst)}'

print(high_and_low("16 2 3 4 5"))