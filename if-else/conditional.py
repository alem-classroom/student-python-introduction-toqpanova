import random
num = int(input())
def is_positive(num):
    if num > 0:
        return ('true')
    else:
        return ('false')
print(is_positive(num))

def is_even(num):
    if num%2 == 0:
        return('true')
    else:
        return('false')
print(is_even(num))

def is_positive_and_even(num):
    if num>0 and num%2 == 0:
        return('true')
    else:
        return('false')
print(is_positive_and_even(num))

def is_positive_or_even(num):
    if num>0 or num%2 == 0:
        return('true')
    else:
        return('false')
print(is_positive_or_even(num))
