f = open("myfile.txt","r")

while True:
    line = f.readline() #Reads only one line of file
    if not line:
        break
    print(line)

f.close()

# output:
'''
This is first line

This is second line

This is third line
'''