# https://www.youtube.com/watch?v=sRwElQ_TOr8

# def find_diff(s,t):
#     ret = 0
#     for element in s+t:
#         ret += ret ^ ord(element)
#     return chr(ret)
    

def find_diff(s,t):
    r = 0
    for ch in s+t:
        r = r ^ ord(ch)
    return chr(r)

print(find_diff("abcd", "acbda"))
print(find_diff("abcd", "acbdx"))



