def alternate_bit(nums):
    first_bit = 0
    second_bit = 0
    while nums:
        first_bit = nums & 1
        if nums >> 1:
            second_bit = (nums >> 1) & 1
            if not first_bit ^ second_bit:
                return False
        else:
            return True
        nums = nums >> 1
    return True

print(alternate_bit(5))
print(alternate_bit(7))
print(alternate_bit(10))
print(alternate_bit(11))

