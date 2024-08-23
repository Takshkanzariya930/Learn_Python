a = {23,"xyz",True,(32,6),23,True}
b = set()
print(a,"    ",type(a))
print(b,"                         ",type(b))

# output: (order of items in set might change every time)
# {True, 'xyz', (32, 6), 23}      <class 'set'>
# set()                           <class 'set'>