12/11/2023

Normal equation is a concept that closely related to [[Data fitting]] and [[Least Squares]].

See 3 normal equation expression in [[Least Squares]]

Normal equation is defined as: $\theta = (X^TX)^{-1}X^Ty$
- where $\theta$ is the vector of coefficients of the linear model
- $X$ is the matrix of input features (with an added column of 1s for the intercept term)
- $y$ is the vector of output values (the target variable)

- Consider a linear system of equations having $n$ unknowns but $m > n$ equations. We wish to find a vector $x \in \mathbb{C}^n$ that satisfies $Ax = b$, where $A \in \mathbb{C}^{m \times n}$ and $b \in \mathbb{C}^m$. 

---
- find [[Least Squares]] from normal equation:

**Objective:**
The objective of the Normal Equation is to find the values of $x$ that minimize the sum of squared residuals. 

Mathematically, residual norm can be expressed as:
$$ r = b - Ax$$
A vector $x \in \mathbf{C}^n$ minimize the residual norm $||r||_2 = || b - Ax||_2$ (least squares problem) if and only if $r \perp range(A)$, that is $A^* r = 0$. 

When $A^* r = 0$, it implies that $r$ is in the null space (also known as [[Kernel space|kernel]]) of $A^*$, meaning that $r$ is orthogonal to the range of $A$. 

The solution is obtained by setting the derivative of the sum of squared [[residual vector , error]] with respect to $x$ to zero. 

Or, we can just substituting $r =  b - Ax$ into $A^* r = 0$. Then we have $A^*(b - Ax) = 0$. This leads to the Normal Equation:
$$ A^*(Ax) = A^*b$$
How to solve this, anyways?
just flip the factor matrix to the right hand side of the equation, then we have: 
$x = (A^TA)^{-1} A^T b$



---

- Q: Why solving $A^* Ax = A^* b$ could lead to minimal residual error vector, or least squares?

To understand why solving the normal equation leads to the minimum residual error vector, or least squares solution, let's break it down.

Consider a system of linear equations, $Ax = b$. In many situations, this system has no exact solution. This happens when $b$ does not lie exactly on the subspace spanned by the columns of $A$. In these cases, we aim to find an $x$ that minimizes the residual error vector, $r = b - Ax$.

The residual error is the difference between the actual output and the predicted output. We aim to minimize the _squared magnitude_ of this error, which is $r^Tr = (b - Ax)^T(b - Ax)$. This is where the 'least squares' comes from; we're minimizing the sum of squares of the residuals.

When you differentiate this expression with respect to $x$ and set it to zero to find the minimum, you get the normal equation:

$$ 2A^T(Ax - b) = 0$$

Which simplifies to:

$$ A^TAx = A^Tb$$

This equation, when solved, gives the value of $x$ that minimizes the sum of squared residuals, hence the term 'least squares solution'. This is why solving the normal equation leads to the least squares solution.

- Limitation of this method:
	- This solution is exact when $A$ is a square matrix and its columns are linearly independent (i.e.,  is full rank). If  is not square or its columns are linearly dependent, the normal equation may not have a unique solution.
	- This method is not [[Stability|stable]] in the presence of rounding errors. 

---

- Q: how do we determine an $r$ is "small"?

Here are a few common ways to assess the "size" or "smallness" of the residuals:

1. **Sum of Squared Residuals (SSR):**
   - One common measure is the sum of squared residuals, which is given by:
$$ SSR = \sum_{i=1}^{n} r_i^2$$
   - A smaller SSR indicates a better fit, as it means that the predicted values are closer to the observed values.

2. **Root Mean Squared Error (RMSE):**
   - RMSE is another popular metric that takes the square root of the mean of the squared residuals:
$$ RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n} r_i^2}$$
   - RMSE provides a measure of the average magnitude of the residuals.

3. **Mean Absolute Error (MAE):**
   - MAE is the mean of the absolute values of the residuals:
$$ MAE = \frac{1}{n}\sum_{i=1}^{n} |r_i|$$
   - MAE is less sensitive to outliers compared to RMSE.

4. **Coefficient of Determination ($R^2$):**
   - $R^2$ is a measure that indicates the proportion of the variance in the dependent variable that is predictable from the independent variables. It ranges from 0 to 1, and a higher $R^2$ suggests a better fit.

In general, the choice of the metric depends on the specific goals and requirements of the analysis. Researchers and practitioners often consider a combination of these metrics and assess them in the context of the problem being addressed. It's important to note that what is considered "small" can vary based on the domain and the nature of the data.

---

![[Pasted image 20231112224039.png]]