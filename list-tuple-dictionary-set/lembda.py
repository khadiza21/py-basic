from unittest import result
from numpy import square

# lambda
square = lambda x: x*x
result = square(6)
print(result)

add = lambda x,y :x+y
sum = add(45,64)
print(sum)

# lambda , list , map
numbers = [12,33,12,54,33,33,23,62,64,33]

double_it = lambda x:x*2
double_numbers = map(double_it,numbers)
squared_numbers = map(lambda x: x*x, numbers)
print("doubled numbers ",list(double_numbers))
print("squared numbers ",list(squared_numbers))

# lambda , list , filter
bigger_numbers = filter(lambda num: num > 50, numbers)
print(list(bigger_numbers))


# lambda , dictionary , filter
books = [ 
    {'name':'ghost','price':230},
    {'name':'chemistry','price':20},
    {'name':'math','price':30},
    {'name':'islamic','price':330},
    {'name':'historical','price':50},
    {'name':'scientific','price':430},
    {'name':'horrible','price':290},
]
cheapest_books = filter(lambda book: book ['price']<100, books)
print('Cheapest books ',list(cheapest_books))


