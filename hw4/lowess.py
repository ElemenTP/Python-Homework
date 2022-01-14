#!/usr/bin/python3 -O
import os
import statsmodels.api as sm
import numpy as np

lowess = sm.nonparametric.lowess

filePath = os.path.dirname(os.path.realpath(__file__))
xlist = list()
ylist = list()
yres = list()
datalen = 0
data_path = f"{filePath}/test.txt"
with open(data_path) as f:
    for line in f.readlines():
        words = line.split()
        if words[0].startswith("#"):
            continue
        xlist.append(int(words[0]))
        ylist.append(float(words[1]))
        yres.append(float(words[2]))
        datalen += 1

xarr = np.asarray(xlist, dtype=np.uint16)
yarr = np.asarray(ylist, dtype=np.float64)


yest = lowess(
    endog=yarr,
    exog=xarr,
    frac=float(10 / datalen),
    is_sorted=True,
    return_sorted=True,
)[:, 1]

print("Year\tNo_Smoothing\tLowess(5)(org)\tLowess(5)(calc)")
for i in range(datalen):
    print(xarr[i], "\t", yarr[i], "\t", yres[i], "\t", "{:.2f}".format(yest[i]))
