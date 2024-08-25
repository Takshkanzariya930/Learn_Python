class Mo_NO:

    def __init__(self,na,no):
        self.name = na
        self.num = no
        self.occ = "EMPTY"
    
    def info(self):
        print(f"Person's name is {self.name} and His/Her mobile No. is {self.num}.")

    @property
    def occupation(self):
        return (self.occ)
    
    @occupation.setter
    def occupation(self,o):
        self.occ = o

a = Mo_NO("XYZ",99342)
a.info()
a.occupation = "TEACHER"
print(f"Person's occupation is {a.occupation}.")

# output:
# Person's name is XYZ and His/Her mobile No. is 99342.
# Person's occupation is TEACHER.