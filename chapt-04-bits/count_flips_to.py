def count_flips_to_num(num1, num2):

    diff = num1 ^ num2
    count = 0
    while diff:
        diff = diff & (diff-1)
        count += 1
    return count

print(count_flips_to_num(29,15))