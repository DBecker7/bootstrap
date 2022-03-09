import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import genpareto

np.random.seed(2112)
sample = genpareto(c = 1.5, loc = 1.5, scale = 1.5)
sample.sort()

plt.hist(sample, bins = 40)
plt.show()

handle = open("testfile.txt", "w")
for item in sample:
    handle.write(str(item) + " ")

handle.close()


