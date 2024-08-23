set1 = {1, 22, 43, 55, 33, 54, 818}
set2 = {1, 33, 54, 55}

print(set1.issubset(set1))
print(set1.issubset(set2))
print(set2.issubset(set1))

# output:
# True
# False
# True