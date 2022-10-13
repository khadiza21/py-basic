# function 
def double_it(num):
    result = num* 2
    print(result)
double_it(4)

def add(num1,  num2):
    total = num1+ num2
    return (total)
sum = add(23,17)

# return function 
def multiply (num1, num2):
    result1 = num1 * num2
    return result1
output = multiply(2,4)
print(output)


# function reusability
print('final number ', add(sum, output) )



# optional parameters and args
def addition(num1, num2=0, num3=1, num4 = 2):
    total = num1 + num2
    print (num1, num2)
    return total


result2 = addition(12,14)
result3 = addition(num2=12, num1 = 14)
result4 = addition(45)

# args
def multiply_args(*numbers):
    result = 1
    for num in numbers:
        result = result * num
    return result

final_result = multiply_args(2,3,2,3,4,2,2)
print(final_result)


