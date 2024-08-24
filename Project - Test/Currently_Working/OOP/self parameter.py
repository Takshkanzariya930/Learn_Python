class person:

    name = "EMPTY"
    age = "EMPTY"
    occupation = "EMPTY"

    def info(self): #To pass 'self' is compulsory.
        print(f"Your name is {self.name}.")
        print(f"Your age is {self.age}.")
        print(f"Your occupation is {self.occupation}.")

raj = person()

raj.name = "Raj"
raj.age = 23
raj.occupation = "Teacher"

raj.info()

# output:
# Your name is Raj.
# Your age is 23.
# Your occupation is Teacher.