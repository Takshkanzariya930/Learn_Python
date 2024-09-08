class student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll_no = roll
        self.marks = marks
        print(f"Student Name : {self.name}")
        print(f"Student Roll. No. : {self.roll_no}")
        print(f"Student Marks : {self.marks}")

    @staticmethod
    def check_pass(marks):

        if marks >= 33:
            print("student has passed the test.")
        else :
            print("student has failed the test.")

a = student("xyz",33,66)
student.check_pass(55)

# output:
# Student Name : xyz
# Student Roll. No. : 33
# Student Marks : 66
# student has passed the test.