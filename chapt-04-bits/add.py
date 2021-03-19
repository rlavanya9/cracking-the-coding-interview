# https://www.youtube.com/watch?v=qq64FrA2UXQ

def add_bitwise(x,y):
    while y:
        carry = x & y
        x = x^y
        y = carry << 1
    return x