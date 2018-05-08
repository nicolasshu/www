---
layout: page
title: "Bayes' Theorem - Prior, Likelihood, Posterior, Evidence"
categories:
  - Math
---
So, I'm not a very smart person. As a result, I keep forgetting some definitions, such as **prior**, **likelihood**, and **posterior** in Bayes' Theorem. Wikipedia actually has a pretty good article for [Bayes' Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem), but I write this for my own reference in remembering. I also give credit to [Chun Li](http://www.lichun.cc/blog/2013/07/understand-bayes-theorem-prior-likelihood-posterior-evidence/) for helping me understand the material better.

## Bayes' Theorem
So, we can write Bayes' Theorem as

$$ Pr(A|B) = \frac{Pr(B|A) \cdot Pr(A)}{Pr(B)}$$

This equates itself to

$$ \text{Posterior} = \frac{\text{Likelihood} \cdot \text{Prior}}{\text{Evidence}} $$

If we consider
$$\begin{cases}
A = \text{Joe Schmo knows music theory}\\
B = \text{Joe Schmo is a music performer}
\end{cases}$$

We can start from the easy, step by step.
#### Posterior $$Pr(A|B)$$
The Posterior states what is the probability that Joe Schmo knows music theory given that he knows how to play music.

#### Evidence $$Pr(B)$$
The evidence says: "This is what we already know!" From what we already know, we can then move onto trying to compute the Posterior

#### Prior $$Pr(A)$$
The prior says: "This is the probability that he knows music theory, knowing nothing about the guy." He could be a master player, but he could also not even know what music is. The point is that we don't know anything about the guy. This only provides the raw probability given no assumptions

#### Likelihood $$Pr(B|A)$$
*This is the one that most got to me.*
Likelihood essentially measures the extent that a sample provides support for a characteristic of a parameter in a parametric model. In layman's terms, you can think of it as:
- We're trying to figure out the $$Pr(A\|B)$$ for a scenario
- We know that just because $$B \rightarrow A$$, it does not mean $$A \rightarrow B$$, BUT, there is a proportional component to that assumption, such that, yes, $$A\rightarrow B$$ will not always be the case, but it doesn't mean it will NEVER be the case. Such that this does play a role in figuring out the posterior of an event $$A$$, given a previous event/assumption $$B$$.
