import win32api
import os
import shutil as sh
from time import sleep,strftime,localtime

check_P = win32api.GetLogicalDriveStrings().split('\000')[:-1]
print(check_P)

while True:

    check_C = win32api.GetLogicalDriveStrings().split('\000')[:-1]

    print(check_C)

    drive = [d for d in check_C if d not in check_P]
    
    if len(drive) >= 1:
        break

    sleep(30)

print(drive)

C_time = strftime("%d-%b-%Y_%H-%M-%S",localtime())

target_dir = f"{check_P[0]}New_Files\\File_{C_time}"

os.chdir(drive[0])

if os.path.exists(target_dir):
    sh.rmtree(target_dir)

print("COPYING....")
sh.copytree(drive[0],target_dir)
print("COMPLETED")