import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd
import os

def logistic_growth(x, r, k):
    y = 1/(1 + np.exp((k - x) * r))
    return y

r_tracker = np.array([])
k_tracker = np.array([])

for i in range(1000):
    df_number = np.random.randint(0, 1000, 1)
    df_filename = "samples/sample_" + str(i).zfill(4) + ".csv"
    try:
        df = pd.read_csv(df_filename)
    except:
        print("df does not exist")
        next

    try:
        popt, pcov = curve_fit(logistic_growth, df.x.to_numpy(), df.y.to_numpy(), p0 = [0.3, 15])
    except:
        print("No minimum found")
        next

    if popt[1] < 0:
        print(i)
        #os.remove("samples/sample_" + str(i).zfill(4) + ".csv")

    r_tracker = np.append(r_tracker, popt[0])
    k_tracker = np.append(k_tracker, popt[1])

x_seq = np.linspace(0, 30, 31)
y_hat = logistic_growth(x_seq, popt[0], popt[1])

figure, axis = plt.subplots(2, 2)

axis[0, 0].plot(df.x, df.y, "o", x_seq, y_hat, "-k")
axis[0, 0].set_title("r = " + str(np.round(popt[0], 3)) + " and k = " + str(np.round(popt[1], 2)))

axis[0, 1].plot(r_tracker, k_tracker, "o")


axis[1, 0].hist(r_tracker)
axis[1, 1].hist(k_tracker)

plt.show()

plt.hexbin(r_tracker, k_tracker, gridsize = 25)
plt.show()

from scipy.stats import kde
k = kde.gaussian_kde(np.stack([r_tracker, k_tracker]))
xi, yi = np.mgrid[r_tracker.min():r_tracker.max():100*1j, k_tracker.min():k_tracker.max():100*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))

plt.pcolormesh(xi, yi, zi.reshape(xi.shape))
plt.show()
