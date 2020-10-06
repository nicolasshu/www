import numpy as np
import matplotlib.pyplot as plt


high_order = 20
polyOrders = np.array(range(high_order))
# Generate numbers
N = 40
x = np.linspace(0,10,N)
rand_mag = 100

y1 = x      + np.random.randn(x.shape[0])*rand_mag
y2 = x**2   + np.random.randn(x.shape[0])*rand_mag
y3 = x**3   + np.random.randn(x.shape[0])*rand_mag
y4 = 30*np.sin(x) + np.random.randn(x.shape[0])*rand_mag
y5 = 12*np.cos(x+1.2) + np.random.randn(x.shape[0])*rand_mag
y = (y1+y2+y3+y4)/4


# ==============================================================================
# JUST CHECKING
# ==============================================================================
plt.figure()
plt.plot(x,y,'bo',label='Random Numbers')
plt.xlabel('x')
plt.ylabel('y')

# EXAMPLE OF 2nd ORDER POLYNOMIAL FIT
coeffs2 = np.polyfit(x, y, 2)
polyFn2 = np.poly1d(coeffs2)
plt.figure()
plt.plot(x,y,'bo'); plt.plot(x,polyFn2(x),'r-')

# ITERATING THROUGH DIFFERENT POLYNOMIALS
for order in range(high_order):
    coeffs = np.polyfit(x,y, order )
    polyFn = np.poly1d(coeffs)

    title_str = 'Polynomial (Order %d)' % order

    plt.figure()
    plt.plot(x,y,'bo',label='Original Data Points')
    plt.plot(x,polyFn(x),'r-',label=title_str)
    plt.xlabel('x'); plt.xlabel('y'); plt.legend()


plt.close('all')
# ===========================================================
# LEAVE-ONE-OUT
# ===========================================================
results = np.zeros((high_order,N))

for order in range(high_order):

    plt.figure(order)
    plt.plot(x_mod,y_mod,'co',label='Modified Points')
    for iter in range(len(x)):
        x_mod = np.delete(x,iter)
        y_mod = np.delete(y,iter)

        coeffs = np.polyfit(x_mod,y_mod,order)
        polyFn = np.poly1d(coeffs)

        y_pred = polyFn(x[iter])
        y_true = y[iter]
        # Get the residual squared on that single data point that was excluded
        thisError = (y_true - y_pred)**2

        # Store on Results
        results[order,iter] = thisError

        plt.figure(order)
        plt.plot(x,polyFn(x),'r-',label='Predicted Points')

        #plt.plot(x[iter],y[iter],'g*',markersize=20,label='Removed Point')
    plt.xlabel('x'); plt.ylabel('y'); plt.title('Polynomial (Order = %d)' % order)
# Remove zeroth order
results = np.delete(results,0,0)

#Calculate Estimated Prediction Error
PE = np.sum(results,axis=1)/N

# Show the Estimated Mean Prediction Errors for Each Polynomial

plt.figure()
plt.plot(PE,'bo-')
plt.xlabel('Polynomial Order')
plt.ylabel('Estimated Mean Prediction Error')

plt.close('all')

# ===========================================================
# K-FOLD
# ===========================================================
from sklearn.model_selection import KFold
rounds = 2
K = 5



results_list = []               # Each element will be for one round
for round in range(rounds):
    # For each round of results...

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
            coeffs = np.polyfit(x,y, order )
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
        len(results_list)


for result_item in results_list:
    plt.plot(polyOrders[1:],result_item[1:],'o-')

plt.xlabel('Polynomial Order')
plt.ylabel('PE Value')
