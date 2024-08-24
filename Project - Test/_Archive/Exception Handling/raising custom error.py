a = input("Enter Numerator: ")
b = input("Enter Denominator: ")

if int(b) == 0:
    raise ValueError("Denominator should not be Zero")
print(int(a)/int(b))

# output:

'''
Enter Numerator: 10
Enter Denominator: 0
Traceback (most recent call last):
  File "c:\Coding\VS Code\Project-Test\Exception Handling\raising custom error.py", line 5, in <module>
    raise ValueError("Denominator should not be Zero")
ValueError: Denominator should not be Zero
'''