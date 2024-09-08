class student:

    def __init__(self,name,roll):
        self.name = name
        self.roll_no = roll
    
    def __len__(self):
        return len(self.name) #Here you can make any function

    def info(self):
        print(f"Student Name : {self.name}")
        print(f"Student Roll. No. : {self.roll_no}")

a = student("XYdsZ",65)
print(len(a))

# output:
# 5