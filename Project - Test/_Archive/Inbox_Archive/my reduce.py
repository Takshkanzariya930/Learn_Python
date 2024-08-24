from functools import reduce

l1 = [1,2,3,4,5,6]
l2 = reduce(lambda x,y : x+y,l1)
print(l2)

# output:
# 21