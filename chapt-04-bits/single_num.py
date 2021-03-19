def single_occ(nums):
    ret = 0
    for num in nums:
        ret = ret ^ num
    return ret

print(single_occ([2,2,3,4,3]))


