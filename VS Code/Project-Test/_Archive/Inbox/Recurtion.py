def factorial(a):
    if a == 0 or a == 1:
        return(1)
    else:
        return(a * factorial(a-1))

inp = int()(input("Enter number to calculate factorial: "))
b = factorial(inp)
print(b)