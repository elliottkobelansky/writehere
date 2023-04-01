import os

promptsset = {}

#write code to read txt fiile
rootdir = r'D:\osu! backup (1)\Songs backup'

with open("C:\Users\austi\Documents\GitHub\WriteThere\prompts.txt",'a+') as f:
    for it in os.scandir(rootdir):
        promptsset.append(it)