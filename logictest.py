import time
import utils

randt = utils.randomtime()
#show confirmation
while True:
    while True:
        if time.time() > randt:

            #open text page
            utils.choose_prompt()
            #display chosen_prompt

            randt = utils.randomtime() + 86400
            break
        else:
            time.sleep(5)

    #show confirmation 
    #text box light green
    lowest = utils.readlowest()
    txt = lowest[0] #display text as Read Only
    prp = lowest[1]
    
