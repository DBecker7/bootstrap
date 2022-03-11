import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(2112) # reproducible
x = np.random.uniform(low = 0, high = 30, size = 40)
x.sort()

def logistic_growth(x, r, k):
    y = 1/(1 + np.exp((k - x) * r))
    return y

y = logistic_growth(x, 0.4, 15)
y = y + np.array([
     0.001,   0.003, -0.002, -0.004, 0.003, 
     0.006, -0.008, -0.004, 0.002, 0.004,
    -0.02,  0.07,    0.12, -0.08, -0.09,
     0.2,    0.12,  -0.12, -0.2, 0.15,
    -0.12,   0.11,  -0.14,  0.,  0.091,
    -0.085,  -0.06,   -0.042, -0.08, -0.006,
    0.02, -0.02, 0.01, -0.05, 0.004,
    -0.002,  0.006,  0.001, -0.002, 0.0001
    ])

x = np.round(x, 4)
y = np.round(y, 4)

popt, pcov = curve_fit(logistic_growth, x, y)

xseq = np.arange(1, 31, 0.1)
yhat = logistic_growth(xseq, popt[0], popt[1])

#plt.plot(x, y, "o", xseq, yhat, "-k")
#plt.show()

xy = pd.DataFrame({"x": x, "y": y})
xy.to_csv("samples.csv", index = False)

rands1 = np.random.randint(0, 40, 40)
print(xy.iloc[rands1])

for i in range(10):
    np.random.seed(i)
    indices = np.random.randint(0, 40, 40)
    xyi = xy.iloc[indices].sort_values("x")
    xyi.to_csv("samples/sample_" + str(i).zfill(4) + ".csv", index = False)

