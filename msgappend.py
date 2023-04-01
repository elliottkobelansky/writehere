import csv
from datetime import *

def msgappend (TS: int, msg: str):
    dt = datetime.utcfromtimestamp(TS)
    yr = dt.strftime("%Y")
    mt = dt.strftime("%m")
    dy = dt.strftime("%d")
    with open("msgs.csv","a") as i:
        writer = csv.writer(i)
        writer.writerow((yr,mt,dy,msg))