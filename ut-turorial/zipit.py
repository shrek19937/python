# python program to demonstrate
# unique combination of two lists
# using zip() and permutation of itertools
 
# import itertools package
import itertools
from itertools import permutations
from itertools import product
 
# initialize lists
list_1 = ["a", "b", "c","d"]
list_2 = [1,4,9]
 
print( list (itertools.product(list_1,list_2)))

keyboards = [ 3, 1 ]
drives = [ 5, 2, 8 ]
permut = itertools.product(keyboards, drives)

#list = [(3, 5), (3, 2), (3, 8), (1, 5), (1, 2), (1, 8)]
cl = [ i[0] + i[1] for i in permut]
print(cl)

def cartesian_product(arr1, arr2):
 
    # return the list of all the computed tuple
    # using the product() method
    return list(product(arr1, arr2))
   
# Driver Function
if __name__ == "__main__":
    arr1 = [1, 2, 3]
    arr2 = [5, 6, 7]
    p = cartesian_product(arr1, arr2)
    print(type(p), len(p), p)

def getMoneySpent(keyboards, drives, s):
        return max([ sum([x,y]) for x in keyboards for y in drives if sum([x,y]) <= s] + [-1])

def gradingStudents(grades):
    #return [ i if (i < 38 or i % 5 < 3) else (i + (5 - i%5)) for i in grades]
    #return [ i for i in grades if (i < 38 or i % 5 < 3) ]
    return [ i if (i < 38 or i % 5 < 3) else (i + (5 - i%5)) for i in grades  ]