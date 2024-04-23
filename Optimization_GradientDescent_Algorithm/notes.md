## Understand what is a Cost Function/Loss Function/Error Function (maybe) Objective Function 
1. From Google [Colab](https://colab.research.google.com/drive/1yVl3doA694Grmn5fWZ63vA72ETmGvs47#scrollTo=1TjiUQtp2kst)
- $J(\theta_0, \theta_1) = \frac{1}{m} \sum_{i=1}^n (h\theta(x)^i-y^i)^2$

Also can be called the residual sum of squares.

Notes in my public [Colab](https://colab.research.google.com/drive/1eTJ7r5bTgJXFcnWR2gt-C0kwRaZhxj3W#scrollTo=0xL2nseyL6_B)
- Summary:
    - Generating Data with numpy using  `numpy.linspace`
    - Suplots and scatter plots with `matplotlib` to plot Cost function and its derivative
    - Gradient Descent Algorithm for a single-variable function:   $ x_{new} = x_{old} - \frac{dy}{dx}\cdot \eta $
    - Functions for which the algorithm was used on: function is on `"./algorithms.py"`
        - $f1(x) = (x+2)^2 $
        - $ f2(x) = x^4 - 4x^2 + 5$
        - $ h(x) = x^5 -2x^4 + 2 $
    - Batch gradient descent vs stocastic gradient descent
    - Gradient descent algorithm for a 