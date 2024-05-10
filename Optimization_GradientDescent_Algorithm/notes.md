## Understand what is a Cost Function/Loss Function/Error Function (maybe) Objective Function 
1. From Google [Colab](https://colab.research.google.com/drive/1yVl3doA694Grmn5fWZ63vA72ETmGvs47#scrollTo=1TjiUQtp2kst)
- $J(\theta_0, \theta_1) = \sum_{i=1}^n (h\theta(x)_i-y_i)^2$

Also can be called the residual sum of squares.

Notes in my public [Colab](https://colab.research.google.com/drive/1eTJ7r5bTgJXFcnWR2gt-C0kwRaZhxj3W#scrollTo=0xL2nseyL6_B)
- Summary of simple things and simple commands:
    - Generating Data with numpy using  `numpy.linspace`
    - Suplots and scatter plots with `matplotlib` to plot Cost function and its derivative
    - Gradient Descent Algorithm for a single-variable function:   $ x_{new} = x_{old} - \frac{dy}{dx}\cdot \eta $
    - Functions for which the algorithm was used on: function is on `"./algorithms.py"`
        - $f1(x) = (x+2)^2 $
        - $ f2(x) = x^4 - 4x^2 + 5$
        - $ h(x) = x^5 -2x^4 + 2 $
    - Batch gradient descent vs stocastic gradient descent
    - Gradient descent algorithm for two-variable function with partial derivative
        - Sympy module -> `diff()`, `.evalf()`
        - Creating a 3D plot with mpl_toolkits
        - Loops and performance considerations with gradient descent algorithm
    - Using `.reshape()` and 2D arrays for calculating the MSE Cost function
        - Plotting this 3D cost function 

# Harder concepts: Understanding the difference between a cost function and a data point
Previously we used our own cost function like $f(x)$ or $f(x,y)$

Now, we have to create a cost function from an existing data set.

In order to do these there are two important formulas to keep in mind:
1. Linear Regression formula
    $$y = \theta_0 + \theta_1x$$
2. Mean Squared Error
    $$MSE = \frac{1}{n}\sum_{i=1}^n(y-\hat{y})^2$$

Now we substitute $y$ from (formula 1) to $\hat{y}$ in (formula 2)

$$MSE = \frac{1}{n}\sum_{i=1}^n(y-\theta_0 - \theta_1x)^2$$
$$MSE = \frac{1}{n}\sum_{i=1}^n(y-\theta_0 - \theta_1x)(y-\theta_0 - \theta_1x)$$
$$MSE = \frac{1}{n}\sum_{i=1}^n(y^2-2\theta_0y-2\theta_1xy+\theta_0^2+2\theta_0\theta_1x+\theta_1^2x^2)$$

This formula makes it easier for us to calculate $\large{\frac{\partial MSE}{\partial\theta_0}}$ and $\large{\frac{\partial MSE}{\partial\theta_1}}$

