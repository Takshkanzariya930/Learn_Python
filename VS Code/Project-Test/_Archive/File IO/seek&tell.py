with open("myfile.txt","r") as f:
    f.seek(7) #Move starting point of the file where program will start reading or writing
    print(f.tell()) #Tells the position in file from where program will start reading or writing
    print(f.read(3))
    print(f.tell())

# output:
'''
7
een
10
'''