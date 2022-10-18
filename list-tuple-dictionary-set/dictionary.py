marks = {'math':98,'chemistry':87,'biology':34 }

marks['math'] = 99
marks['english'] = 70
del marks['chemistry']

print(marks)

marks_keys = marks.keys()
print(marks_keys)

marks_values = marks.values()
print(marks_values)

marks_items = marks.items()
print(marks_items)

marks.clear()
print(marks)