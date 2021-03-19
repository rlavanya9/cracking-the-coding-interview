def substr(str1):
    res = [str1[i:j] for i in range(len(str1))
            for j in range(i+1, len(str1)+1)]
    return res

print(substr("Geeks"))