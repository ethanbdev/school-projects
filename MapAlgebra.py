import numpy as np

def subtract(left, right):
    # initialize a new list the same size as left with a 0 for all the elements using list comprehension (python documentation)
    newL = [[0 for i in range(len(left))] for j in range(len(left[0]))]
    # iterate the list by row then column with i and j acting as indices
    for i in range(0, len(left)):
        for j in range(0, len(left[0])):
            newL[i][j] = right[i][j] - left[i][j]
    return newL

def multiply(left, right):
    newL = [[1 for i in range(len(left))] for j in range(len(left[0]))]
    for i in range(0, len(left)):
        for j in range(0, len(left[0])):
            newL[i][j] = right[i][j] * left[i][j]
    return newL

def divide(left, right):
    newL = [[1 for i in range(len(left))] for j in range(len(left[0]))]
    for i in range(0, len(left)):
        for j in range(0, len(left[0])):
            newL[i][j] = right[i][j] / left[i][j]
    return newL

# pointlists to input into the functions:
left = [[2,4,5], [5,1,1], [10,3,7]]
right = [[1,3,7], [6,8,9], [2,2,2]]

print(subtract(left, right))
print(multiply(left, right))
print(divide(left, right))

//now use numpy
def subtract(left, right):
    return right - left

def multiply(left, right):
    return right * left

def divide(left, right):
    return right / left

# arrays to input into functions (pointlists):
left = np.array([[2,4,5], [5,1,1], [10,3,7]])
right = np.array([[1,3,7], [6,8,9], [2,2,2]])

print(subtract(left, right))
print(multiply(left, right))
print(divide(left,right))