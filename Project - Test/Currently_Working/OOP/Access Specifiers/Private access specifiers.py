class student:
    def __init__(self,na,no):
        self.__name = na # | Declaring name and roll private 
        self.__roll = no # | attributes(variables)

    def __info(self): # | Declaring info(function) private attributes
        print(f"Roll No, = {self.roll} : Name = {self.name}")

class class12th(student):
    def info12th(self):
        print(f"Roll No (12th) = {self.roll} : Name (12th)= {self.name}")


a = student("XYZ",23)
a.info()             # |  We cn not directly access name(var), roll(var) 
print(a.name,a.roll) # |  and info(method).

b = class12th("ABC",33)
b.info12th()         # |  subclass can not access private variables

# output:
# AttributeError: 'student' object has no attribute 'info'
# AttributeError: 'class12th' object has no attribute 'roll'