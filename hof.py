#Diego Lopez hof
from functools import reduce


def uniq(lst):
    
    result = []

    [result.append(x) for x in lst if x not in result] #add to array and check

    return result
    

def find_max(matrix):
    
    return reduce(lambda x,y : x if x > y else y, [num for submatrix in matrix for num in submatrix])


def count_ones(matrix):
    x = 0
    count = 0
    for num in matrix:
        for num1 in matrix[x]:
            if num1 == 1:
                count += 1
        x += 1


    return count



def addgenerator(x):
    return lambda y : x + y #add x to a value


def apply_to_self():
     return lambda x, y: x + y(x) 


def map2(matrix,f):
    return [[f(x) for x in row] for row in matrix]


