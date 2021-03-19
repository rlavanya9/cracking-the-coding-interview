# https://www.youtube.com/watch?v=e0sVe4-JJJI
def count_set_bits(num):
    count = 0
    while num:
        num = num & (num-1)
        count += 1
    return count

print(count_set_bits(10))
