def insert_m_bits(m,n,i,j):
    capture_bits = (1<<i) -1
    clear_bits = -1 << (j+1)

    capture_bits = n & capture_bits
    n = n & clear_bits

    m = m << i
    n = m | n
    n = n | capture_bits

    return n

print(insert_m_bits(8, 1201, 3, 6))
