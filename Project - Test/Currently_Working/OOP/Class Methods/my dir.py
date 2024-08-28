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
    
print(dir(student))

# output:
''''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__le__', '__lt__','__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__','__repr__',
 '__setattr__', '__sizeof__','__str__','__subclasshook__', '__weakref__', 'for_string', 'info']
 '''