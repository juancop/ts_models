# Time Series Computations

In this section I will describe the functions I've implemented so far. I will give a brief description of what they are used for, and what is their interpretation. 

## ACF and PACF

If you have read anything about Time Series, you might have heard the terms ACF (Autocorrelation Function) and PACF (Partial Autocorrelation Function). With this functions we can identify linear relationships (correlations) between a tieme series and itself k periods before. 

Suppose that you have a series ![equation](https://latex.codecogs.com/gif.latex?y_t)