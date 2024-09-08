class student:
    school_name = "xyz"

    def __init__(self,name,roll):
        self.name = name
        self.roll_no = roll

    def info(self):
        print(f"Student Name : {self.name}")
        print(f"Student Roll. No. : {self.roll_no}")
        print(f"Student's school : {self.school_name}")

    @classmethod
    def ch_school(cls,sch_name):
        cls.school_name = sch_name

a = student("ABC",56)
a.school_name = "DEF"
a.info()
print(student.school_name)

student.ch_school("WAS")
print(student.school_name)

# output:
# Student Name : ABC
# Student Roll. No. : 56
# Student's school : DEF
# xyz
# WAS