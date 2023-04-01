from random import randint
from datetime import *

def randomtime():
    """Generates a UNIX timestamp between 9AM and 9PM of the same day"""
    midnight = datetime.combine(datetime.today(), time.min).strftime('%s')
    randtime = randint(32400,75600)
    return int(midnight)+randtime
