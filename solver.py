import numpy as np

data=open("exinput.txt").read().splitlines()
def par(start):
    outputmatrix=[]
    for item in start:
        line=[int(t) for t in item if t.isdigit()]
        outputmatrix.append(line)
    return outputmatrix
a=par(data)
matrix=np.array(a)
print(matrix)
#construct the nine python grids by selecting the mid point of each grid and adding adjacent numbers
def find_grid(arr):
    grid = []
    for i in range(len(arr)):
        for j, value in enumerate(arr[i]):
            if (i==1 or i%3 ==1) and (j==1 or j%3==1):
                new_neighbors = []
                new_neighbors = [
                    arr[i][j],
                    arr[i - 1][j],  
                    arr[i][j + 1], 
                    arr[i + 1][j],  
                    arr[i][j - 1],  
                    arr[i+1][j+1],
                    arr[i+1][j-1],
                    arr[i-1][j+1],
                    arr[i-1][j-1]
                    ]
                grid.append(new_neighbors)
    return grid

#find next empty space
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

#check grid, columns, and rows
def validity(arr,num,pos):
    loc=0
    posx,posy=pos
    if posx in [0,1,2]: loc+=3
    elif posx in [3,4,5]:loc+=6
    elif posx in [6,7,9]:loc+=9
    if posy in [0,1,2]: loc-=3
    elif posy in [3,4,5]: loc-=2
    elif posy in [6,7,8]:loc-=1
    grid=find_grid(arr)
    if num in grid[loc]: return False
    for i in range(len(arr)):
        if i == posx and num in arr[i]: return False
        for j in range(len(arr[i])):
            if j == posy and arr[i][j]==num: return False
    return True

#appends one, then finds the next empty one :()
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if validity(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

solve(a)
matrix=np.array(a)
print(matrix)