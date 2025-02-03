A_B = [[1,2],[2,3],[3,4]]
X = ['x','y','z']
sol = []

for i in range(len(A_B)):
    sol.append(f"{X[i]} = {A_B[i][-1]}")
   

print(sol)