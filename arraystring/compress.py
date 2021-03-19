#  aabcccccaaa should be a2b1c5a3. if original string is smaller than compressed version, return original

# def compress(myStr):

#     letter_count = {}
#     out_lst = []
#     for letter in myStr:
#         letter_count[letter] = letter_count.get(letter, 0) + 1
#     for k,v in letter_count.items():
#         out_lst.append(k+str(v))
#     return "".join(out_lst)

# print(compress('aabcccccaaa'))

def compress2(myStr):
    out_word = ""
    lc = 0
    prev_letter = ""
    for letter in myStr:

        if letter == prev_letter:
            lc += 1
        else:             
            if lc != 0: 
                out_word += prev_letter + str(lc)
            prev_letter = letter
                # lc = 1
            lc = 1
    out_word += prev_letter + str(lc)                    
    if len(out_word) > len(myStr):
        return myStr
    else:
        return out_word

print(compress2('aabcccccaaa'))
print(compress2('abcdef'))
