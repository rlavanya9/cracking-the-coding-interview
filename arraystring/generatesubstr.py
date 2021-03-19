def generate_substr(mystring):
    for i in range(len(mystring)):
        for j in range(i+1, len(mystring)+1):
            print(mystring[i:j])



print(generate_substr('great life'))
