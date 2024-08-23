f = open('myfile.txt',"r") #This will throw an error if file does not exist
print(f)
f.close() #You must close opened file or it will throw an ERROR

# Output: