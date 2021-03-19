#  check if a string is palindrome by comparing the first and the last letters till mid
def palindrome(myStr):
    mid = (len(myStr) // 2 )
    left = myStr[:mid]
    right = myStr[mid+1:]
    i = 0
    j = -1

    while i < len(left) and j < len(right) :
        if left[i] == right[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

print(palindrome('malayalam'))
print(palindrome('top'))
print(palindrome('apple'))
print(palindrome('kayak'))
print(palindrome('dad'))

#  check if palindrome if all occurance of letters in word is even except for 1 letter with single occurence
def palindrome2(myStr):
    letter_count = {}
    even_count = 0
    odd_count = 0
    for letter in myStr:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    for key,value in letter_count.items():
        if value%2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if odd_count <= 1:
        return True
    else:
        return False
         

print(palindrome2('malayalam'))
print(palindrome2('top'))
print(palindrome2('apple'))
print(palindrome2('kayak'))
print(palindrome2('dad'))

