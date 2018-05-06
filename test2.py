# Author: nhascup
# 05/05/2018
# Python Refresh

def add(x, y):
    return x + y


def absoluteValue(number):
    if number < 0:
        return number * -1
    return number


result1 = add(1234, 5678)
print(result1)
result2 = add(-1.5, .5)
print(result2)
print("The total sum is", result1 + result2)
