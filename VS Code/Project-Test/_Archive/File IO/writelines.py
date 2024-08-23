f = open("myfile.txt","w")

lines = ["red","\ngreen","\nyellow"]
f.writelines(lines)

f = open("myfile.txt","r")
print(f.read())
f.close()

# output:
'''
red
green
yellow
'''