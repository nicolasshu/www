---
layout: article
title: "Bayesian Inference on Gaussian Distributions"
tags:
  - Machine Learning
  - Math
permalink: /bayesian_inference_for_gaussian.html
mathjax: true
---



## Introduction



Here we will try to better understand how Bayesian inference works for Gaussian distributions. 

## Likelihood

Let's say that we have a dataset $\boldsymbol{X} = \{ x_1, \cdots, x_N \}$, where $x_i \in \mathbb{R}$ and $x_i \sim \mathcal{N(\mu,\sigma)}$. In other words, we have $N$ examples from an univariate Gaussian distribution which has the mean $\mu$ and the variance $\sigma$ for the distribution. Let us also assume that all of the $N$ examples are sampled independently from each other. Therefore, the likelihood of the dataset is defined as the probability of obtaining the data given $\mu$, as a function of $\mu$. Note that this all makes sense in a diverging connection in a Bayesian network, where the mean node diverges to $N$ nodes, and if $\mu$ is known, then all of the samples are independent. 

$$\bbox[teal,4pt]{p(\boldsymbol{X}|\mu) = \prod_{i=1}^N p(x_i|\mu) = \frac{1}{(2\pi \sigma^2)^{N/2}} \exp \left[ -\frac{1}{2\sigma^2} \sum_{i=1}^N (x_i - \mu)^2 \right]}$$

Although this is defined as the likelihood, it would be best to determine a single equation that does not have a factorized notation (i.e. $\prod$). Now, let us define the empirical mean $\bar{x}$ and empirical variance $s^2$. 

$$\begin{align}
\bar{x} &= \frac{1}{N}\sum_{i=1}^N x_i \\ 
s^2 &= \frac{1}{N}\sum_{i=1}^N (x_i - \bar{x})^2
\end{align}$$

Therefore, we can rewrite 

$$\begin{align}
\sum_{i=1}^N (x_i - \mu)^2 &= \sum_{i=1}^N (x_i - \bar{x} - \mu + \bar{x})^2 \\ 
&= \sum_{i=1}^N [(x_i - \bar{x}) - (\mu - \bar{x})]^2 \\ 
&= \underbrace{\sum_{i=1}^N (x_i - \bar{x})^2}_{Ns^2} + \sum_{i=1}^N (\bar{x} - \mu)^2 - 2 \sum_{i=1}^N (x_i - \bar{x})(\mu - \bar{x}) \\ 
&= Ns^2 + \sum_{i=1}^N (\bar{x} - \mu)^2 -2 \left[ \left( \left(\sum_{i=1}^N x_i \right)-N\bar{x} \right) (\mu - \bar{x})\right] \\ 
&= Ns^2 + \sum_{i=1}^N (\bar{x} - \mu)^2 -2 \left[ \left( N\bar{x}-N\bar{x} \right) (\mu - \bar{x})\right] \\ 
&= Ns^2 + \sum_{i=1}^N (\bar{x} - \mu)^2 - 0 \\ 
&= Ns^2 + \sum_{i=1}^N \underbrace{(\bar{x} - \mu)^2}_{\text{indep of $i$}} \\
&= Ns^2 + N (\bar{x} - \mu)^2
\end{align}$$

Therefore, by putting this into the likelihood

$$\begin{align}
p(\boldsymbol{X}|\mu) &= \frac{1}{(2\pi \sigma^2)^{N/2}} \exp \left[ -\frac{1}{2\sigma^2} \sum_{i=1}^N (x_i - \mu)^2 \right] \\ 
&= \frac{1}{(2\pi \sigma^2)^{N/2}} \exp \left[ -\frac{1}{2\sigma^2} [Ns^2 + N (\bar{x} - \mu)^2]\right] \\ 
&\propto \exp\left( -\frac{Ns^2}{2\sigma^2} \right) \exp \left( -\frac{N}{2\sigma^2} (\bar{x}-\mu)^2\right)
\end{align}$$

Now, if $\sigma^2$ is constant (meaning that all of the data examples have the same variance), then we can drop the constant factors from the likelihood, thus obtaining that the likelihood of the dataset is  

$$\bbox[teal,4pt]{p(\boldsymbol{X} | \mu) \propto \exp \left( -\frac{N}{2\sigma^2} (\bar{x} - \mu)^2 \right) \propto \mathcal{N} \left(\bar{x} \bigg| \mu , \frac{\sigma^2}{N} \right) }$$

