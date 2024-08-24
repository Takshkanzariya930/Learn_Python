set1 = {1, 22, 43, 55, 818}
set2 = {1, 33, 54, 55, 565, 323}

print("This is new set",set1.symmetric_difference(set2))

print("set1 =",set1)
print("set2 =",set2)

# output:
# This is new set {33, 323, 43, 818, 565, 54, 22}
# set1 = {1, 818, 22, 55, 43}
# set2 = {1, 33, 323, 565, 54, 55}