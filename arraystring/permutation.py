# check permutation of two strings
# permutation is 2 string with same characters in different order
def permutation(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    letter_dict = {}
    letter_dict2 = {}
    if len(str1) != len(str2):
        return False
    else:
        for letter in str1:
            letter_dict[letter] = letter_dict.get(letter, 0) + 1
        for letter2 in str2:
            letter_dict2[letter2] = letter_dict2.get(letter2, 0) + 1
        for key,value in letter_dict2.items():
            if key in letter_dict and value == letter_dict[key]:
                continue
            else:
                return False
        return True    


print(permutation('abcd', 'bdca'))
print(permutation('abcd', 'bbca'))
print(permutation('2354', '1234'))
print(permutation('dcw4f', 'dcw5f'))

def permute2(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    letter_count = {}

    for letter in str1:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    for letter2 in str2:
        if letter2 not in letter_count:
            return False
        elif letter_count[letter2] <= 0:
            return False
        else:
            letter_count[letter2] -= 1
        
    return True

print(permute2('abcd', 'bdca'))
print(permute2('abcd', 'bbca'))
print(permute2('2354', '1234'))
print(permute2('dcw4f', 'dcw5f'))    