## Prior

Now let's compute the prior. Often, for different distributions, a natural conjugate prior is a prior which leads to the posterior being in the same distribution as the prior.  On the dataset, $\sigma^2$ is the variance of the observation noise, and $\mu$ is the mean of the observations. So, since the likelihood has the form 

$$p(\boldsymbol{X} | \mu) \propto \exp \left( -\frac{n}{2\sigma^2} (\bar{x} - \mu)^2 \right) \propto \mathcal{N} \left(\bar{x} \bigg| \mu , \frac{\sigma^2}{n} \right) $$

Then the natural conjugate prior $p(\mu)$ has the form

$$ \bbox[teal,4pt]{p(\mu) \propto \exp\left[ - \frac{(\mu - \mu_0)^2}{2 \sigma_0^2}  \right] \propto \mathcal{N}(\mu | \mu_0, \sigma_0^2) }$$

where the mean of the prior is $\mu_0$, and the variance of the prior is $\sigma_0^2$. 



## Posterior

Now, we need to compute the posterior $p(\mu \vert \boldsymbol{X})$. The posterior distribution is given by 

$$p(\mu \vert \boldsymbol{X}) \propto p(\boldsymbol{X} \vert \mu) p (\mu)$$

By expanding it, we will have 

$$\begin{align}
p(\mu | \boldsymbol{X}) &\propto p(\boldsymbol{X} | \mu) p (\mu) \\ 
&\propto \exp\left(-\frac{1}{2\sigma^2} \sum_{i=1}^N (x_i - \mu)^2 \right) \cdot \exp \left( -\frac{1}{2\sigma_0^2} (\mu - \mu_0)^2 \right) \\ 
&= \exp \left[ -\frac{1}{2\sigma^2} \sum_{i=1}^N (x_i^2 + \mu^2 - 2x_i \mu) + \frac{-1}{2\sigma_0^2} (\mu^2 + \mu_0 - 2 \mu_0 \mu)\right] 
\end{align}$$

We know that the product of two Gaussians yield another Gaussian. So we can write

$$ \begin{align} p(\mu | \boldsymbol{X}) &\propto \exp \left[  \color{cyan}{-\frac{\sum_i x_i^2}{2\sigma^2}}  \color{green}{- \frac{N \mu^2}{2\sigma^2}} \color{magenta}{+\frac{\sum_i x_i \mu}{\sigma^2}} \color{green}{- \frac{\mu^2}{2\sigma_0^2}} \color{cyan}{- \frac{\mu_0}{2\sigma_0^2}} \color{magenta}{+ \frac{\mu_0\mu}{\sigma_0^2}} \right] \\ 
&= \exp \left[ \color{green}{- \frac{\mu^2}{2} \left( \frac{N}{\sigma^2} + \frac{1}{\sigma_0^2} \right)} \color{magenta}{+\mu \left( \frac{\sum_i x_i}{\sigma^2} + \frac{\mu_0}{\sigma_0^2} \right)} \color{cyan}{- \left( \frac{\sum_i x^2_i}{2 \sigma^2} + \frac{\mu_0}{2\sigma_0} \right)} \right] \\ 
&\triangleq \exp \left[ -\frac{1}{2\sigma_N^2} \left( \color{green}{\mu^2} \color{magenta}{-2\mu_N \mu} \color{cyan}{+\mu_N^2} \right)\right]
&= \exp \left[ -\frac{1}{2\sigma_N^2} (\mu - \mu_N)^2 \right] \\ 
\end{align}$$

By matching the different coefficients, we can determine the posterior variance $\sigma_N^2$ and the posterior mean $\mu_N$. By matching the $\mu^2$ first, we can determine the $\sigma_N^2$:

$$\begin{align} 
-\frac{\mu^2}{2\sigma_N^2} &= -\frac{\mu^2}{2} \left( \frac{N}{\sigma^2} + \frac{1}{\sigma_0^2}\right) \\ 
\frac{1}{\sigma_N^2} &= \frac{N}{\sigma^2} + \frac{1}{\sigma_0^2} = \frac{N\sigma_0^2 + \sigma^2}{\sigma^2\sigma_0^2}\\
\sigma_N^2 &= \left( \frac{N}{\sigma^2} + \frac{1}{\sigma_0^2} \right)^{-1} = \frac{\sigma^2\sigma_0^2}{N\sigma_0^2 + \sigma^2}
\end{align}$$

