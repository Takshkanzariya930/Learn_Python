i=0

while i<7:
    print(i)
    if i == 5:   # This statements ends loop hear, 
        break    # so else is not printed because else is part of loop.
    i = i + 1
else:
    print("Loop complete")

print("Out of the loop")

# output:
# 0
# 1
# 2
# 3
# 4
# 5
# Out of the loop