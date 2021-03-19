def single_num(nums):
    ones = 0
    twos = 0
    for num in nums:
        ones = (num ^ ones) & ~twos
        twos = (num ^ ones) & ~ones
    return ones
#
#  def single_num(nums):
#     ones, twos = 0, 0
#     for i in range(len(nums)):
#         print(nums[i])
        # ones = (ones ^ nums[i]) & ~twos
        # twos = (twos ^ nums[i]) & ~ones
    # return ones

print(single_num([3,3,3,4,5,5,4,4,5,6]))
