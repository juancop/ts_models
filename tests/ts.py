import numpy as np
import pandas as pd
from matplotlib import collections  as mc
import pylab as pl
import matplotlib.pyplot as plt

def barlett(n, p):
    """
    Computes Barlett's variance for the ACF. 
    
    Params
    -------
        n (int): The lenght of the time series. 
        p (int): The number of lags.
        
    Returns
    -------
        sd (list): Barlett's standard deviation for the ACF.
    
    """
    sd = []
    for k in range(len(p)):
        sd.extend([np.sqrt((1 + sum([2*p_k**2 for p_k in p[:k+1]]))/n)])
    return sd

def plot_coord(coords, up_ci, lw_ci, title, max_lags, points):
    """
    Auxiliar function for plotting the ACF and its Confidence intervals. 
    Will be used for the ACF and PACF. 
    
    
    Params
    -------
        coords: The coordinates for each bar. 
        up_ci (list): Series for the upper limit of the confidence interval
        lw_ci (list): Series for the lower limit of the confidence interval
        title (str): Title for the plot
        max_lags (int): Max number of lags to plot. 
        points (list): ACF or PACF values.
        
    Returns
    --------
        Does not return anything. Instead, it plots the ACF or PACF.
    """
    lc = mc.LineCollection(coords, linewidths=1, color = "black")
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.axhline(y=0, xmin=0.0, xmax=1, color = "black", linewidth = 1)
    ax.plot(lw_ci, linestyle = "--", color = "blue", linewidth = 1)
    ax.plot(up_ci, linestyle = "--", color = "blue", linewidth = 1)
    ax.scatter(range(max_lags+1), points)
    ax.set_title(title)

def acf(y, max_lags, barlett_ci = False, display = True):
    """ 
    Computes and plots the ACF for a given series. It allows the use of Barlett's 
    equation for the variance of the ACF.
    
    Params
    -------
        y (list, df or series): The series to which the ACF is going to be computed. 
        max_lags (int): Maximum number of lags to compute and plot. 
        barlett_ci (bool): [False] Use Barlett's equation to compute the standard deviation
                           for the autocorrelations. 
        display (bool): [True] Displays the plot of the ACF. 
        
    Returns
    --------
        if display = True: 
            acf (list): ACF values. Displays the ACF plot.
            
        if display = False:
            acf (list): ACF values. 
            sd (list): Standard Deviation of the ACF.
    
    """
    if type(y) == list:
        y = pd.DataFrame(y)
    elif y == pd.core.frame.DataFrame:
        pass
    else: 
        print("Type {} not supported.".format(type(y)))
    mean = y.mean()[0]
    var = y.var()[0]
    _acf = []
    T = len(y)
    for p in range(max_lags+1):
        tmp = pd.concat([y, y.shift(p)], axis = 1).dropna()
        tmp = tmp-mean
        mult = tmp.iloc[:, 0] * tmp.iloc[:, 1]
        mult = mult.sum()/(var * (T-1))
        _acf.append(mult)
    if barlett_ci:
        sd = barlett(T, _acf)
    else:
        sd = [np.sqrt(1/T)]*(max_lags+1)
    
    up_ci, lw_ci = [1.96*x for x in sd], [-1.96*x for x in sd]
    coords = []
    for x1, x2 in zip(range(max_lags+1), _acf):
        coords.append([(x1, 0), (x1, x2)])
    if display:
        lc = mc.LineCollection(coords, linewidths=1, color = "black")
        fig, ax = pl.subplots()
        ax.add_collection(lc)
        ax.autoscale()
        ax.axhline(y=0, xmin=0.0, xmax=1, color = "black", linewidth = 1)
        ax.plot(lw_ci, linestyle = "--", color = "blue", linewidth = 1)
        ax.plot(up_ci, linestyle = "--", color = "blue", linewidth = 1)
        ax.scatter(range(max_lags+1), _acf)
        
        return _acf
    else:
        return _acf, sd