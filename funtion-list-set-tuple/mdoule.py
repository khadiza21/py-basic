from unittest import result
#import file type 01
# import function
# sum = function.add(45,56)
# print('Sum in modules.py ', sum)
# result = function.multiply(12,3)

#import file type 02
from function import add, multiply 
#import file type 03
from function import *
res = add(56,89)
print('result in modules.py ', res)
