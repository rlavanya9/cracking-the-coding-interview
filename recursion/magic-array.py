# def magic_array(myarr):
#     return magic_array_helper(myarr, 0)

# def magic_array_helper(myarr, i):
#     if not myarr:
#         return -1

#     while myarr:    
#         if myarr[i] == i:
#             return i
#         magic_array(i+1)

def magic_array(myarr, low, high):
    if high >= low:
        mid = (low+high)//2

    if myarr[mid] == mid:
        return mid
    
    if myarr[mid] < mid:
        return magic_array(myarr, mid+1, high)

    elif myarr[mid] > mid:
        return magic_array(myarr, low, mid-1)
    else:
        return -1

arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100] 
n = len(arr) 
print("Fixed Point is " + str(magic_array(arr, 0, n-1))) 

# print(magic_array([-10, -5, 0, 3, 7]))
# print(magic_array([0, 2, 5, 8, 17]))
# print(magic_array([-10, -5, 3, 4, 7, 9]))
