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
    
a = student("DEF",97)
a.info()

b = student.for_string("ABC-43")
b.info()

# output:
# Student Name : DEF
# Student Roll. No. : 97
# Student Name : ABC
# Student Roll. No. : 43