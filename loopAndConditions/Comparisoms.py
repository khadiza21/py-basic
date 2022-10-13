from turtle import Turtle


print(12<35)
print(43<23)
print(12>35)
print(43>23)

# conditions
price =234

# multiple conditions
if price < 150: 
    print("Too much")
elif price<124:
    print("Reasonable")
else:
    print("Normal")


# nested conditions
salary = 2333
has_flat=True
if( salary > 2344):
    if has_flat == True:
       print('ok fine')
    else: 
        print("sad for you")
else:
    print("don't be sad")


#  
exam = 'BSc'
passed = False
if exam == 'BSc' and passed == True:
    print("Done")
else:
    print("Remain")





