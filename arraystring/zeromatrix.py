def zero_matrix(matrix):
    value_i = []
    value_j = []
    for i in range(len(matrix)):
        # print(range(i))
        # print(range(len(matrix[0])))
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                value_i.append(i) 
                value_j.append(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in value_i or j in value_j:
                matrix[i][j] = 0
            # if j in value_j:
            #     matrix[j] = 0
    return matrix    


print(zero_matrix([[1,2,3], [4,0,6], [7,8,9]]))
print(zero_matrix([[1,0,3], [4,5,6], [0,8,9]]))