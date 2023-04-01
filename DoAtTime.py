import time
from Randomtime import randomtime

randt = randomtime()
#show confirmation
while True:
    while True:
        if time.time() > randt:
            #open text page
            #wait until submit button is pressed
            randt = randomtime() + 86400
            break
        else:
            time.sleep(5)

    #show confirmation
