# python list , list methods and slice . more on lists on python
numbers = [12,33,12,54,33,33,23,62,64,33]
print(numbers[1])
print(numbers[:])
print(numbers[-6])
print(numbers[1:5])
print(numbers[1:])
print(numbers[3:])
print(numbers[3:-3])

# list [start :end :step]
print(numbers[2:7:2])
print(numbers[2:5:-1])
print(numbers[5:2:-1])
print(numbers[::-1])

# more on list
numbers.append(100)
print(numbers)

numbers.insert(4,130)
print(numbers)

numbers.remove(12)
print(numbers)

print(numbers.pop())
print(numbers)

print(numbers.count(33))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.copy()
print(numbers)

numbers.clear()
print(numbers)






