class student:

    def __init__(self,name,roll):
        self.name = name
        self.roll_no = roll

    def En_no(self):
        return (f"S.{self.roll_no}.24")

    def info(self):
        print(f"Student Name : {self.name}")
        print(f"Student Roll. No. : {self.roll_no}")

class std12th(student):

    def __init__(self, name, roll):
        super().__init__(name, roll)

    def En_no(self):
        return (f"S12.{self.roll_no}.24")

a = student("XYZ",77)
print(f"Enrollment No. is {a.En_no()}")
a.info()

b = std12th("ABC",76)
print(f"Enrollment No. is {b.En_no()}")
b.info()

# output:
# Enrollment No. is S.77.24
# Student Name : XYZ
# Student Roll. No. : 77
# Enrollment No. is S12.76.24
# Student Name : ABC
# Student Roll. No. : 76