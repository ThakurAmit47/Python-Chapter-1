from functools import reduce
#This is a map Example
l = [1, 2, 3, 4, 5, 6]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))

#filter Example
def even(n):
    if(n%2 == 0):
        return True
    return False
Onlyeven = filter(even, l)
print(list(Onlyeven))

#Reduce Example
def sum(a, b):
    return a + b

mul = lambda x, y: x*y
print(reduce(sum, l))
print(reduce(mul, l))
