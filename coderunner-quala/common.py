import random
import time
W = ['A', 'B', 'C', 'D']

def create_rand_str(n=50):
    return ''.join([W[random.randrange(0, 4)] for i in range(n)])

def wait_for_sec(s=1):
    time.sleep(s)
