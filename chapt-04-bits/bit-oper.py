# https://www.youtube.com/watch?v=HWTnwZQmhpc

def set_bit(num,i):
    return num | (1 << i)

def clear_bit(num,i):
    return num & ~(1 << i)

def toggle_bit(num, i):
    return num ^ (1 << i)

def get_bit(num, i):
    return num & (1 << i)

def update_bit(num, i, bit):
    num & ~(1<<i) | (bit << i)



