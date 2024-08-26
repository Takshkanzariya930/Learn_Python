class student:
    def __init__(self,na,no):
        self.name = na
        self.roll = no

    def _info(self): #Protected Method
        print(f"Roll No, = {self.roll} : Name = {self.name}")

class class12th(student):
    pass


a = student("XYZ",23)
print(a.roll)
a._info()

b = class12th("ABC",33)
print(b.roll)
b._info()

# output:
# 23
# Roll No, = 23 : Name = XYZ
# 33
# Roll No, = 33 : Name = ABC