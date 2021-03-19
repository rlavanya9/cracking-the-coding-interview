def binary_gap(x):

    # 10110
    start = False
    gap = 0
    ans = 0
    if isinstance(x,int):
        # if x <= max and x >= min:
        bin_x = bin(x)
        str_bin_x = str(bin_x)
        for element in str_bin_x:
            if element == '1':
                if start == False:
                    start = True
                else:
                    if gap > ans:
                        ans = gap
                    gap = 0
            else:
                if start == True:
                    gap += 1
        return ans
    # return bin_x
print(binary_gap(529))

