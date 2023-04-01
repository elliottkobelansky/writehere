import time
from Randomtime import randomtime

randomtime = randomtime()
while True:
    if time.time() > randomtime:
        print("hi") #THIS IS WHERE YOU PUT THE CODEEE
        break
    else:
        time.sleep(60)

