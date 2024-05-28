## Understand what is a Cost Function/Loss Function/Error Function (maybe) Objective Function 
1. From Google [Colab](https://colab.research.google.com/drive/1yVl3doA694Grmn5fWZ63vA72ETmGvs47#scrollTo=1TjiUQtp2kst)
- $J(\theta_0, \theta_1) = \sum_{i=1}^n (h\theta(x)_i-y_i)^2$

Also can be called the residual sum of squares.
The goal of gradient descent is to minimize the value of $J(\theta_0, \theta_1)$
- It is easy to get confused with these new terms like $\theta_0$, $\theta_1$, $J$, $H$

## Understanding recap:
- $h_{\theta}(x) = \theta_0 + \theta_1x$, this is a new notation in machine learning rather than the mathematical notation $y = mx + c$
- $J$ is a cost function that measures how well a model predicts the actual data by using $MSE$
- Gradient Descent is an optimization algorithm where we try to minimize the value from $J(\theta_0, \theta_1)$
- The gradient descent algorithm will require these parameters to get updated as we try to minimize the value of $J$ by descending down the gradient:
$$\theta_1 := \theta_1 - \alpha \frac{1}{m} \frac{\partial J(\theta_0, \theta_1)}{\partial \theta_1} $$
- Note that in Multi-variable cost functions requires understanding of vector calculus, as the parameters could be a vector (2D numpy.array())
$$ \theta := \theta - \nabla_{\theta}J(\theta) $$ 

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

$$\frac{\partial MSE}{\partial \theta_0} = -\frac{2}{n}\sum_{i=1}^n(y^(i) - \theta_0 - \theta_1x^(i))$$
$$\frac{\partial MSE}{\partial \theta_1} = -\frac{2}{n}\sum_{i=1}^n(y^(i) - \theta_0x - \theta_1x^2)(x^(i))$$

## Understanding Regression Analysis:
In the google colab I have 2 variables:
- `x_5` and `y_5` both are numpy arrays of size `(7,1)`

Applying regression to these variables (dependent and independent):

`regr = LinearRegression()`

`regr.fit(x_5, y_5)`

The `def fit(X, y, sample_weight=None)` takes an `X` and a `y` parameter which can both be matrices.
- In single variable Linear Regression -> `X` and `y` both have size `(n,)` 
- However, multi-variable linear Regression allows for `(n_samples, n_features)` in `X` and `(n_samples, n_targets)` in `y`
- `sample_weights` is simply a 1D array -> `(n_samples,)`

Observation: sample of data
- Student
Features: characteristic/attribute of the observation
- age, sex, grade

Literally like a database table.

# Advanced Mathematics with Linear Algebra in Linear Regression
## Bivariate Model
Two Independent variables and one dependent variables.
## Multiple Linear Regression:
Independent variables are $(\vec{X_1}, \vec{X_2}, ..., \vec{X_n})$ and one dependent variable $({Y})$
- Goal is to find a hyperplane that minimizes the squared differences between the actual and predicted values of Y
$$y = w_0 + w_1X_1 + w_2X_2 + ... w_nX_n + e $$
In Matrix form:
$$\vec{Y} = X \vec{w} + \vec{e}$$
where:
- $\vec{Y}$ is a vector of size $n$
- $X$ is a ($n$ x $p$) matrix, where $n$ is the observation and $p$ represents a variable
- $\vec{w}$ is a vector of linear coefficients
- $\vec{e}$ where each element is an error term