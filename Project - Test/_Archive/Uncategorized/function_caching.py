from functools import lru_cache
from time import sleep

@lru_cache(maxsize=None)
def fx(n):
    sleep(3)
    return(n**3)

print(fx(2))
print("done for 2")

print(fx(65))
print("done for 65")

print(fx(43))
print("done for 43")

print(fx(33))
print("done for 33")

print(fx(45))
print("done for 45")

print(fx(65))
print("done for 65")

# output:
# 8
# done for 2
# 274625
# done for 65
# 79507
# done for 43
# 35937
# done for 33
# 91125
# done for 45
# 274625
# done for 65