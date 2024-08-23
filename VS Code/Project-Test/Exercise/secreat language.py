def Encrypt():

    enstr = input("\n\nEnter string to encrypt it. \n-> ")
    enstr_list = []
    enstr.lower()
    enstr.strip()
    
    for i in enstr.split():

        if len(i) == 1:
            temp = i
            enstr_list.append(temp)
        elif len(i) == 2:
            temp = i[1]+i[0]
            enstr_list.append(temp)
        elif len(i) == 3:
            temp = i[1:3]+i[0]
            enstr_list.append(temp)
        else:
            temp = "sla"+i[1:len(i)]+i[0]+"uck"
            enstr_list.append(temp)

    print("\n\nHear is your Encrypted string \n")
    for e in enstr_list:
        print(e,end=' ')
    print('\n')

def Decrypt():
    destr = input("\n\nEnter string to decrypt it. \n-> ")   
    destr_list = []
    destr.lower()
    destr.strip()
    
    for i in destr.split():

        if len(i) == 1:
            temp = i
            destr_list.append(temp)
        elif len(i) == 2:
            temp = i[1]+i[0]
            destr_list.append(temp)
        elif len(i) == 3:
            temp = i[-1]+i[0:len(i)-1]
            destr_list.append(temp)
        else:
            temp = i[-4]+i[3:len(i)-4]
            destr_list.append(temp)

    print("\n\nHear is your Decrypted string \n")
    for e in destr_list:
        print(e,end=' ')
    print('\n')

def chose():
    select = int(input("if you want to Encrypt press 1, But if you want to Decrypt press 2. \n-> "))
    if select == 1:
        Encrypt()    
    else:
        Decrypt()

chose()