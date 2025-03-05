import copy

A_B = []
X = []
sol = []

def accepting_equations():
    
    global equations
    equations = []
    
    print("\nEquation should be in this form only : ")
    print("0x+1y-3z=7")
    
    print("\nYou should not enter : ")
    print("x32 + y=z")
    
    No_of_equations = int(input("Enter No of equation you want to enter : "))
    
    for _ in range(1,No_of_equations+1):
        
        equations.append(input(f"Enter {_} Equation : "))

def creating_matrices():
    
    for i in range(len(equations)):
        A_B.append(equations[i].replace('+',' +').replace('-',' -').replace('=',' ').split())
    
    for i in range(len(A_B)):
        for j in range(len(A_B[i])-1) :
            X.append(A_B[i][j][-1])
            A_B[i][j] = A_B[i][j][:-1]
            
    for i in range(len(A_B)):
        A_B[i] = list(map(float,A_B[i]))

def converting_to_one(m,n):
    
    A_B[m] = list(map(lambda x : x*(1/A_B[m][n]),A_B[m]))
    
def converting_to_zero(r1,r2,n):
    f = A_B[r1][n]

    for i in range(len(A_B[r1])):
        A_B[r1][i] = A_B[r1][i] - (f*A_B[r2][i])

def converting_matrix_in_reduced_row_echelon_form():

    temp = 0
    i = 0

    for i in range(len(A_B)-1):
        if (all(x == 0 for x in A_B[i])):
            temp = A_B[len(A_B)-1]
            A_B[len(A_B)-1] = A_B[i]
            A_B[i] = temp

    while(A_B[0][0] == 0):
        
        i = i + 1
        temp = A_B[0]
        A_B[0] = A_B[i]
        A_B[i] = temp
        
        if (i == len(A_B)-1):
            break

    for i in range(len(A_B)):
        converting_to_one(i,i)
        for j in range(len(A_B)):
            if j != i : 
                converting_to_zero(j,i,i)
                
def determining_types_of_solution():
    A = copy.deepcopy(A_B)
    rank_of_A = len(A)
    rank_of_A_B = len(A_B)
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            if j == len(A[i])-1:
                A[i].pop()
                
    for i in range(len(A)):
        if all(x==0 for x in A[i]):
            rank_of_A = rank_of_A - 1
            
    for i in range(len(A_B)):
        if all(x==0 for x in A_B[i]):
            rank_of_A_B = rank_of_A_B - 1
            
    if rank_of_A == rank_of_A_B == len(equations):
        return 0
    elif rank_of_A == rank_of_A_B < len(equations):
        return 1
    else:
        return 2

def finding_solution():
    i = 0
    for i in range(len(A_B)):
        sol.append(f"{X[i]} = {A_B[i][-1]}")

accepting_equations()
creating_matrices()
converting_matrix_in_reduced_row_echelon_form()

if determining_types_of_solution() == 0:
    finding_solution()
    
    print("\n",sol)

elif determining_types_of_solution() == 1:
    
    for i in equations:
        print(i)
    
    print("Above system of linear equation has infinitely many solution")
        

elif determining_types_of_solution() == 2:

    for i in equations:
        print(i)
    
    print("Above system of linear equation has No Solution")