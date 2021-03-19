def reverse_bit(nums):
    i = 0
    m= 0
    while i < 32:
        m = m << 1 + (nums & 1) 
        nums >> 1
        i += 1
    return m
