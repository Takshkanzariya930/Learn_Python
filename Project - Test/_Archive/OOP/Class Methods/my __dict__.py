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
    
a = student("xyz",43)
print(a.__dict__)

# output:
# {'name': 'xyz', 'roll_no': 43}