class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def info(self):
        print(f"Employee ID is {self.id} and Name is {self.name}.")

class Programmer(Employee):
    def __init__(self,id,name,*lan):
        super().__init__(id,name) # Initialize id and name using the parent class
        self.lan = lan
    
    def Prog_info(self):
        print(f"language known by {self.id}({self.name}) is {self.lan}.")

a = Employee(444,"XYZ")
a.info()

b = Programmer(434,"ABC","python","C")
b.info()
b.Prog_info()

# output:
# Employee ID is 444 and Name is XYZ.
# Employee ID is 434 and Name is ABC.
# language known by 434(ABC) is ('python', 'C').