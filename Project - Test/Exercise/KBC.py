que = ["what is capital of india?","what is indian currency called?","Which planet is known as the Red Planet?","What is the largest mammal in the world?"]
ans = ["delhi","rupee","marse","blue whale"]
reply = []
total = []
c = 0
ic = 0
i=0
sum=0

print("\n\n     ---------- WELCOME TO KBC ----------")

print("if you got one answer correct you get 1000 Rs. \nBut if you got one answer in correct then you loss 500 Rs.\n \n \n ")

while i < len(que):

    print(que[i])
    inp=input("Enter your answer: ")
    reply.append(inp.lower())
    
    if ans[i]==reply[i]:
        print("!!!!    your answer is correct    !!!!\n ")
        total.append(1000)
        c=c+1
    else:
        print("!!!!    your answer is incorrect    !!!!\n ")
        total.append(-500)
        ic=ic+1
    i=i+1

for a in total:
    sum = sum + a

print("you got",c,"answers correct and",ic,"answers incorrect.")

if sum<0:
    print(f"\n     You lost {sum} Rs.")
else:
    print(f"\n     You won {sum} Rs.")