# Time Series Computations

In this section I will describe the functions I've implemented so far. I will give a brief description of what they are used for, and what is their interpretation. 

## ACF and PACF

If you have read anything about Time Series, you might have heard the terms ACF (Autocorrelation Function) and PACF (Partial Autocorrelation Function). With this functions we can identify linear relationships (correlations) between a tieme series and itself k periods before. 

### Autocovariance and Autocorrelation 
Suppose that you have a series ![equation](https://latex.codecogs.com/gif.latex?y_t&space;\sim&space;(0,&space;\sigma^2_y)). Its autocovariance  ![equation](https://latex.codecogs.com/gif.latex?k) periods before is 

![equation](https://latex.codecogs.com/gif.latex?\gamma_k&space;=&space;\operatorname{cov}(y_t,&space;y_{t-k})&space;=&space;\mathbb{E}&space;\big[y_t&space;y_{t-k}\big])

Since we are interested in the autocorrelation, we divide the covariance over the standard deviation of both ![equation](https://latex.codecogs.com/gif.latex?y_t) and ![equation](https://latex.codecogs.com/gif.latex?y_{t-k}). 

![equation](https://latex.codecogs.com/gif.latex?\rho_k&space;=&space;\frac{\operatorname{cov}(y_t,&space;y_{t-k})}{\sqrt{\mathbb{V}(y_t)}&space;\sqrt{\mathbb{V}(y_{t-k})}}&space;=&space;\frac{\gamma_k}{\gamma_0})

In order to approximate to the ACF, we use the sample ACF computing ![equation](https://latex.codecogs.com/gif.latex?\gamma_k) as follows, 

![equation](https://latex.codecogs.com/gif.latex?\gamma_k&space;=&space;\frac{1}{T}&space;\sum_{t=1}^{T-k}&space;(y_t&space;-&space;\bar{Y})(y_{t-k}&space;-&space;\bar{Y}))

Finally, to test whether or not ![equation](https://latex.codecogs.com/gif.latex?y_t) is a white noise process, we might use the following standard deviation (even thought we will later use some other tests), 

![equation](https://latex.codecogs.com/gif.latex?S_{\hat{\rho_k}}&space;=&space;\sqrt{\frac{1}{T}})

![ACF of White Noise Process](https://github.com/juancop/ts_models/blob/develop/tests/images/acf_wn.png)
