# Time Series Computations

In this section I will describe the functions I've implemented so far. I will give a brief description of what they are used for, and what is their interpretation. 

## ACF and PACF

If you have read anything about Time Series, you might have heard the terms ACF (Autocorrelation Function) and PACF (Partial Autocorrelation Function). With this functions we can identify linear relationships (correlations) between a tieme series and itself k periods before. 

### Autocovariance and Autocorrelation 
Suppose that you have a series ![equation](https://latex.codecogs.com/gif.latex?y_t&space;\sim&space;(0,&space;\sigma^2_y)). Its autocovariance  ![equation](https://latex.codecogs.com/gif.latex?k) periods before is 

<center> ![equation](https://latex.codecogs.com/gif.latex?\gamma_k&space;=&space;\operatorname{cov}(y_t,&space;y_{t-1})&space;=&space;\mathbb{E}&space;\big[y_t&space;y_{t-1}\big]) <center/>