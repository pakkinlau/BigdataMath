Related: [[over-determined|overdetermined]]


![[Pasted image 20231112232504.png|500]]

Polynomial fitting: 

Given the data points $(x_1, y_1), \dots, (x_m, y_m)$, we fine a polynomial of degree $n-1$, $p(x) = c_0 + c_1x + \dots + c_{n-1}x^{(n-1)}$ that fits the data, where we assume $m > n$. That is, we find $p(x)$ so that $p(x_i) \approx y_i$, $i = 1,2, \dots, m$.

Thus, we are solving the following system

$\begin{bmatrix} 1 & x_1 & & x_1^{n-1} \\  1 & x_2 & \dots & x_2^{n-1} \\ 1 & x_3 & & x_3^{n-1} 　\\ & \vdots & & \vdots \\  1 & x_m & & x_m^{n-1}  \end{bmatrix} \begin{bmatrix} c_0 \\ c_1 \\ \vdots \\ c_{n-1}\end{bmatrix} \approx \begin{bmatrix} y_1 \\ y_2 \\ y_3 \\ \vdots \\ y_m \end{bmatrix}$

Also $X\beta \approx Y$. The coefficients $c_0, c_1, \dots, c_{n-1}$ are from our proposed best fitting polynomial line $f(x) = c_0 + c_1x + c_2x^2 + \ldots + c_{n-1}x^{n-1}$.  

Objective function: $\underset{\beta}{min} ||Y - X \beta ||^2$
Solving this objective function give you the coefficient $c_0, c_1, \dots, c_{n-1}$ in $\beta$. That best fit the given polynomial to the data. 

When we determined $\beta$, The best fitting polynomial can be expressed as: $f(x) = c_0 + c_1x + c_2x^2 + \ldots + c_{n-1}x^{n-1}$

- Q: Why we need to use polynomial to frame data points?
	- It allows for capturing more complex relationships between the independent variable $x$ and the dependent variable $y$ than a simple linear fit. 
	- Using higher-degree polynomials allows for more flexibility in capturing the underlying patterns in the data.

---
To see why the above expression is valid, we can review simpler cases: 

If we set $n = 1$, the original problems becomes a simple linear model: 

$\begin{bmatrix} 1 & x_1 \\ 1 & x_2 \\ 1 & x_3 \\ \vdots & \vdots \\ 1 & x_m \end{bmatrix} \begin{bmatrix} c_0 \\ c_1 \end{bmatrix} \approx \begin{bmatrix} y_1 \\ y_2 \\ y_3 \\ \vdots \\ y_m \end{bmatrix}$

The best fitting line is a straight line $f(x) = c_0 + c_1 x$. 

If we set $n = 2$, the equation becomes: 

$X = \begin{bmatrix} 1 & x_1 & x_1^2 \\ 1 & x_2 & x_2^2 \\ 1 & x_3 & x_3^2 \\ \vdots & \vdots & \vdots \\ 1 & x_m & x_m^2 \end{bmatrix}, \quad \beta = \begin{bmatrix} c_0 \\ c_1 \\ c_2 \end{bmatrix}, \quad Y = \begin{bmatrix} y_1 \\ y_2 \\ y_3 \\ \vdots \\ y_m \end{bmatrix}$

The corresponding best fitting line a quadratic function in 2D space. 

Applying [[Least Squares]], and then we have $f(x) = c_0 + c_1x + c_2x^2$ and the coefficients $c_0, c_1, c_2$ determine the shape of this curve. 

---

### 3D linear (n=1) fitting

If you have 3D data points (x_i, y_i, z_i) and you want to find the best-fitting plane, you can extend the linear regression model to include the z-coordinate as well. The general form of the linear regression equation for a plane can be expressed as:
$$ \begin{bmatrix} 1 & x_1 & y_1 \\ 1 & x_2 & y_2 \\ 1 & x_3 & y_3 \\ \vdots & \vdots & \vdots \\ 1 & x_m & y_m \end{bmatrix} \begin{bmatrix} c_0 \\ c_1 \\ c_2 \end{bmatrix} \approx \begin{bmatrix} z_1 \\ z_2 \\ z_3 \\ \vdots \\ z_m \end{bmatrix}$$

In this equation:
- The first column of the matrix on the left is a column of ones, representing the constant term.
- The second column corresponds to the x-coordinates.
- The third column corresponds to the y-coordinates.

