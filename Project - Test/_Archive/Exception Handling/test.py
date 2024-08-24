a = input(":::::  ")
print(a)
print(type(a))

try:
    if type(int(a)) == int:
        print("int")
    elif type(a) == str:
        print("str")
    c=0
except ValueError:
    c=1

print(c)