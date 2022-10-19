# list
numbers = [12,23,53,64,34,89,29,51]
total = sum(numbers) # built in function in python sum()
print('list sum by built in sum function ',total)


total1 = 0
for i in numbers:
    total1 += i
    print(i)
print('list sum by loop ',total1)


# list loop through with index and value
for i,num in enumerate(numbers):
    print(num)
# list loop through with index and value
for i,num in enumerate(numbers):
    print(i,num)
# list loop through with index and value
for num in enumerate(numbers):
    print(num)

# set
nums = {12,23,45,53,23,12,45}
total2 = 0
for num in nums:
    total2 += num
print('set element summation by loop ',total2)

# tuple
numbers_tuple = 12, 23,34,63,62,90,23
total3 = 0
for num in numbers_tuple:
    total3 += num
print('tuple element summation by loop ',total3)


#dictionary 
# looping type 01
marks = {'math':98,'chemistry':87,'biology':60 ,'english': 89}
for mark in marks:
    val = marks[mark]
    print(mark,val)

# looping type 02
for subject, mark in marks.items():
    print(subject,mark)





