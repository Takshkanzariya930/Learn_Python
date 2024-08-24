set1 = {1, 22, 43, 55, 33, 54, 818}
set2 = {1, 33, 54, 55}

print(set1.issuperset(set1))
print(set1.issuperset(set2))
print(set2.issuperset(set1))

# output:
# True
# True
# False