a = 36 #Global Variable

def hello():
    a = 7
    b = 43   
    print("hello",b)
    print(a+b)

hello()
print(a)

def hello2():
    global a
    a = 7
    b = 43   
    print("hello",b)
    print(a+b)

hello2()
print(a)
# print(b) #Will throw an error

# output:
# hello 43
# 50
# 36