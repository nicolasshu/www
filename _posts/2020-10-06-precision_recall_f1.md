---
layout: article
title: "Precision, Recall, and F1 Score"
tags:
  - Math
  - Machine Learning
permalink: /.html
mathjax: true
---

## Why?

Precision, recall, and F1 score is always something I have a problem understanding, so I have decided to write this to help myself remember every time I forget. Let us first define some evaluation metrics, and then, we will go into precision, recall, and finally the F1 score



## Evaluation Metrics Definitions

### False Positive / False Alarm / Type I Error

This is when something is marked as positive, but in reality, it isn't positive.  

E.g. A patient who is diagnosed to have cancer, but in reality, does not have cancer is a false positive. 

### False Negative / Miss / Type II Error

This is when something is marked as negative, but actually it was positive. 

E.g. A patient goes to a physician, but is sent home because the physician said he was fine. If, in reality (s)he had a disease, (s)he is a false negative. 

### Sensitivity / Recall / Hit Rate / True Positive Rate

$$
TPR = \frac{TP}{P} = \frac{TP}{TP + FN} = \text{How many positive cases are actually positive?}
$$

This says how often did an agent classify something as positive when that sample was in fact positive. In other words, the proportion of positives that are correctly identified. 

E.g. Percentage of sick people to be correctly identified as being sick. 

### Specificity / Selectivity / True Negative Rate 

$$
TNR=\frac{TN}{N} = \frac{TN}{TN+FP} = \text{How many negative cases are actually negative?}
$$

This says how often did an agent classify something as negative when that sample was in fact negative. In other words, it measures the proportion of negatives that are correctly identified.

E.g. The percentage of healthy people who are actually identified as being healthy. 

### Precision / Positive Predictive Value

$$
PPV=\frac{TP}{TP+FP}
$$

This tries to answer what proportion of positive identifications were actually correct. An agent that produces no false positives has a precision of 1. 



## Precision and Recall

Let us remember the definitions of precision and recall:
$$
\text{precision} = \frac{TP}{TP+\color{yellowgreen}{FP}} \quad \quad \quad \text{recall}=\frac{TP}{TP+\color{cyan}{FN}}
$$
Ideally, you want to have both precision and recall to be equal to 1. As one can see, when you choose to focus more on precision, it means that you choose to minimize the false positives. When you choose to focus on recall, you want to lower the number of false negatives. Now, why would we want to have precision and recall? Isn't accuracy enough?

### Example: Why do we need precision/recall?

Let us consider another scenario, where we have 9990 healthy patients and 10 progeria patients. Progeria is an extremely rare disorder where kids have a mutation at the gene which encodes the protein lamin A, which promotes genetic stability. This is one of those extremely rare diseases, which has an occurence of 1 every 20 million people. Let's say we have a model, regardless of the patient, the model diagnoses as a negative

```python
def model(patient):
    return False
```

This means that this model will have have a 99.9% accuracy. However, we know very well that this model just misdiagnosed every single cancer patient! :O What happens if we compute precision and recall?
$$
\begin{align}
\text{precision}&=\frac{0}{0+0}=undefined\\
\text{recall}&= \frac{0}{0+10} = 0.0
\end{align}
$$
This starts to tell us a better story! Here, recall tells us that it has gotten none of the sick patients! And here, since there are no positive predictions, then it is defined. Let us start to have a better interpretation of these two values.

### Example: Interpretation

A doctor diagnosed a number of patients and in the end, he found out that there were:

- True Positives: 5
- False Positives: 2
- False Negatives: 8
- True Negatives: 30

Here, we calculate that the precision is 71% and the recall is 38%. What does this mean?

- (Precision) When the doctor predicts a patient is sick, (s)he is correct 71% of the time
- (Recall) This doctor correctly identifies 38% of all of the sick patients

In other words, the two metrics try to answer the following questions:

- (Precision) Of the people who are diagnosed as sick, how many are _actually_  sick?
- (Recall) Of the people that are actually sick, how many are diagnosed as sick?



### Behavior of Trade-Off

It is often the case that when you elevate the precision, you lower the recall and vice versa. This happens because, let us consider the following distribution, where a classifier tries to determine a threshold where the right is classified as positive (`o`), and the left as negative (`x`). 

```
x x x x o x x x o x o x o o o o 
```

Let us start with the following case, with a precision of 0.75, and recall of 0.86

```
x x x x o x x x|o x o x o o o o       TP: 6 | FP: 2 | TN: 7 | FN: 1
```

If you want to increase the precision, you want to minimize the false positives, you move the threshold to the right. This yields a precision of 1.00, and a recall of 0.57.

```
x x x x o x x x o x o x|o o o o       TP: 4 | FP: 0 | TN: 9 | FN: 3
```

If you want to increase the recall, you want to minimize the false negatives, you move the threshold to the left. This yields a precision of 0.58, and a recall of 1.00

```
x x x x|o x x x o x o x o o o o       TP: 7 | FP: 5 | TN: 4 | FN: 0
```

So because you are taking one risk (e.g. FP/FN) over the other (e.g. FN/FP), the precision and recall are often inversely related. 



### Which to focus on? Precision or Recall?

So which one do we care about? Depending on the problem scenario, you may wish to focus more on recall or on precision. For example, if we are dealing with a scenario where a positive sample is an aggressive case of a disease. This is an example in which you shouldn't care much about the false positive cases, but you'd likely want to minimize the false negative cases. In other words, you'd much rather tell a patient (s)he has a disease even if (s)he doesn't have it, than to miss it by saying that (s)he doesn't have it, and saying: "Whoops! My bad."

