import numpy as np
import pandas as pd
from matplotlib import collections  as mc
import pylab as pl

def acf(y, max_lags):
    if type(y) == list:
        y = pd.DataFrame(y)
    elif y == pd.core.frame.DataFrame:
        pass
    else: 
        print("Type {} not supported.".format(type(y)))
    mean = y.mean()[0]
    var = y.var()[0]
    covariances = []
    T = len(y)
    for p in range(max_lags+1):
        tmp = pd.concat([y, y.shift(p)], axis = 1).dropna()
        tmp = tmp-mean
        mult = tmp.iloc[:, 0] * tmp.iloc[:, 1]
        mult = mult.sum()/(var * (T-1))
        covariances.append(mult)
        
    coords = []
    for x1, x2 in zip(range(max_lags+1), covariances):
        coords.append([(x1, 0), (x1, x2)])
    lc = mc.LineCollection(coords, linewidths=1, color = "black")
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    #ax.margins(0.1)
    ax.axhline(y=0, xmin=0.0, xmax=1, color = "black", linewidth = 1)
        
    return covariances