class student:
    def __init__(self,name,roll):
        self.name = name
        self.roll_no = roll

    def info(self):
        print(f"Student Name : {self.name}")
        print(f"Student Roll. No. : {self.roll_no}")

class std12th(student):
    def __init__(self,name,roll,marks):
        super().__init__( name,roll)
        self.marks = marks

    def info12th(self):
        super().info()
        print(f"Student Marks : {self.marks}")

a = student("xyz",43)
a.info()

b = std12th("ABC",56,100)
b.info12th()

# output:
# Student Name : xyz
# Student Roll. No. : 43

# Student Name : ABC
# Student Roll. No. : 56
# Student Marks : 100