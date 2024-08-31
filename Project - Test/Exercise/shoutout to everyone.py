import win32com.client
names = []

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    name = input("Enter name to be added: ")
    names.append(name)
    
    ch = input("\nDo you want to add more(y/n): ")
    
    if ch == 'n' or ch == 'N':
        break

for i in names:

    speaker.speak(f"Shout out to {i}")