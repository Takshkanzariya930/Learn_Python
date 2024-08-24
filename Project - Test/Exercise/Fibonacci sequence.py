def FS(a):
    if a == 0 :
        return(0)
    elif a == 1:
        return(1)
    else:
        return(FS(a-1)+FS(a-2))

c = int(input("Enter the number of term you need to find: "))
b = FS(c)
print(b)

# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8.....