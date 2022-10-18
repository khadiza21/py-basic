import numbers

from numpy import empty


numbers = [12,23,45,53,23,12,45]
print(numbers)
# set
nums = {12,23,45,53,23,12,45}
print(nums)

# set initial
empty = set()
print(empty)

numbers_set = set(numbers)
print(numbers_set)

numbers_set.add(77)
numbers_set.remove(12)
print(len(numbers_set))
