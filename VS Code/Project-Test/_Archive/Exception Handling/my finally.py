
def table():
    try:
        a = int(input("Enter your number: "))
        b = [32,a,34,22,7,88]
        return(b[a])

    except ValueError:
        print("This program only accepts integer as input.")

    finally:
        print("Program ends hear") #If i have written this without finally this would not run,
                                   #because when error happens and interpreter jumps to except block

c = table()
print(c)

# output:
# Enter your number: d
# This program only accepts integer as input.
# Program ends hear
# None