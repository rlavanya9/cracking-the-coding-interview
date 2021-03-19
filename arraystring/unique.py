#check if string has all unique characters only using string and arrays.

# WITH STRINGS AND ARRAYS
def uniqueStr(myStr):
    prev_used = ""
    myStr = myStr.lower()
    myStr = myStr.replace(' ','')
    
    if len(myStr) > 256:
         return False
    
    for letter in myStr:
        if letter in prev_used:
            return False
        else:
            prev_used = letter
    return True


print(uniqueStr("apple"))
print(uniqueStr('least'))

#  WITH SETS
def uniqueStr2(myStr):

    myStr = myStr.lower()

    myStr = myStr.replace(" ", "")

    if len(myStr) > 256:
        return False
    else:
        return len(myStr) == len(set(myStr))

print(uniqueStr2("apple"))
print(uniqueStr2('least'))

# WITH DICTIONARY
def uniqueStr3(myStr):

    out_dict = {}
    for letter in myStr:
        out_dict[letter] = out_dict.get(letter, 0) +1

    for key in out_dict:
        if out_dict[key] > 1:
            return False
        
    return True

print(uniqueStr3("apple"))
print(uniqueStr3('least'))