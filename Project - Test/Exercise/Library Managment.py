class Library:
    def __init__(self,no,*name):
        self.No_of_books = int(no)
        self.names_of_books = name
        print(self.names_of_books)
        print(self.No_of_books)

    def check(self):
        if len(self.names_of_books) == self.No_of_books :
            print("you are correct their is no error in your input.")
        else :
            print("There is an error in your input.")

L1 = Library(6,"abc","xyz","road","ddd","rjg","gggg")
L1.check()