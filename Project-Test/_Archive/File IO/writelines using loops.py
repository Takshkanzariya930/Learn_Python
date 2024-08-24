f = open("myfile.txt","w")

lines = ["red","green","yellow"]

for line in lines:
    f.write(line+"\n")

f = open("myfile.txt","r")
print(f.read())
f.close()

# output:
'''
red
green
yellow

'''