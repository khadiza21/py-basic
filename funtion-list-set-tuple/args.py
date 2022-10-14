# args (tuple)
def multiply_args(*numbers):
    result = 1
    for num in numbers:
        result = result * num
    return result

final_result = multiply_args(2,3,2,3,4,2,2)
print(final_result)

#2 
def add(num1,num2,num3,*numbers):
    print(num1,num2,num3)
    print(numbers)
add(3,4,2,3,1,5,15)

# 3
def full_name(f_name, l_name):
    name = f'{f_name} {l_name}' 
    return name
name = full_name(l_name='Khadiza' , f_name='Vhuiya')
print(name)

# kargs (dictionary )
def long_name(**kargs):
    print(kargs)
long_name(first = 'Dr. ', last = 'Chowdhury', middle = 'Rahman')

def name_mixed (first, last, **name_parts):
    print(first, last, name_parts);
fullname = name_mixed(first='khadiza',last='vhuiya', middle='bint',father='abdul mazid')

# tupple and dic , normal
def all_types (first, *args, **kargs):
    print(first)
    print(args)
    print(kargs)
all_types('abc','bcd', 'kjk', 'lll', name='abul', father='babul')
