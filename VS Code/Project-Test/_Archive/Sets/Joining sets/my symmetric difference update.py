set1 = {1, 22, 43, 55, 818}
set2 = {1, 33, 54, 55, 565, 323}
set1.symmetric_difference_update(set2)

print("set1 =",set1)
print("set2 =",set2)

# output:
# set1 = {33, 818, 323, 565, 22, 54, 43}
# set2 = {1, 33, 323, 565, 54, 55}