Alternatively, in a judicial system, you might want to have a low recall and a high precision. By having such system, it results in you maybe letting some guilty people go, however, you want to make sure that when you sentence someone to prison, you want to be absolutely 100% sure that that individual committed the crime. Otherwise, you'll be punishing an innocent person. 

## F$_1$ Score and F$$_\beta$$ Score 

As one can see from the above, the precision and recall are two quantities which hard to compare between two models. For example, let us say that there are two physicians who, when seeing their performance, they end up having 

| Metric    | Physician A | Physician B |
| --------- | ----------- | ----------- |
| Precision | 60%         | 50%         |
| Recall    | 70%         | 80%         |

Which one performs best? This really depends on whether you care more about the precision or recall. However, ideally it would be nice to have a single metric that allows one to have a normalized idea of who is better. This is when the F-measure was introduced in 1992 at the Fource Message Understanding Conference [2]. 

Remember that we want to have both precision and recall to be closest to 1.0 as possible. Let us say that we have a model to determine a disease that has a precision and recall to be 0.9 and 0.1 respectively. If we are to take the arithmetic mean to be 0.5. But this makes no sense, does it? Because it is basically doing terrible in catching the disease! If we were to calculate the harmonic mean, it would be 0.33.
$$
\begin{align}
\mu_a &= \frac{precision+recall}{2} = \frac{0.9+0.1}{2} = 0.50 \\
\mu_h &= \frac{1}{\frac{1}{2}\frac{1}{precision} + \frac{1}{2}\frac{1}{recall}} = \frac{2}{\frac{1}{0.9} + \frac{1}{0.1}} = 0.33
\end{align}
$$
This is a much better depiction of how the model is actually performing! 

So the F1 score is in fact the harmonic mean between precision and recall:
$$
F_1 = \frac{2 \cdot precision \cdot recall}{precision \cdot recall}
$$


### Derivation and Understanding of the F-Measure

Now, where does this come from? The proper definition of the generalized F-measure, which is known as the $F_\beta$-score is 
$$
F_\beta = (1+\beta^2)\frac{PR}{\beta^2P+R} \quad s.t. \quad 0 \leq \beta \leq \infty \quad [\text{Chinchor, 1992}]
$$
 where $\beta$ is a parameter which controls the balance between your precision and recall preferences. 

| $\beta$ | Result                        |
| ------- | ----------------------------- |
| $=1$    | Equals the harmonic mean      |
| $>1$    | Focuses more on the recall    |
| $<1$    | Focuses more on the precision |
| $=0$    | $F_0 = P$                     |

Technically, van Rijsbergen defined an effectiveness funcion $E$ in 1979, which is defined as 
$$
E = 1 - \frac{1}{\alpha \frac{1}{P} + (1-\alpha)\frac{1}{R}}
$$
When we set $\alpha = (1+\beta^2)^{-1}$, we have 
$$
\begin{align}
E &= 1 - \frac{1}{\alpha \frac{1}{P} + (1-\alpha)\frac{1}{R}} \\
&= 1 - \frac{1}{\frac{1}{1+\beta^2} \frac{1}{P} + \left(1-\frac{1}{1+\beta^2}\right)\frac{1}{R}} \\
&= 1 - \frac{1}{\frac{\beta^2 + 1-1}{1+\beta^2} \frac{1}{P} + \frac{1}{1+\beta^2} \frac{1}{R}} \\ 
&= 1 - (1+\beta^2)\frac{PR}{\beta^2 P + R} \\
&= 1 - F_\beta
\end{align}
$$
So, we can consider 
$$
F_\beta = \frac{1}{\alpha \frac{1}{P} + (1-\alpha)\frac{1}{R}} \quad s.t. \quad 0\leq \alpha \leq 1
$$
And note that $F_{\alpha=0.5} = F_{\beta=1}$, thus making $F_1$ being the harmonic mean of the precision and recall.

### Why $\beta^2$ and not $\beta$? 

When the gradients of the efficiency (also for the F-measure) with respect to precision and recall are equal, it means that the ratio of recall to precision is the desired ratio. 
$$
\frac{\partial E}{\partial P} = - \frac{R[\alpha R + (1-\alpha)P] - PR(1-\alpha)}{(\alpha R + (1-\alpha)P)^2}\\
\frac{\partial E}{\partial R} = - \frac{P[\alpha R + (1-\alpha)P] - PR\alpha}{(\alpha R + (1-\alpha)P)^2}
$$

$$
\begin{align}
\frac{R[\alpha R + (1-\alpha)P] - PR(1-\alpha)}{(\alpha R + (1-\alpha)P)^2} &= \frac{P[\alpha R + (1-\alpha)P] - PR\alpha}{(\alpha R + (1-\alpha)P)^2} \\
R[\alpha R + (1-\alpha)P] - PR(1-\alpha) &= P[\alpha R + (1-\alpha)P] - PR\alpha \\
\alpha^2R^2 &= (1-\alpha)P^2\\
\end{align}
$$
Since $\beta=R/P$, we can replace $R$ with $\beta P^2$,  we can say 
$$
\begin{align}
\alpha \beta^2 P^2 &= (1-\alpha) P^2\\ 
\alpha \beta^2 &= 1-\alpha\\ 
\alpha (\beta^2+1) &= 1\\ 
\alpha &= \frac{1}{\beta^2+1}\\ 
\end{align}
$$


## Resources 

[1] [The Truth of the F-Measure](../assets/pdf/Sasaki_2007_The Truth of the F-measure.pdf)

[2] [Overview of the Fourth Message Understanding Evaluation and Conference](../assets/pdf/M92-1001.pdf)