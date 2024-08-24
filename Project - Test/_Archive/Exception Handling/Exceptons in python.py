a = input("Enter your number: ")

for i in range(1,11):
    print(f"{a} X {i} = {a*i}")

# output:
# Enter your number: q
# ValueError: invalid literal for int() with base 10: 'q'