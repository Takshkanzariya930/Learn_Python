f = open("myfile.txt","a")
f.write("\n\nHi i am extra")
f.close()

f = open("myfile.txt","r")
print(f.read())
f.close()

f = open("myfile.txt","w")
f.write("\nHi i am extra")
f.close()

f = open("myfile.txt","r")
print(f.read())
f.close()

# output:
'''
This is first line      |
This is second line     | 
This is third line      | --> This output is due to opening file in append mode
                        |     where only line is added previous content is as it is
Hi i am extra           |
                        
Hi i am extra           | --> This output is due to opening file in write mode 
                              where everything has been over written
'''