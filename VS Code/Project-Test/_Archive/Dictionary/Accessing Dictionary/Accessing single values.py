info = {23:"Ramesh",50:"Priya",66:"Rekha",44:"Kunj"}

print(info[66])     #Will raise ERROR if key not found
print(info.get(77)) #Will NOT raise ERROR if key not found

# output:
# Rekha
# None