def swap(nums):
    odd = (nums & int('AAAAAAAA', 16)) >> 1
    even = (nums & int('55555555', 16)) << 1
    return odd|even

print(swap(22))
print(swap(41))
