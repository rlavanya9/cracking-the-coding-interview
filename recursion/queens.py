# def is_safe(mat,row,col):
#     for i in range(col):
#         if mat[row][i] == 1:
#             return False
    
#     for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
#         if mat[i][j] == 1:
#             return False
    
#     for i,j in zip(range(row,n,1), range(col,-1,-1)):
#         if mat[i][j] == 1:
#             return False
    
#     return True
def possible(grid,y,x):

    l = len(grid)

    for i in range(l):
        if grid[y][i] == 1:
            return False
    
    for i in range(l):
        if grid[i][x] == 1:
            return False
    
    for i in range(l):
        for j in range(l):
            if grid[i][j] == 1:
                if abs(i-y) == abs(j-x):
                    return False
    return True



def solve(grid):
    l = len(grid)

    for y in range(l):
        for x in range(l):
            if grid[y][x] == 0:
                if possible(grid,y,x):
                    grid[y][x] == 1
                    solve(grid)
                    if sum(sum(a) for a in grid) == l:
                        return grid
                    grid[y][x] = 0
    return grid


# Solution = solve(copy.deepcopy(grid)) #get the solution
# print(np.matrix(Solution)) #Print the solution

# def possible(grid,y,x): #is it possible to place a queen into y,x?

#     l=len(grid) #how big is our grid?
    
#     for i in range(l): #check for queens on row y
#         if grid[y][i]==1: #if exist return false
#             return False
#     for i in range(l):  #check for queens on column x
#         if grid[i][x]==1: #if exists return 0
#             return False
        
#     for i in range(l): #loop through all rows
#         for j in range(l): #and columns
#             if grid[i][j]==1: #if there is a queen
#                 if abs(i - y) == abs(j - x): #and if there is another on a diagonal
#                     return False #return false
#     return True #if every check clears, we can return true

# def solve(grid):
    
#     l=len(grid) #length of our grid  
    
#     for y in range(l): #for every row
#         for x in range(l): #for every column
#             if grid[y][x]==0: # we can place if there is no queen in given position
#                 if possible(grid,y,x): #if empty, check if we can place a queen
#                     grid[y][x]=1 #if we can, then place it
#                     solve(grid) #pass grid for recursive solution
#                     #if we end up here, means we searched through all children branches
#                     if sum(sum(a) for a in grid)==l: #if there are 8 queens
#                         return grid #we are successful so return
#                     grid[y][x]=0 #remove the previous placed queen


#     return grid #means we searched the space, we can return our result

grid=[[0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0]]

print(solve(grid))