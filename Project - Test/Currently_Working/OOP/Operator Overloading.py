class vector:

    def __init__(self,i,j,k):
        
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):

        return (f"{self.i}i + {self.j}j + {self.k}k")

    def __add__(self,v):

        return vector(self.i + v.i, self.j + v.j, self.k + v.k)
    
v1 = vector(2,3,4)
print(f"v1 = {v1}")

v2 = vector(4,7,2)
print(f"v2 = {v2}")

v3 = v1 + v2
print(f"v3 = {v3}")

v4 = v3 + v1
print(f"v4 = {v4}")

# output:
# v1 = 2i + 3j + 4k
# v2 = 4i + 7j + 2k
# v3 = 6i + 10j + 6k
# v4 = 8i + 13j + 10k