def stairs(n):
    if n <= 1:
        return 1
        
    if n > 1:
        return stairs(n-1) + stairs(n-2)
# def stairs(term):
#    if term <= 1:
#        return 1
#    else:
#        return (stairs(term-1) + stairs(term-2))

print(stairs(3))
print(stairs(2))
print(stairs(38))