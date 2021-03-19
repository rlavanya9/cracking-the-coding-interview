def count_money(n):
    countHelper(n, "Quarter")
 
def countHelper(n, tyoe):
    count = 0
    sum = 0
    if tyoe == "Quarter":
        while n > count*25:
           sum+= countHelper(n - count*25, "Dime")
    elif tyoe == "Dime":
        while n > count*10:
            sum+=countHelper(n - count*10, "Nickel")
    elif tyoe == "Nickel":
        while n > count*5:
            sum+=countHelper(n - count*5, "Penny")
    elif tyoe == "Penny":
        return 1
    
    return sum 

# def count_money(n):
#     return count_helper(n, 'quarter')

# def count_helper(n, types):
#     sum = 0
#     count = 0
#     if types == 'quarter':
#         while n > count*25:
#             sum += count_helper(n - count*25, 'dime')
#     elif types == 'dime':
#         while n > count*10:
#             sum += count_helper(n - count*10, 'nickel')
#     elif types == 'nickel':
#         while n > count*5:
#             sum += count_helper(n - count*5, 'penny')
#     elif types == 'penny':
#         return 1
    
#     return sum

print(count_money(5))