import time
import utils

randt = utils.randomtime()

alreadyentry = True

while True:

    if time.time() > randt and not utils.msgread(y, m, d):
        alreadyentry = False

    if utils.msgread(y,m,d):
        alreadyentry = True

    if alreadyentry == True:
        #show confirmation screen
    if alreadyentry == False:
        #show text box screen
        while True:
            if utils.msgread(y,m,d):
                randt = utils.randomtime() + 86400
                new_prompt = utils.choose_prompt() #display new prompt
                alreadyentry == True
                break
            time.sleep(1)
    
    time.sleep(5)