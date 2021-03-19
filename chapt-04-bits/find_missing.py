def find_missing(myarr):
    init = 0
    sn = list(range(len(myarr)+1))
    print(sn)
    for element in myarr + sn:
        init = init ^ element
    return init

print(find_missing([0,1,2,3,5]))
