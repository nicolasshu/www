---
layout: article
title: "Cross-Validation (a.k.a. Rotation Estimation)"
tags:
  - Math
  - Machine Learning
permalink: cross_validation.html
---

Cross-validation is a pretty cool method to compare different models that you're trying to fit your data to, and see which models are yield the most robust results. This inherently means that the most robust models are the least prone to find themselves overfitting to your data.

---  
---  

# Theory
## Types
### Leave-One-Out Cross-Validation
### Leave-p-Out Cross-Validation
### k-Fold Cross-validation

---  
---  

# Examples
So here are two examples of using it. For these examples, we will be comparing different polynomial orders, e.g.

$$y = \beta_0 + \beta_1 x_1$$

$$y = \beta_0 + \beta_1 x + \beta_2 x^2$$

$$y = \beta_0 + \beta_1 x + \beta_2 x^2 + \cdots + \beta_k x^k$$

and we will be using the [mean squared error](http://nicolasshu.com/math/2018/05/17/matherrors.html) to quantify our errors.

---

## Big Picture First
### Import the Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
```
### Set the Highest Order to be used
```python
high_order = 20
polyOrders = np.array(range(high_order))
```
### Generate the Numbers
We will first set a number of datapoint $$N$$, and for this case, I just decided to have

$$\vec{y} = \vec{y_1} + \vec{y_2} + \vec{y_3} + \vec{y_4} \quad \text{ where}$$

$$ \begin{cases}
\vec{y_1} = \vec{x} + \text{randomness} \\
\vec{y_2} = \vec{x}^2 + \text{randomness} \\
\vec{y_3} = \vec{x}^3 + \text{randomness} \\
\vec{y_4} = 30 \sin(\vec{x}) + \text{randomness} \\
\end{cases}$$

because why not?
```python
N = 40
x = np.linspace(0,10,N)
rand_mag = 100

y1 = x      + np.random.randn(x.shape[0])*rand_mag
y2 = x**2   + np.random.randn(x.shape[0])*rand_mag
y3 = x**3   + np.random.randn(x.shape[0])*rand_mag
y4 = 30*np.sin(x) + np.random.randn(x.shape[0])*rand_mag
y = (y1+y2+y3+y4)/4
```

When plotting it, we **MAY** have the following data (don't forget that there is a randomness that I added to it)
```python
plt.figure()
plt.plot(x,y,'bo',label='Random Numbers')
plt.xlabel('x')
plt.ylabel('y')
```

[INSERT FIGURE]

### What's our main question?
So, the question is,

And we can fit it to a polynomial by using `numpy.polyfit()`, e.g.
```python
ORDER = 2
coeffs2 = np.polyfit(x, y, ORDER)
polyFn2 = np.poly1d(coeffs2)
plt.figure()
plt.plot(x,y,'bo'); plt.plot(x,polyFn2(x),'r-')
```

[INSERT FIGURE]

But the question is:  
**We can fit multiple different polynomial order models to our data, but which one is the best? How can we decide it?**

[INSERT MULTIPLE FIGURES - 6 orders in 2x3 or 3x2 fashion]

Below we will see only two types of cross-validation being applied

---

## Leave-One-Out Cross-Validation (LOOCV)
As explained above, the Leave-One-Out method looks at every possibility when you remove a single datapoint, train the model on the $$N-1$$ datapoints, and then see how the robust is the model towards that datapoint

*Again, these scripts may not be the most efficient ways of doing cross-validation, but it's to lay a good framework of how it works*

### Initiate the Results
We can first create a `results` array, where we will store the results. This array will be in $$\mathbb{R}^{\text{Number of Orders} \times N}$$, where $$N$$ is the number of datapoints

### Validate it for Every Datapoint
So as stated before, we're going to iterate through every datapoint, and for each datapoint, we're going to remove it, and train the model based on the rest.

```python
        # PARTIAL
        # Remove this datapoint
        x_mod = np.delete(x,iter)
        y_mod = np.delete(y,iter)

        # Train the model
        coeffs = np.polyfit(x_mod,y_mod,order)
        polyFn = np.poly1d(coeffs)
```

We will then predict the labels $$y_{pred}$$, and then, by using the [mean squared error](http://nicolasshu.com/math/2018/05/17/matherrors.html) (we will first compute the squared residual, and later on take the mean)

$$ Residual^2 = (y_{true} - y_{pred})^2$$

```python
        # PARTIAL
        # Predict the results
        y_pred = polyFn(x[iter])
        y_true = y[iter]

        # Get the residual squared on that single data point that was excluded
        thisError = (y_true - y_pred)**2
```

Then we will store that $$residual^2$$ on the `results` array, and we can plot it for funsies too

```python
        # PARTIAL
        # Store on Results
        results[order,iter] = thisError

        # (OPTIONAL) Plot those predictions
        plt.plot(x,polyFn(x),'r-',label='Predicted Points')
```

### Iterate through different polynomial orders
All there is left to do is to let it iterate it through different orders
```python
for order in range(high_order):
```

### Complete Validation of Every Point for Every Polynomial Order
Your complete cross-validation will be the following:
```python
results = np.zeros((high_order,N))

for order in range(high_order):
    # For each polynomial order...
    plt.figure(order)
    plt.plot(x,y,'bo',label='Modified Points')

    for iter in range(len(x)):
        # For every data point...

        # Remove this datapoint
        x_mod = np.delete(x,iter)
        y_mod = np.delete(y,iter)

        # Train the model
        coeffs = np.polyfit(x_mod,y_mod,order)
        polyFn = np.poly1d(coeffs)

        # Predict the results
        y_pred = polyFn(x[iter])
        y_true = y[iter]

        # Get the residual squared on that single data point that was excluded
        thisError = (y_true - y_pred)**2

        # Store on Results
        results[order,iter] = thisError

        # Plot those predictions
        plt.plot(x,polyFn(x),'r-',label='Predicted Points')
        #plt.plot(x[iter],y[iter],'g*',markersize=20,label='Removed Point')
    plt.xlabel('x'); plt.ylabel('y'); plt.title('Polynomial (Order = %d)' % order)
```

[INSERT A FEW OF THE FIGURES 3x2 or 2x3]

### Show Your Results
All you have to do left is to plot your results. Here, remember how I didn't compute the mean of the MSE? I am now going to compute that mean

```python
# Remove zeroth order
results = np.delete(results,0,0)

#Calculate Estimated Prediction Error
PE = np.mean(results,axis=1)

# Show the Estimated Mean Prediction Errors for Each Polynomial
plt.figure()
plt.plot(PE,'bo-')
plt.xlabel('Polynomial Order')
plt.ylabel('Estimated Mean Prediction Error')
```

[INSERT THAT LAST FIGURE!]

---

## k-Fold Cross-validation

As explained above, the k-Fold cross validation requires one to separate your data into k parts, which may be randomized or not, remove one of the parts, train the data on the rest, and iterate through the different parts.

To do so, you can choose to build your partitioning algorithm from scratch (I highly suggest it as it cranks out your coding kung fu), or you can use [SciKit Learn](http://scikit-learn.org/stable/index.html)'s [`KFold`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html)

### Import that Function
```python
from sklearn.model_selection import KFold
```

### Initialize Some Constants
In this case, I'm setting that I'll repeat the experiment for 20 rounds, and I would like to partition the data into 5 parts. I am also initializing a list `results_list`, where I'll store my results

```python
rounds = 20
K = 5
results_list = []               # Each element will be for one round
```

### Start Up the KFold Class
So, we gotta start up our KFold class, to start to use its set of tools, and then we can split up our data, which is stored in `x`
```python
    # Initiate the KFold Class
    kf = KFold(n_splits=K, shuffle=True)

    # Separate Data into K parts
    kf.get_n_splits(x)
```

If you'd like to get some of the status, we can write

```python
>>> kf
KFold(n_splits=10, random_state=None, shuffle=True)
```

### Start Validating Your Parts/Folds
For each experiment (i.e `round`), we will use an array `results` to get the validation results.

```python
    results = np.zeros((high_order,K))
```

For each part/fold, we will separate the data into the training set (`x_train`, `y_train`) and testing set (`x_test`, `y_test`)

```python
    # PARTIAL
    for iter, (train_index, test_index) in enumerate(kf.split(x)):
        # For each split...
        # Now we have the indices for the training set and the test set
        x_train, x_test = x[train_index], x[test_index]
        y_train, y_test = y[train_index], y[test_index]
```

in which we can plot it for funsies

```python
        # PARTIAL
        # Plot the training set and the test set together
        plt.figure()
        plt.plot(x_train,y_train,'bo')
        plt.plot(x_test,y_test,'rx')
        plt.xlabel('x'); plt.ylabel('y')
```

Now for each polynomial order, we can train the model, and create a polynomial function
```python
        # PARTIAL
        for order in range(high_order):
            # For each polynomial order...
            # Train the model based on the training set and create a polynomial function
            coeffs = np.polyfit(x_train,y_train, order )
            polyFn = np.poly1d(coeffs)
```

Next, we calculate the predictions $$y_{pred}$$, and we can calculate the mean squared error based on the residuals, and we can store that onto the `results` (numpy array).

```python
            # Calculate the predictions
            y_pred = polyFn(x_test)

            # Calculate the estimated prediction error
            thisError = np.mean((y_test - y_pred)**2)

            # Store on Results
            results[order,iter] = thisError
```


Remember, the way that we are storing things is, if we had 3 parts/folds and were testing on two polynomial orders

$$y = \beta_0 + \beta_1 x_1$$

$$y = \beta_0 + \beta_1 x + \beta_2 x^2$$

<img src='https://g.gravizo.com/svg?
digraph G {
     "y_pred \n (Order 1 \n Fold 1)" -> "thisError \n (Order 1 \n Fold 1)" [label="MSE w/ \n y_test"]
     "y_pred \n (Order 1 \n Fold 2)" -> "thisError \n (Order 1 \n Fold 2)" [label="MSE w/ \n y_test"]
     "y_pred \n (Order 1 \n Fold 3)" -> "thisError \n (Order 1 \n Fold 3)" [label="MSE w/ \n y_test"]
     "y_pred \n (Order 2 \n Fold 1)" -> "thisError \n (Order 2 \n Fold 1)" [label="MSE w/ \n y_test"]
     "y_pred \n (Order 2 \n Fold 2)" -> "thisError \n (Order 2 \n Fold 2)" [label="MSE w/ \n y_test"]
     "y_pred \n (Order 2 \n Fold 3)" -> "thisError \n (Order 2 \n Fold 3)" [label="MSE w/ \n y_test"]
    "thisError \n (Order 1 \n Fold 1)" -> "results \n Order 1"
    "thisError \n (Order 1 \n Fold 2)" -> "results \n Order 1"
    "thisError \n (Order 1 \n Fold 3)" -> "results \n Order 1"
    "thisError \n (Order 2 \n Fold 1)" -> "results \n Order 2"
    "thisError \n (Order 2 \n Fold 2)" -> "results \n Order 2"
    "thisError \n (Order 2 \n Fold 3)" -> "results \n Order 2"
    "results \n Order 1" -> "thisResult \n Order 1" [label=" Average"]
    "results \n Order 2" -> "thisResult \n Order 2" [label=" Average"]
    "thisResult \n Order 2" -> results_list
    "thisResult \n Order 1" -> results_list
}
'/>

All there's left to do is to store it onto the `results_list`

```python
    # PARTIAL
    # Put it on the list!
    results_list.append(thisResult)
```

### Complete Validation
Your complete validation for the K-Fold CV will be now iterating through different experiments (i.e. `rounds`), where in each experiment, you pull out some random elements, validate it, then in the next experiment, you put everything back into that bag, shake it, and repeat.

```python
from sklearn.model_selection import KFold
rounds = 20
K = 5
results_list = []               # Each element will be for one round
for round in range(rounds):
    # For each round of results...
    # Initiate the KFold Class
    kf = KFold(n_splits=K, shuffle=True)

    # Separate Data into K parts
    kf.get_n_splits(x)

    # To get status
    kf
    # KFold(n_splits=10, random_state=None, shuffle=True)

    results = np.zeros((high_order,K))

    for iter, (train_index, test_index) in enumerate(kf.split(x)):
        # For each split...
        # Now we have the indices for the training set and the test set
        x_train, x_test = x[train_index], x[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # Plot the training set and the test set together
        # plt.figure()
        # plt.plot(x_train,y_train,'bo')
        # plt.plot(x_test,y_test,'rx')
        # plt.xlabel('x'); plt.ylabel('y')

        for order in range(high_order):
            # For each polynomial order...
            # Train the model based on the training set and create a polynomial function
            coeffs = np.polyfit(x_train,y_train, order )
            polyFn = np.poly1d(coeffs)

            title_str = 'Polynomial (Order %d)' % order     # For book keeping

            # Calculate the predictions
            y_pred = polyFn(x_test)

            # Calculate the estimated prediction error
            thisError = np.mean((y_test - y_pred)**2)

            # Store on Results
            results[order,iter] = thisError

        thisResult = np.mean(results,axis=1)

    # Put it on the list!
    results_list.append(thisResult)
```

### Showing Your Results

Now, all you have to do is show your results, assuming you ran everything in the "**Big Picture**" section.

```python
for result_item in results_list:
    plt.plot(polyOrders[1:],result_item[1:],'o-')
plt.ylim((1000,10000))
plt.xlabel('Polynomial Order')
plt.ylabel('PE Value')
```
