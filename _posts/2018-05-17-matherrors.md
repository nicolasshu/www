---
layout: article
title: "Measures of Fit"
tags:
  - Math
permalink: loss_functions.html
---

## Mean Squared Error
The **mean squared error** is a nice measure of fitness. Its formula is

$$ MSE = \frac{1}{n} \sum_{i=1}^{n} \left( y_{true,i} - y_{pred,i} \right)^2 $$

This is pretty good because it gets the error/residual of the prediction and squares it making sure that one is not accounting for negative errors, and the squareness makes the penalty much higher than it should be. Such penalty, depending on the system can be sometimes very high, leading to an unstable system, especially when taking them through perceptron algorithms for example. With that, it's important to make sure that the learning rate is low.

## Root Mean Squared Error

The **root mean squared error** is literally the square root of the *mean squared error*

$$RMSE = \sqrt{MSE} = \sqrt{ \frac{1}{n} \sum_{i=1}^{n} \left( y_{true,i} - y_{pred,i} \right)^2 } $$

It is pretty nice because it maintains positivity on the errors/residuals, making sure negative errors don't play against the error, but it doesn't have a squared penalty. In fact, its units are more **relatable**. As an example, if we get a model and we're trying to get the amount of error of, let's say *chickens* on our data:
- If we use MSE, our error will be (e.g.) "Given our model, we expect to have an average of error of 32 chickens$$^2$$"
- If we use RMSE, our error will be (e.g.) "Given our model, we expect to have a mean of error of 6 chickens"


## Median Absolute Deviation
The **median absolute deviation** has the formula of

$$ MAD = \text{median}( | x_i - \text{median}(\textbf{x})| )$$

and it behaves differently than the previous errors. Looking more closely in the equation:
1. $$x_i - \text{median}(\textbf{x})$$ centers the entire data around the **median**, making the median to be 0
1. $$\text{abs}(x_i - \text{median}(\textbf{x}))$$ gets the negative values of the centered data to be positive
1. $$MAD$$ in turn gets the median of all of those centered data that were made positive, and find the median of it!

As a result, the **median absolute deviation** provides an idea of how much does a data deviate. It is not necessarily a standard deviation, but a different type.


## Statistical Error vs. Residual
Given that $$\textbf{x} \sim  N(\mu,\sigma^2)$$

$$\mu = \frac{1}{N} \sum_k x_k $$

$$\bar{x} = \frac{1}{n} \sum_{k=1}^n x_k$$

The **statistical error** tells one how much an observation varies or deviates from its expected value, which is determined from the mean of the entire population $\mu$, which may be hard to find.

$$ e_k = x_k - \mu $$

The **residual** tells one the difference between the observation and the *observable sample mean* $$\bar{x}$$

$$ r_k = x_k - \bar{x} $$

With such, it can be proved that

$$\sum_k \text{Residual}_k = 0 $$  
$$\sum_k \text{Statistical Error}_k \neq 0$$

Eventually, "*one can standardize statistical erros in a z-score, and standardize residuals in a t-statistic or more generalized studentized residuals*"
