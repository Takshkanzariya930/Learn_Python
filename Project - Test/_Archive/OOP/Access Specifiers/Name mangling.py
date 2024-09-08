class student:
    def __init__(self,na,no):
        self._name = na # | name can be mangled.
        self.__roll = no # | Declaring roll(variable) Non mangled attributes.

    def __info(self): # | Declaring info(function) Non mangled attributes.
        print(f"Roll No, = {self.roll} : Name = {self.name}")

a = student("XYZ",23)
print(a._name) # | mangled attributes can be accessed directly.

a.__info()      # | non mangled attributes can not be
print(a.__roll) # | accessed "directly".

print(a._student__roll) # | non mangled attributes can be accessed "indirectly".

# output:
# XYZ
# AttributeError: 'student' object has no attribute '__info'
# 23