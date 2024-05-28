import numpy as np

# Gradient Descent Algorithm single-variable functions
def gradient_descent(derivative_func, initial_guess : float, multiplier : float, precision : float, max_iter : int):
    # Initialize x
    new_x = initial_guess
    x_list = new_x

    # Store values for returning 
    new_x_values = []

    for i in range(max_iter):
        previous_x = new_x
        gradient = derivative_func(new_x)
        new_x = previous_x - multiplier * gradient
        new_x_values.append(new_x)

        step_size = abs(new_x - previous_x)
        if step_size < precision:
            print(f'Loop ran {i} times')
            break
    # Convert from list to array
    values = np.array(new_x_values)
    slope_values = derivative_func(values)

    return values, slope_values

# Gradient Descent Algorithm Two-variable functions

# Gradient Descent Algorithm two-variable functions
def gradient_descent(function, gradients: np.array, initial_guess : np.array, multiplier : float, precision : float, max_iter : int):
    # Initialize parameters of 2D numpy array
    params = initial_guess
    for i in range(max_iter):
        old_params = params
        params = params - multiplier * gradients
        step_size = abs(params - old_params).sum() # Sum of the cost from each partial derivative
        if step_size < precision:
            print(f'Loop ran {i} times')
            break
    # Results:
    print(f'Values in gradients array: {gradients}')
    print(f'The minimum cost is: {function(params[0], params[1])}') # Where f is the function to minimize
        