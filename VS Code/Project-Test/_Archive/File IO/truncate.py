with open("myfile.txt","w") as f:
    f.write("Hello world")
    f.truncate(7)  #Clears everything except first seven bytes of file

with open("myfile.txt","r") as f:
    print(f.read())

# output:
'''
Hello w
'''