By matching the $\mu$ coefficients, we can determine the posterior mean $\mu_N$ 

$$\begin{align} 
\frac{-2\mu \mu_N}{-2\sigma_N^2} &= \mu \left( \frac{\sum_{i=1}^N x_i }{\sigma^2} + \frac{\mu_0}{\sigma_0^2} \right) \\ 
\frac{\mu_N}{\sigma_N^2} &= \frac{\sum_{i=1}^N x_i }{\sigma^2} + \frac{\mu_0}{\sigma_0^2} \\ 
&= \frac{N \bar{x}}{\sigma^2} + \frac{\mu_0}{\sigma_0^2} \\ 
&= \frac{\sigma_0^2 N\bar{x} + \sigma^2 \mu_0 }{\sigma^2 \sigma_0^2} \\ 
\mu_N &= \sigma_N^2 \frac{\sigma_0^2 N\bar{x} + \sigma^2 \mu_0 }{\sigma^2 \sigma_0^2} \\ 
&= \frac{\sigma^2\sigma_0^2}{N\sigma_0^2 + \sigma^2} \cdot \frac{\sigma_0^2 N\bar{x} + \sigma^2 \mu_0 }{\sigma^2 \sigma_0^2} \\ 
&= \frac{\sigma_0^2 N\bar{x} + \sigma^2 \mu_0}{N\sigma_0^2 + \sigma^2} \\ 
&= \frac{\sigma^2}{N\sigma_0^2 + \sigma^2}\mu_0 + \frac{N\sigma_0^2}{N\sigma_0^2 + \sigma^2}\bar{x} \\ 
&= \sigma_N^2 \left( \frac{\mu_0}{\sigma_0^2} + \frac{N\bar{x}}{\sigma^2} \right)
\end{align}$$



So, the two parameters for the posterior Gaussian are:

$$\bbox[teal,4pt]{\begin{align}
\mu_N &= \frac{\sigma^2}{N\sigma_0^2 + \sigma^2}\mu_0 + \frac{N\sigma_0^2}{N\sigma_0^2 + \sigma^2} \underbrace{\bar{x}}_{\mu_{ML}} = \sigma_N^2 \left( \frac{\mu_0}{\sigma_0^2} + \frac{N\bar{x}}{\sigma^2} \right) \\
\sigma_N^2 &= \frac{\sigma^2\sigma_0^2}{N\sigma_0^2 + \sigma^2}
\end{align}}$$

Note that $\bar{x} = \mu_{ML} = N^{-1} \sum_{i=1}^N x_i$ as the maximum likelihood solution for $\mu$. Note that you can represent the variance as the **precision** of a Gaussian, which should be the inverse of the variance. 

$$\lambda = \frac{1}{\sigma^2} \quad \quad \lambda_0 = \frac{1}{\sigma_0^2} \quad \quad \lambda_N = \frac{1}{\sigma_N^2}$$

We can write the precision of the posterior Gaussian as 

$$\lambda_N = \frac{1}{\sigma_N^2} = \frac{N}{\sigma^2} + \frac{1}{\sigma_0^2} = N\lambda + \lambda_0$$

And for the mean of the posterior using the precision, 

$$\mu_N = \sigma_N^2 \left( \frac{\mu_0}{\sigma_0^2} + \frac{N \bar{x}}{\sigma^2} \right) = \frac{\mu_0 \lambda_0 + N\bar{x} \lambda}{\lambda_N}$$



Let us look at how all of these equations behave when you add more data.

> For each of the following, when you have $N\rightarrow \infty$, then:
>
> - Mean: $\displaystyle \lim_{\color{green}{N}\rightarrow \infty} \mu_N = \lim_{\color{green}{N}\rightarrow \infty} \frac{\sigma^2}{\color{green}{N}\sigma_0^2 + \sigma^2}\mu_0 + \frac{\color{green}{N}\sigma_0^2}{\color{green}{N}\sigma_0^2 + \sigma^2} \mu_{ML} = \mu_{ML}$
> - Variance: $\displaystyle \lim_{\color{green}{N\rightarrow \infty}} \sigma_{\color{green}{N}}^2 = \lim_{\color{green}{N\rightarrow \infty}} \frac{\sigma^2\sigma_0^2}{\color{green}{N}\sigma_0^2 + \sigma^2} = 0$ 
> - Precision: $\displaystyle \lim_{\color{green}{N\rightarrow \infty}} \lambda_{\color{green}{N}} = \lim_{\color{green}{N\rightarrow \infty}} = \color{green}{N}\lambda + \lambda_0 = \infty$
>
> This all starts to make sense intuitively. As we increase the number of examples, the mean progressively starts to get closer to the mean of the maximum likelihood of the Gaussian data. Meanwhile, the variance steadily starts to shrink to infinitesimally small values, whereas the precision starts to become infinitely high. 



