
try:
    a = int(input("Enter your number: "))

    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")

except ValueError:
    print("This program only accepts integer as input.")

# output:
# Enter your number: a
# This program only accepts integer as input.