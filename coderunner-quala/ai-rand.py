import game
import time
import random
from common import *

while True:
    res = game.submit(create_rand_str())
    print(res)
    wait_for_sec()
