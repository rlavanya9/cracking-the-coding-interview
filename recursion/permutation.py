def perm(remaining, candidate=""):
    if len(remaining)==0:
        print(candidate)
    
    for i in range(len(remaining)):
        newcandidate = candidate + remaining[i]
        newremain = remaining[0:i] + remaining[i+1:]

        perm(newremain, newcandidate)

if __name__ == '__main__':
 
    s = "ABC"
    perm(s)