r1 = []
r2 = []
r3 = []

for i in range(3):
    num = int(input())
    r1.append(num)

for i in range(3):
    num = int(input())
    r2.append(num)

for i in range(3):
    num = int(input())
    r3.append(num)

a = r1[2] * r2[1] * r3[0]
b = r1[0] * r2[2] * r3[1]
c = r1[1] * r2[0] * r3[2]
d = r1[0] * r2[1] * r3[2]
e = r1[1] * r2[2] * r3[0]
f = r1[2] * r2[0] * r3[1]

det = -a-b-c+d+e+f

print(r1[0],r1[1],r1[2])
print(r2[0],r2[1],r2[2])
print(r3[0],r3[1],r3[2])

print(f"This is determinant of matrix : {det}")