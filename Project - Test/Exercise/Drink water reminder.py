from plyer import notification
from time import sleep

while True:
    
    notification.notify( 
        title="REMINDER",
        message="DRINK A GLASS OF WATER",
        app_name="REMINDER",
        timeout=10)
    
    sleep(172800)