class student:

    def __init__(self,name,roll):
        self.name = name
        self.roll_no = roll

    def __str__(self):
        return (f"str: The name of the student is {self.name} and Roll. No. is {self.roll_no}")

    def __repr__(self):
        return (f"repr: The name of the student is {self.name} and Roll. No. is {self.roll_no}")
    
    def info(self):
        print(f"Student Name : {self.name}")
        print(f"Student Roll. No. : {self.roll_no}")

a = student("XYZ",78)
print(str(a))
print(repr(a))

# output:
# The name of the student is XYZ and Roll. No. is 78
# repr: The name of the student is XYZ and Roll. No. is 78