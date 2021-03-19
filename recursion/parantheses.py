def paren(s,n):
    return paren_helper(s,0,n,0,0)

def paren_helper(s,pos,n,open,close):

    if (close == n):
        for i in s:
            print(i, end="")
        print()
        return
    else:
        if (open > close):
            s[pos] = ")"
            paren_helper(s,pos+1,n,open,close+1)
        
        if (open < n):
            s[pos] = "("
            paren_helper(s,pos+1,n,open+1,close)

n = 3; 
s = [""] * 2 * n; 
paren(s, n); 
