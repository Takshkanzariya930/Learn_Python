class student:

    school_name = "sch" # | School name and No_of_students
    No_of_students = 0  # | are class variables.

    def __init__(self,name,roll,marks):

        self.name = name    # | 
        self.roll_no = roll # |-> These are instant variables.
        self.marks = marks  # | 
        student.No_of_students += 1

    def info(self):
        print(f"\nStudent Name : {self.name}")
        print(f"Student Roll. No. : {self.roll_no}")
        print(f"Student Marks : {self.marks}")
        print(f"Student School : {self.school_name}")

a = student("xyz",33,35)
a.info()

b = student("abc",43,54)
b.school_name = "rch" # This change in school_name only affects b object.
b.info()

c = student("real",36,76)
c.info()

print(f"\nTotal No of student is :{student.No_of_students}") 

# output:
# Student Name : xyz
# Student Roll. No. : 33
# Student Marks : 35
# Student School : sch

# Student Name : abc
# Student Roll. No. : 43
# Student Marks : 54
# Student School : rch

# Student Name : real
# Student Roll. No. : 36
# Student Marks : 76
# Student School : sch

# Total No of student is :3