## Posterior Predictive

Now, we come to compute the posterior predictive. As a recap (Bishop Eq. 2.113), if we have a marginal Gaussian distribution $p(x)$ and a conditional Gaussian distribution $p(y \vert x)$

$$\begin{align} p(x) &= \texttip{\mathcal{N} (x | \mu, \color{magenta}{\Lambda^{-1}})}{Marginal} \\ p(y|x) &= \mathcal{N} (y | \color{purple}{Ax + b}, \color{yellow}{L^{-1}})\end{align}$$

Then to compute the marginal distribution $p(y)$ is 

$$p(y) = \mathcal{N} (y|\color{purple}{A\mu+b}, \color{yellow}{L^{-1}} + A\color{magenta}{\Lambda^{-1}} A^T)$$

So, the posterior predictive is given by 

$$\begin{align} 
p(x|\boldsymbol{X}) &= \int p(x|\mu) \cdot p(\mu|\boldsymbol{X}) d\mu \\ 
&= \int \mathcal{N}(x|\mu, \sigma^2) \cdot \mathcal{N}(\mu | \color{purple}{\mu_N}, \color{yellow}{\sigma_N^2}) d\mu
\end{align}$$

$$\bbox[teal,4pt]{p(x|\boldsymbol{X}) = \mathcal{N} (x|\color{purple}{\mu_N}, \color{yellow}{\sigma_N^2} + \color{magenta}{\sigma^2})}$$

[Alternate Proof here]

## Marginal Likelihood

The marginal likelihood $l$ can be defined as 

$$\bbox[4pt,teal]{\begin{align}
l &= p(\boldsymbol{X}) = \int \left[ \prod_{i=1}^N \mathcal{N} (x_i | \mu, \sigma^2) \right] \mathcal{N} (\mu | \mu_0, \sigma_0^2) d\mu \\
&=\frac{\sigma}{(\sqrt{2\pi}\sigma)^n \sqrt{N\sigma_0^2 + \sigma^2}} \exp \left( -\frac{\sum_i x_i}{2\sigma^2} - \frac{\mu_0^2}{2\sigma_0^2} \right) \exp \left[\frac{1}{2(N\sigma_0^2 + \sigma^2)} \cdot \left( \frac{\sigma_0^2 N^2 \bar{x}^2 }{\sigma^2} + \frac{\sigma^2\mu_0^2}{\sigma_0^2} + 2N\bar{x} \mu_0 \right) \right]
\end{align}}$$

### Proof

