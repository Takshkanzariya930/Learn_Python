set1 = {1, 22, 43, 55, 818}
set2 = {"1", 33, 54, "55", 565, 323}

print(set1.isdisjoint(set2))
print(set2.isdisjoint(set2))

# output:
# True
# False