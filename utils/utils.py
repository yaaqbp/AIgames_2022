import random
import numpy as np
import os

def seed_everything(seed = 123):
	random.seed(seed)
	np.random.seed(seed)
	return seed

def set_dir():
    os.chdir('/Users/jakubpietraszek/python/AIgames')
    print('cwd:', os.getcwd())