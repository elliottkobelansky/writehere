def readlowest():
    with open("msgs.csv","r") as fp: 
        data = fp.readlines() 
    lastRow = data[-1]
    lsLR = lastRow.split(",")
    return tuple(lsLR[3:])
print(readlowest())