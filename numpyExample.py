import numpy as np
from random import randrange

avg = np.zeros([2])

for i in range(20):
   avg = np.vstack((avg, np.array([randrange(100), randrange(5)])))

print(np.average(avg, axis=0))