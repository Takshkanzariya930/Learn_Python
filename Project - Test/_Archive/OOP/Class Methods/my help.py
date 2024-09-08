class student:

    def __init__(self,name,roll):
        self.name = name
        self.roll_no = roll

    def info(self):
        print(f"Student Name : {self.name}")
        print(f"Student Roll. No. : {self.roll_no}")

    @classmethod
    def for_string(cls,x):
        return cls(x.split("-")[0],int(x.split("-")[1]))
    
help(student)

# output:
''''
class student(builtins.object)
 |  student(name, roll)
 |
 |  Methods defined here:
 |
 |  __init__(self, name, roll)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  info(self)
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  for_string(x)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 '''