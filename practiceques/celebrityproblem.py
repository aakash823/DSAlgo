def returncelebrity(matrix, x, y):
    #O(n)
    # while ( x < y):
    #     if matrix[x][y] == 1:
    #         x+=1
    #     else:
    #         y-=1
    # return x

    # for i in range(4):
    #     sum = 0
    #     for j in range(4):
    #         sum+=matrix[i][j]
    #     if sum==0:
    #         return i

    stack = []
    for i in range(4):
        stack.append(i)
    
    while len(stack) != 1:
        x = stack.pop()
        y = stack.pop()
        if matrix[x][y] == 1:
            stack.append(y)
        else:
            stack.append(x)
    return stack[-1]


matrix = [[0,0,1,0],[0,0,1,0],[0,0,0,0],[0,0,1,0]]
print(returncelebrity(matrix,0,len(matrix[0])-1))