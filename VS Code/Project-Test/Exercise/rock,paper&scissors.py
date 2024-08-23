from random import choice
define = {0:"ROCK", 1:"PAPER", 2:"SCISSORS"}
checker = [0,1,2]
ind = [0,1,2]
player_ch = 0
comp_ch = 0

print("LET'S PLAY".center(60,"-"))
print('''
    0 = "ROCK"
    1 = "PAPER"
    2 = "SCISSORS"
''')

player_ch = int(input("Enter your choice : "))

comp_ch = choice(ind)

if player_ch not in checker:
    raise ValueError("Your choice should be 0, 1 or 2".center(60,"-"))

print(f"\nYour choice is {define[player_ch]} and Computer's choice is {define[comp_ch]}")

if player_ch == comp_ch:
    print("\n--> It's a Draw.\n")

elif player_ch == 0 and comp_ch == 1:
    print("\n--> You lost.\n")

elif player_ch == 0 and comp_ch == 2:
    print("\n--> You won.\n")

elif player_ch == 1 and comp_ch == 0:
    print("\n--> You won.\n")

elif player_ch == 1 and comp_ch == 2:
    print("\n--> You lost.\n")

elif player_ch == 2 and comp_ch == 0:
    print("\n--> You lost.\n")

elif player_ch == 2 and comp_ch == 1:
    print("\n--> You won.\n")

print("Thank you for playing".center(60,"-"))