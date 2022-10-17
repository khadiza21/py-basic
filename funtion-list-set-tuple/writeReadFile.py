with open('message.txt','a') as fileWrite:
    fileWrite.write("\nHello BK!!\n")

with open('message.txt','r') as fileRead:
    text = fileRead.read()
    print(text)