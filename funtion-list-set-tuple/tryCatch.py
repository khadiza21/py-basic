# py have so exception explore it
try:
    num = 12/0
    print(num)
except:
    print('Something went wrong')
finally:
    print('This is done')