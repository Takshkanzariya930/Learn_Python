a = input("Enter Numerator: ")
b = input("Enter Denominator: ")

try:
    if type(int(a)) == int and type(int(b)) == int:
        c="int"
except ValueError:
    c="str"

if c == "str" and a == "quit":
    print("Program terminates hear")
    quit()

elif c == "str" and b == "quit":
    print("Program terminates hear")
    quit()

elif c == "str":
    raise ValueError("Input should be integer")


elif c == "int" and int(b) == 0:
    raise ValueError("Denominator should not be Zero")

print(int(a)/int(b))

# output:

'''
Enter Numerator: 44
Enter Denominator: quit
program will end hear

Enter Numerator: 22
Enter Denominator: 2
11.0

'''