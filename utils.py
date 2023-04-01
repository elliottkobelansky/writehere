import csv
from datetime import *
import pandas
import random


def msgappend (TS: int, msg: str, prompt: str):
    dt = datetime.utcfromtimestamp(TS)
    yr = dt.strftime("%Y")
    mt = dt.strftime("%m")
    dy = dt.strftime("%d")
    with open("msgs.csv","a") as i:
        writer = csv.writer(i)
        writer.writerow((yr,mt,dy,msg,prompt))
    return 

def msgread(y,m,d):
    """ Returns from a given a tuple where the first element is the text and the second is the prompt"""
    try:
        df = pandas.read_csv("msgs.csv", names=['y', 'm', 'd', 'msg', 'prompt'])
        mp = df.loc[((df["y"] == y) & (df["m"] == m) & (df["d"] == d))][['msg', 'prompt']]
        return tuple(mp.iloc[0])
    except:
        return None

def readlowest():
    with open("msgs.csv","r") as fp: 
        data = fp.readlines() 
    lastRow = data[-1]
    lsLR = lastRow.split(",")
    return tuple(lsLR[3:])

def choose_prompt():
    promptsset = set()

    with open("prompts.txt",'r') as f:
        prompts_list = f.readlines()

        for prompt in prompts_list:
            prompt = prompt.split("\n")[0]
            promptsset.add(prompt)   

        chosen_prompt = (random.choice(list(promptsset)))
        promptsset.remove(chosen_prompt)
        
    with open("prompts.txt", "w") as f:
        for prompt in promptsset:
            f.writelines(str(prompt)+"\n")
        f.close

def randomtime():
    """Generates a UNIX timestamp between 9AM and 9PM of the same day"""
    midnight = datetime.combine(datetime.today(), time.min).strftime('%s')
    randtime = random.randint(32400,75600)
    return int(midnight)+randtime
