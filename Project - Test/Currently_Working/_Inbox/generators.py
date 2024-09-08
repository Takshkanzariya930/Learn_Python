def my_generator():

    for i in range(10):
        yield(i)

gen = my_generator()

print(next(gen))
print(next(gen))

for j in range(7):
    print(next(gen))

# output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8