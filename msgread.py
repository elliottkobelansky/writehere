import pandas
def msgread(y,m,d):
    """ Returns from a given a tuple where the first element is the text and the second is the prompt"""
    df = pandas.read_csv("msgs.csv", names=['y', 'm', 'd', 'msg', 'prompt'])
    mp = df.loc[((df["y"] == y) & (df["m"] == m) & (df["d"] == d))][['msg', 'prompt']]
    return tuple(mp.iloc[0])
print(msgread(2021,12,24))