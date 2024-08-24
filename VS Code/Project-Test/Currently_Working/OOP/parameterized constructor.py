class person:
    def __init__(self,n,a,o) :
        self.name = n
        self.age = a
        self.occupation = o
        print(f"Your name is {self.name}.")
        print(f"Your age is {self.age}.")
        print(f"Your occupation is {self.occupation}.")

a = person("xyz",27,"Teacher")

# output:
# Your name is xyz.
# Your age is 27.
# Your occupation is Teacher.