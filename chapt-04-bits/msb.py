def msb_set(nums):
    i = 0
    bit = False
    while nums:
        if (1 & nums):
            bit = True
        i += 1
        nums = nums >> 1
    
    if bit:
        return i - 1
    else:
        return 0

        

        

print(msb_set(0))
print(msb_set(7))
print(msb_set(5))