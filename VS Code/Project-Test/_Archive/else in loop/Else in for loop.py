for i in range(7):
    print(i)
    if i == 5:   # This statements ends loop hear, 
        break    # so else is not printed because else is part of loop.
else:
    print("Loop completed")

print("Out of the loop")

# output:
# 0
# 1
# 2
# 3
# 4
# 5
# Out of the loop