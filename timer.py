from datetime import datetime

import time
import random


our = datetime.today()
now = datetime.time(our)
print(now)

for i in range(5):
    minute = datetime.today().minute

    hour = datetime.today().hour

    
    if hour %2:
        print(hour,'нечетных часв',)
        
    else:
        print(hour, 'четных часов')

        
    if minute %2:
           print(minute,'нечетных минут')
    else:
            print(minute,'четных минут')
   
    wait_time = random.randint(1,60)
    time.sleep(wait_time)
our = datetime.today()
now = datetime.time(our)
print(now)

