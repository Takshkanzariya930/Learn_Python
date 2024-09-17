import win32api
import os
import shutil as sh
from time import sleep
from win10toast import ToastNotifier
toaster = ToastNotifier()

check_P = win32api.GetLogicalDriveStrings().split('\000')[:-1]
print(check_P)

while True:

    check_C = win32api.GetLogicalDriveStrings().split('\000')[:-1]

    print(check_C)

    drive = [d for d in check_C if d not in check_P]
    
    if len(drive) >= 1:
        break

    sleep(30)

toaster.show_toast("ALERT!!", "CODE RUNNING...", duration=20)

print(drive)

target_dir = f"{check_P[0]}New_Files\\File198"

os.chdir(drive[0])

if os.path.exists(target_dir):
    sh.rmtree(target_dir)

print("COPYING....")
sh.copytree(drive[0],target_dir)

toaster.show_toast("ALERT!!", "COMPLETED.", duration=20)