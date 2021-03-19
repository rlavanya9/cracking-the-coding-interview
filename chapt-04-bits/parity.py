def count_bits(nums):
    count = 0
    val = nums
    while nums: 
        if nums & 1:
            count += 1
        nums = nums >> 1
     
    
    if (count % 2) != 0:
        return val | (1 << 8)
    
    return val

print(count_bits(1))
print(count_bits(5))