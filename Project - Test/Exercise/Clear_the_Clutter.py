import os 
n = 0

os.chdir("snap")

for i in os.listdir():
    if i.endswith(".png"):
        n += 1
        os.replace(i,f"{n}.png")