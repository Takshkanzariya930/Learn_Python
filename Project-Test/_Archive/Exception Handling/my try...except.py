
try:
    a = int(input("Enter your number: "))

    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")

except Exception as e :
    print(e)

# output:
# Enter your number: d
# invalid literal for int() with base 10: 'd'