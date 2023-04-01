import os
import unicodedata
import random

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