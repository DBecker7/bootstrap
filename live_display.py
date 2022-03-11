import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")

# Easy to read
parm = np.array([[0.2, 15], 
    [0.233, 14.67],
    [0.32, 15.01],
    [0.28, 14.7],
    [0.33, 15.23],
    [0.3, 15]])

# Might be easier to type live
parm2 = np.array([0.2, 15, 0.233, 14.67, 0.32, 15.01]).reshape(-1, 2)
parm2

def logistic_growth(x, r, k):
    y = 1/(1 + np.exp((k - x) * r))
    return y

xseq = np.linspace(0, 30, 31)
yseq = logistic_growth(xseq, 0.3, 15)

data = pd.read_csv("data.csv")
data.plot("x", "y", kind = "scatter")

for i in range(parm.shape[0]):
    yi = logistic_growth(xseq, parm[i, 0], parm[i,1])
    plt.plot(xseq, yi, color = "lightgrey")

plt.plot(xseq, yseq, color = "black")

plt.show()
