l1 = [1,2,3,4,5,6,7,8]
l2 = filter(lambda x : x%2 == 0,l1)
print(l2)
print(list(l2))

# output:
# <filter object at 0x00000204E0E59BA0>
# [2, 4, 6, 8]