> In order to compute the marginal likelihood, let us call $m=\mu_0$ and $\tau^2 = \sigma_0^2$ as our hyperparameters for simplicity
>
> $$
\begin{align}
l &= p(\boldsymbol{X}) \\
&= \int \left[ \prod_{i=1}^N \mathcal{N} (x_i | \mu, \sigma^2) \right] \mathcal{N} (\mu | \mu_0, \sigma_0^2) d\mu \\
&= \int \left[ \prod_{i=1}^N \mathcal{N} (x_i | \mu, \sigma^2) \right] \mathcal{N} (\mu | m, \tau^2) d\mu \\
&= \frac{1}{(\sigma \sqrt{2\pi})^n (\tau \sqrt{2\pi})} \int \exp \left( - \frac{1}{2\sigma^2 \sum_i (x_i - \mu)^2 - \frac{1}{2\tau^2} (\mu-m)^2 }\right) d\mu
\end{align}
$$
>  
> Let us now define $S^2 = \frac{1}{\sigma^2}$ and $T^2 = \frac{1}{\tau^2}$
>  $$
> \begin{align}
p(\boldsymbol{X}) &= \frac{1}{(S^{-1}\sqrt{2\pi})^n (T^{-1} \sqrt{2\pi})} \int \exp \left[ -\frac{S^2}{2} \left( \sum_i x_i^2 + n \mu^2 - 2\mu \sum_i x_i\right) - \frac{T^2}{2} \left(\mu^2 +m^2-2m\mu\right)\right] \\
&= \color{purple}{\frac{1}{(S^{-1}\sqrt{2\pi})^n(T^{-1}\sqrt{2\pi})}} \int \color{purple}{e^{-\frac{S^2 \sum_i x_i^2}{2}}} e^{-\frac{S^2N\mu^2}{2}} e^{S^2\mu \sum_i x_i} e^{-\frac{T^2}{2}\mu^2} \color{purple}{e^{-\frac{T^2}{2}m^2}} e^{T^2m\mu} d\mu \\
&= \underbrace{\color{purple}{\frac{e^{-\frac{S^2 \sum_i x_i^2}{2}-\frac{T^2}{2}m^2} }{(S^{-1}\sqrt{2\pi})^n(T^{-1}\sqrt{2\pi})}}}_{c} \int e^{-\frac{S^2N\mu^2}{2}} e^{S^2\mu \sum_i x_i} e^{-\frac{T^2}{2}\mu^2} e^{T^2m\mu} d\mu \\
&= c \int \color{violet}{e^{-\frac{S^2N\mu^2}{2}} e^{S^2\mu \sum_i x_i} e^{-\frac{T^2}{2}\mu^2} e^{T^2m\mu}} d\mu \\
&= c \int \color{violet}{\exp \left[ -\frac{1}{2} \left( S^2N\mu^2 - 2S^2\mu \sum_i x_i +T^2 \mu^2 -2T^2 m \mu\right) \right]}  d\mu \\
&= c \int \exp \left[ -\frac{1}{2} \left( S^2N + T^2 \right) \left( \mu^2 - 2\mu \underbrace{\frac{S^2\sum_i x_i +T^2 m}{S^2 N + T^2} }_{\alpha}\right)\right] d\mu \\
&= c \int \exp \left[ -\frac{1}{2} \left( S^2N + T^2 \right) \left( \mu^2 - 2\mu \alpha\right)\right] d\mu \\
&= c \int \exp \left[ -\frac{1}{2} \left( S^2N + T^2 \right) \left( \mu^2 - 2\mu \alpha \color{violet}{+ \alpha^2 - \alpha^2} \right) \right] d\mu \\
&= c \int \exp \left[ -\frac{1}{2} \left( S^2N + T^2 \right)(\mu-\alpha)^2 \color{purple}{+ \frac{1}{2} \left( S^2N + T^2 \right)\alpha^2 }\right] d\mu \\
&= c \int \exp \left[ -\frac{1}{2} \left( S^2N + T^2 \right)(\mu-\alpha)^2 \right] \color{purple}{\exp \left[ \frac{1}{2} \left( S^2N + T^2 \right)\alpha^2 \right]} d\mu \\
&= c  \color{purple}{\exp \left[ \frac{1}{2} \left( S^2N + T^2 \right)\alpha^2 \right]} \int \exp \left[ -\frac{1}{2} \left( S^2N + T^2 \right)(\mu-\alpha)^2 \right] d\mu \\
&= c  \exp \left[ \frac{1}{2} \color{red}{\left( S^2N + T^2 \right) \left( \frac{S^2\sum_i x_i +T^2 m}{S^2 N + T^2} \right)^2} \right] \int \exp \left[ -\frac{1}{2} \left( S^2N + T^2 \right)\left(\mu-\frac{S^2\sum_i x_i +T^2 m}{S^2 N + T^2}\right)^2 \right] d\mu \\ 
&= c  \exp \left[ \frac{1}{2}  \color{red}{\frac{(S^2\sum_i x_i +T^2 m)^2}{S^2 N + T^2}} \right] \underbrace{\color{yellow}{\int \exp \left[ -\frac{1}{2} \left( S^2N + T^2 \right)\left(\mu-\frac{S^2\sum_i x_i +T^2 m}{S^2 N + T^2}\right)^2 \right] d\mu}}_{\cdots = \frac{1.25331 erf(\frac{0.7071 -T^2m + s^2 N(\mu-\bar{x})+T^2\mu }{\sqrt{NS^2 + T^2}})}{\sqrt{NS^2 + T^2}} = \frac{\sqrt{2\pi}}{\sqrt{S^2N + T^2}} }  \\
&= c  \exp \left[ \frac{1}{2}  \frac{(S^2 \color{brown}{\sum_i x_i} +T^2 m)^2}{S^2 N + T^2} \right] \color{yellow}{\frac{\sqrt{2\pi}}{\sqrt{S^2N + T^2}}} \\ 
&= c  \exp \left[ \frac{1}{2}  \frac{(S^2 \color{brown}{N \bar{x}}+T^2 m)^2}{S^2 N + T^2} \right] \frac{\sqrt{2\pi}}{\sqrt{S^2N + T^2}} \\ 
&= \frac{e^{-\frac{S^2 \sum_i x_i^2}{2}-\frac{T^2}{2}m^2} }{(S^{-1}\sqrt{2\pi})^n \color{lime}{(T^{-1}\sqrt{2\pi})}}  \exp \left[ \color{violet}{ \frac{1}{2} \frac{(S^2 N\bar{x} +T^2 m)^2}{S^2 N + T^2} }\right] \color{lime}{\frac{\sqrt{2\pi}}{\sqrt{S^2N + T^2}}} \\
&= \frac{1 }{(S^{-1}\sqrt{2\pi})^n \color{lime}{(T^{-1}\sqrt{2\pi})}} \exp \left[-\frac{S^2 \sum_i x_i^2}{2}-\frac{T^2}{2}m^2 \right] \exp \left[ \color{violet}{\frac{1}{2} \frac{(S^2 N\bar{x} +T^2 m)^2}{S^2 N + T^2} }\right] \color{lime}{\frac{\sqrt{2\pi}}{\sqrt{S^2N + T^2}}}
\end{align}
$$
>
>Now, let us work on the constant and the exponent portion:
>
> $$\color{lime}{\frac{\sqrt{2\pi}}{T^{-1}\sqrt{2\pi}\sqrt{S^2N + T^2}} = \frac{1}{\tau\sqrt{\frac{N}{\sigma^2} + \frac{1}{\tau^2}}}\frac{\sigma}{\sigma} = \frac{\sigma}{\sqrt{\sigma^2\tau^2 \left( \frac{n}{\sigma^2}+ \frac{1}{\tau^2} \right)}} = \frac{\sigma}{\sqrt{\tau^2N + \sigma^2}} }$$
> 
> $$\color{violet}{\frac{1}{2} \frac{(S^2 N\bar{x} +T^2 m)^2}{S^2 N + T^2} = \frac{\left( \frac{1}{\sigma^2} n\bar{x} + \frac{1}{\tau^2} m \right)^2}{2 \left( \frac{n}{\sigma^2} + \frac{1}{\tau^2}\right)} = \frac{\left(\frac{N \bar{x} \tau^2+ \sigma^2 m}{\tau^2 \sigma^2} \right)^2}{2 \left( \frac{\tau^2 N +\sigma^2}{\tau^2 \sigma^2} \right)} = \frac{(N\bar{x}\tau^2 + \sigma^2 m)^2}{2\tau^2 \sigma^2 (\tau^2 N + \sigma^2)}}$$
> 
> $$\color{violet}{= \frac{N^2 \bar{x} \tau^4 + \sigma^4 m^2 + 2 \sigma^2 \tau^2 m N \bar{x}}{2 \sigma^2 \tau^2 (\tau^2 N + \sigma^2)} = \frac{\frac{N^2 \bar{x}^2 \tau^2}{\sigma^2} + \frac{\sigma^2 m^2}{\tau^2} + 2mN\bar{x}}{2 (\tau^2 N + \sigma)}}$$
> 
> Therefore, bringing it all together, we obtain 
> 
> $$
\begin{align}
p(\boldsymbol{X}) &=  \frac{1 }{(\sigma\sqrt{2\pi})^n} \exp \left[-\frac{\sum_i x_i^2}{2\sigma^2}-\frac{m^2}{2\tau^2} \right] \exp \left[ \color{violet}{\frac{1}{2} \frac{(S^2 N\bar{x} +T^2 m)^2}{S^2 N + T^2} }\right] \color{lime}{\frac{\sqrt{2\pi}}{(T^{-1}\sqrt{2\pi})\sqrt{S^2N + T^2}}} \\
&= \frac{1 }{(\sigma\sqrt{2\pi})^n} \exp \left[-\frac{\sum_i x_i^2}{2\sigma^2}-\frac{m^2}{2\tau^2} \right] \exp \left[ \color{violet}{\frac{\frac{N^2 \bar{x}^2 \tau^2}{\sigma^2} + \frac{\sigma^2 m^2}{\tau^2} + 2mN\bar{x}}{2 (\tau^2 N + \sigma)} }\right] \color{lime}{\frac{\sigma}{\sqrt{\tau^2N + \sigma^2}} } \\
&= \frac{\sigma}{(\sigma\sqrt{2\pi})^n \sqrt{\tau^2N + \sigma^2}} \exp \left[-\frac{\sum_i x_i^2}{2\sigma^2}-\frac{m^2}{2\sigma_0^2} \right] \exp \left[ \frac{\frac{N^2 \bar{x}^2 \tau^2}{\sigma^2} + \frac{\sigma^2 m^2}{\tau^2} + 2mN\bar{x}}{2 (\tau^2 N + \sigma)} \right] 
\end{align}
$$
> 
> By substituting the $\tau$ and $m$ terms back again, we obtain 
> 
> $$\bbox[teal,4pt]{p(\boldsymbol{X}) = \frac{\sigma}{(\sigma\sqrt{2\pi})^n \sqrt{\sigma_0^2N + \sigma^2}} \exp \left[-\frac{\sum_i x_i^2}{2\sigma^2}-\frac{\mu_0^2}{2\sigma_0^2} \right] \exp \left[ \frac{\frac{N^2 \bar{x}^2 \tau^2}{\sigma^2} + \frac{\sigma^2 \mu_0^2}{\sigma_0^2} + 2 \mu_0 N\bar{x}}{2 (\sigma_0^2 N + \sigma)} \right] }$$