The vector on the right represents the z-coordinates of your 3D data points.

The matrix multiplication will give you a set of equations:
$$ c_0 + c_1x_i + c_2y_i \approx z_i$$

This equation represents the best-fitting plane in 3D space. The coefficients $c_0, c_1,$ and $c_2$ can be found using various methods such as the least squares method.

Keep in mind that this assumes a linear relationship between the variables. If your data suggests a more complex relationship, you may need to consider a higher-degree polynomial or other regression techniques.

---
## 3D quadratic fitting

For polynomial fitting with a maximum degree $n = 2$ for 3D data points $(x_i, y_i, z_i)$, the general form of the equation becomes:
$$ \begin{bmatrix} 1 & x_1 & y_1 & x_1^2 & x_1y_1 & y_1^2 \\ 1 & x_2 & y_2 & x_2^2 & x_2y_2 & y_2^2 \\ 1 & x_3 & y_3 & x_3^2 & x_3y_3 & y_3^2 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 1 & x_m & y_m & x_m^2 & x_my_m & y_m^2 \end{bmatrix} \begin{bmatrix} c_0 \\ c_1 \\ c_2 \\ c_3 \\ c_4 \\ c_5 \end{bmatrix} \approx \begin{bmatrix} z_1 \\ z_2 \\ z_3 \\ \vdots \\ z_m \end{bmatrix}$$

In this equation:
- The first column of the matrix on the left is a column of ones, representing the constant term.
- The second column corresponds to the x-coordinates.
- The third column corresponds to the y-coordinates.
- The fourth column represents the square of the x-coordinates ($x^2$).
- The fifth column represents the product of the x and y coordinates ($xy$).
- The sixth column represents the square of the y-coordinates ($y^2$).

The vector on the right represents the z-coordinates of your 3D data points.

The matrix multiplication will give you a set of equations:
$$ c_0 + c_1x_i + c_2y_i + c_3x_i^2 + c_4x_iy_i + c_5y_i^2 \approx z_i$$

You can use various methods, such as the least squares method, to determine the coefficients $c_0, c_1, c_2, c_3, c_4,$ and $c_5$ that best fit your data.


---

Multivariable polynomial fitting (combining polynomial + multi-dimension)

In the context of multivariable fitting, we extend the concept of polynomial fitting to accommodate multiple independent variables. Given a set of data points in the form $(\mathbf{x}_1, y_1), \dots, (\mathbf{x}_m, y_m)$, where each $\mathbf{x}_i$ is a vector in a multidimensional space, and $y_i$ represents the corresponding dependent variable, we seek a fitting function that captures the relationship between the input variables and the output.

Consider a polynomial of degree $n$ in multiple variables:
$$ p(\mathbf{x}) = c_0 + c_1x_1 + c_2x_2 + \dots + c_{n-1}x_1^{(n-1)} + \dots + c_{n-1}x_m^{(n-1)} + \dots + c_nx_1^n + \dots + c_nx_m^n$$

Our goal is to find the coefficients $c_0, c_1, \dots, c_n$ that minimize the difference between the predicted values of the function, $p(\mathbf{x}_i)$, and the actual observed values, $y_i$, for all data points.

This leads to the formulation of a system of equations:
$$ \begin{bmatrix} 1 & x_{1,1} & x_{2,1} & \dots & x_{m,1} & \dots & (x_{1,1})^n & \dots & (x_{m,1})^n \\ 1 & x_{1,2} & x_{2,2} & \dots & x_{m,2} & \dots & (x_{1,2})^n & \dots & (x_{m,2})^n \\ \vdots & \vdots & \vdots & \ddots & \vdots & \ddots & \vdots & \ddots & \vdots \\ 1 & x_{1,k} & x_{2,k} & \dots & x_{m,k} & \dots & (x_{1,k})^n & \dots & (x_{m,k})^n \end{bmatrix} \begin{bmatrix} c_0 \\ c_1 \\ c_2 \\ \vdots \\ c_n \end{bmatrix} \approx \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_m \end{bmatrix}$$

Here, each $x_{i,k}$ represents the $k$-th component of the $i$-th input vector. Solving this system yields the coefficients for the multivariable polynomial, allowing us to express the fitting function $p(\mathbf{x})$ that approximates the given dataset.




---


[[Least Squares]]
- We find $p(x)$ by minimizing the squares of the derivations, $\sum_{i=1}^m |p(x_i) - y_i|^2$
- 

