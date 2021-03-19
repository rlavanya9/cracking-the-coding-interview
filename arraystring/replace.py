# given a string, replace its spaces with '%20'
# method 1 - with rstrip and replace
def replace_blank(myStr):
    myStr = myStr.rstrip()
    myStr = myStr.replace(" ",'%20')
    return myStr

print(replace_blank("Mr John Smith   "))
print(replace_blank('much ado about nothing      '))

# method 2 - without replace method

def replace_blank2(myStr):
    myStr = myStr.rstrip()
    new_word = ""
    for letter in myStr:
        if letter == " ":
            new_word += '%20'
        else:
            new_word += letter
    return new_word

print(replace_blank2("Mr John Smith   "))
print(replace_blank2('much ado about nothing      '))

# method 3 - using split and join methods.

# def replace_blank3(myStr):
#     myStr = myStr.split()
#     print(myStr)
#     for letter in myStr:
#         if letter == " ":
#             letter = '%20'
#     return "".join(myStr)

# print(replace_blank3("Mr John Smith   "))
# print(replace_blank3('much ado about nothing      '))