## Conclusion

Bringing it all together, if one is to have a dataset $\boldsymbol{X}$ with $N$ examples, which are all univariate, the **likelihood** of obtaining the dataset given some mean $\mu$, is 

$$\bbox[teal,4pt]{p(\boldsymbol{X} | \mu) = \mathcal{N} \left(\bar{x} \bigg| \mu , \frac{\sigma^2}{N} \right) }$$

The **prior distribution** for the mean $\mu$ has a prior mean $\mu_0$ and variance $\sigma_0^2$ being represented as 

$$ \bbox[teal,4pt]{p(\mu) = \mathcal{N}(\mu | \mu_0, \sigma_0^2) }$$

The **posterior distribution** for the mean given the dataset can be described as

$$\bbox[teal,4pt]{p(\mu | \boldsymbol{X} ) = \mathcal{N} \left( \mu \bigg| \underbrace{\frac{\sigma^2}{N\sigma_0^2 + \sigma^2}\mu_0 + \frac{N\sigma_0^2}{N\sigma_0^2 + \sigma^2} \bar{x}}_{\mu_N}, \underbrace{\frac{\sigma^2\sigma_0^2}{N\sigma_0^2 + \sigma^2}}_{\sigma^2_N} \right) }$$

And in order to identify the probability of a probe sample $x$ given the dataset $\boldsymbol{X}$ can be described as

$$\bbox[teal,4pt]{p(x|\boldsymbol{X}) = \mathcal{N} (x|\mu_N, \sigma_N^2 + \sigma^2)}$$

Finally, to obtain the marginal likelihood of the dataset, one can compute as

$$\bbox[4pt,teal]{p(\boldsymbol{X}) =\frac{\sigma}{(\sqrt{2\pi}\sigma)^n \sqrt{N\sigma_0^2 + \sigma^2}} \exp \left( -\frac{\sum_i x_i}{2\sigma^2} - \frac{\mu_0^2}{2\sigma_0^2} \right) \exp \left[\frac{1}{2(N\sigma_0^2 + \sigma^2)} \cdot \left( \frac{\sigma_0^2 N^2 \bar{x}^2 }{\sigma^2} + \frac{\sigma^2\mu_0^2}{\sigma_0^2} + 2N\bar{x} \mu_0 \right) \right]}$$










## Sources

- Kevin P. Murphy ["Conjugate Bayesian Analysis of the Gaussian Distribution"](https://www.cs.ubc.ca/~murphyk/Papers/bayesGauss.pdf) 3 Oct 2007
- Christopher Bishop - Pattern Recognition 
