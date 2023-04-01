from random import randint
from datetime import *

def randomtime():
    midnight = datetime.combine(datetime.today(), time.min).strftime('%s')
    randtime = randint(32400,75600)
    return int(midnight)+randtime
