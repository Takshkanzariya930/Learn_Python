import os
n = 0

os.chdir("Snaps")

for i in os.listdir():
    if i.endswith(".png"):
        n = n + 1
        os.replace(i,f"{n}.png")