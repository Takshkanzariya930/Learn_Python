class student:
    def __init__(self,na,no):
        self.name = na  # | This two Variables can be accessed from any
        self.roll = no  # | where this are called public variables.

    def info(self):
        print(f"Roll No, = {self.roll} : Name = {self.name}")

class class12th(student):
    def info12th(self):
        print(f"Roll No (12th) = {self.roll} : Name (12th)= {self.name}")

a = student("XYZ",23)
a.info()             # |  Here we can access name(var), roll(var) 
print(a.name,a.roll) # |  and info(method).

b = class12th("ABC",33)
b.info12th()         # |  subclass can also access public variables

# output:
# Roll No, = 23 : Name = XYZ
# XYZ 23