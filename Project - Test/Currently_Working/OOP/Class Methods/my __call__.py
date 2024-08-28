class student:

    def __init__(self,name,roll):
        self.name = name
        self.roll_no = roll

    def info(self):
        print(f"Student Name : {self.name}")
        print(f"Student Roll. No. : {self.roll_no}")

    def __call__(self,marks):
        print(f"Student with Roll No. {self.roll_no} got {marks} marks.")

a = student("XYZ",23)
a(100)  #using object as function

# output:
# Student with Roll No. 23 got 100 marks.