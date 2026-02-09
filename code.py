def max_satisfied(customers, grumpy, X):
    # Calculate the baseline
    baseline = 0
    for c, g in zip(customers, grumpy):
        if g == 0:
            baseline += c
    
    # Calculate the initial window's gain
    current_gain = 0
    for i in range(X):
        current_gain += customers[i] * grumpy[i]
    
    max_gain = current_gain
    
    # Slide the window
    for i in range(X, len(customers)):
        current_gain += customers[i] * grumpy[i]
        current_gain -= customers[i - X