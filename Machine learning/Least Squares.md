
find $x \in \mathbb{C}^n$ such  that $||b - Ax||_2$ is minimized

**Introduction:**
Least squares is a fundamental concept in linear algebra that deals with the approximation of a set of data points using a linear equation. It is widely used in various fields including statistics, engineering, and computer science. The goal of the least squares method is to find the best-fitting linear equation that minimizes the sum of the squared differences between the observed and predicted values.

---
### 3 methods to solve least squares 

- 1. [[Normal equation]]
	- Please refer to that note for more info

- 2. [[Reduced QR decomposition|QR factorization]]
	- Please refer to that note for more info

- 3. [[Singular value decomposition|SVD]]
	- Please refer to that note for more info



---

## 3 representations of least squares

## Representation 1: Data regression representation

   - Mathematically, the problem can be formulated as minimizing the sum of squared differences:
$$ \sum_{i=1}^{n} (y_i - (ax_i + b))^2$$
- This expression is more often found in statistics book. 
- In this expression, $y_i$ represents the observed values in the dataset. $ax_i + b$ is the equation of the linear model you are trying to fit to the data, where $a$ is the slope, $b$ is the y-intercept, and $x_i$ is the independent variable. 

   - We minimize this term to find minimal of sum of squared difference. 
   - To solve this, calculus techniques are often used, setting partial derivatives with respect to 'a' and 'b' to zero to find the optimal coefficients.

**Minimizing Residuals:**
   - Given a set of data points (x₁, y₁), (x₂, y₂), ..., (xₙ, yₙ), where yᵢ is the observed value and xᵢ is the independent variable, the least squares method aims to find coefficients (a and b) for the linear equation y = ax + b that minimizes the sum of squared residuals.
   - Residuals are the differences between the observed yᵢ and the corresponding predicted values (axᵢ + b). Minimizing these squared residuals ensures a "best-fit" line.


---
## Representation 2 - See [[Data fitting]]

In the context of linear regression, the least squares problem can be described as finding a vector $x \in \mathbb{C}^n$ such that the residual vector $||b - Ax||_2$ is minimized. Here, $A \in \mathbb{C}^{m \times n}$ is a design matrix that represents the relationships between the input variables and the parameters of the model, and $b \in \mathbb{C}^m$ is the observed output vector.

The problem can be represented in matrix form as:

$$ \mathbf{y} = \mathbf{X} \mathbf{b} + \mathbf{e}$$

where $\mathbf{y}$ is the vector of observed values, $\mathbf{X}$ is the matrix of independent variables, $\mathbf{b}$ is the vector of coefficients to be determined, and $\mathbf{e}$ is the error vector. The solution for $\mathbf{b}$ is given by the following [[Normal equation]]:

$$\mathbf{b} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$

This formulation is equivalent to $Ax = b$ with $A = \mathbf{X}$, $x = \mathbf{b}$, and $b = \mathbf{y}$.


---
## Example use case of representation 2: 


For example, consider linear 2D fitting with data points $(1,2), (6,8), (7,5)$. The matrix $Ax = b$ becomes:

$$\begin{bmatrix}1 & 1 \\ 1 & 6 \\ 1 & 7\end{bmatrix} \begin{bmatrix}b \\ m\end{bmatrix} = \begin{bmatrix}2 \\ 8 \\ 5\end{bmatrix}$$

Here, $x \in \mathbb{C}^n$ with $n =2$, and $b \in \mathbb{C}^m$ with $m = 3$.

Applying Singular Value Decomposition (SVD) to the matrix $A$ transforms the problem:

1. The optimal solution of the least squares approximation is given by: $\frac{\partial}{\partial y} \| \Sigma y - U^T b \|_2^2 = 2 \Sigma^T (\Sigma y - U^T b)$
2. For SVD regression, the line would be: $x = V \Sigma^{-1} U^T b$

Thus, these representations express the same concept in different mathematical notations and formalisms, providing a comprehensive view of how least squares problems can be formulated and solved.



---

### Representation 3: Linear Regression with Singular Value Decomposition (SVD)

Given the Singular Value Decomposition (SVD) of matrix $A$: $A = U \Sigma V^T$, where:

- $A$ is the input data matrix,
- $U$ is the left singular matrix,
- $\Sigma$ is a diagonal matrix containing the singular values,
- $V^T$ is the transpose of the right singular matrix.

We aim to solve the linear regression problem, formulated as finding coefficients $\mathbf{x}$ that minimize the residual sum of squares: $\underset{x}{\text{argmin}} \, \| A\mathbf{x} - \mathbf{b} \|_2^2$, where $Ax$ represents the predicted values and $\mathbf{b}$ represents the observed values.

To obtain $x$, we can use the following [[normal equation]]: $x = V \Sigma^{-1} U^T b$

---
## Derivation for representation 3 

This problem can be expanded as follows: 

$\| A\mathbf{x} - \mathbf{b} \|_2^2 = (A\mathbf{x} - \mathbf{b})^T (A\mathbf{x} - \mathbf{b})$

Substitute $A = U \Sigma V^T$ into the equation:

$\| U \Sigma V^T \mathbf{x} - \mathbf{b} \|_2^2 = (U \Sigma V^T \mathbf{x} - \mathbf{b})^T (U \Sigma V^T \mathbf{x} - \mathbf{b})$

Given that $U$ and $V^T$ are orthogonal matrices, they do not change the Euclidean norm. This allows us to simplify the equation to:

$\| \Sigma V^T \mathbf{x} - U^T \mathbf{b} \|_2^2 = (\Sigma V^T \mathbf{x} - U^T \mathbf{b})^T (\Sigma V^T \mathbf{x} - U^T \mathbf{b})$

Introduce $\mathbf{y} = V^T \mathbf{x}$ to transform the problem into $\underset{y}{\text{argmin}} \| \Sigma \mathbf{y} - U^T \mathbf{b} \|_2^2$:

$\| \Sigma \mathbf{y} - U^T \mathbf{b} \|_2^2 = (\Sigma \mathbf{y} - U^T \mathbf{b})^T (\Sigma \mathbf{y} - U^T \mathbf{b})$

In expanded form, we aim to minimize:

$\underset{y}{\text{argmin}} \, \sum_{i=1}^{n} (\sigma_i y_i - u_i^T \mathbf{b})^2$

where $\sigma_i$ are the singular values, and $u_i$ are the columns of $U$.

To solve this problem, we find the derivative of $\| \Sigma \mathbf{y} - U^T \mathbf{b} \|_2^2$ with respect to $\mathbf{y}$ and set it to zero. The gradient of this function is:

$\frac{\partial}{\partial y} \| \Sigma y - U^T b \|_2^2 = 2 \Sigma^T (\Sigma y - U^T b)$

Setting this to zero provides:

$\Sigma^T (\Sigma y - U^T b) = 0$

Multiplying through by $\Sigma^{-T}$ (as $\Sigma$ is a diagonal matrix, $\Sigma^T = \Sigma$ and $\Sigma^{-T} = \Sigma^{-1}$), we get:

$\Sigma y - U^T b = 0$

Solving for $y$ yields:

$y = \Sigma^{-1} U^T b$

Recall we defined $y = V^T x$, so we can substitute this back to obtain $x$:

$x = V \Sigma^{-1} U^T b$

The coefficients $\mathbf{x}$ that minimize the residual sum of squares in the original linear regression problem are given by this formula. This assumes full rank of $A$ (so that $\Sigma^{-1}$ exists). In practice, SVD is often used to calculate the pseudoinverse of $A$ for linear regression, which handles the case where $A$ is not full rank.

This derivation shows how the least squares solution in linear regression can be derived using SVD. The formula $\tilde{x} = V^T \left( \Sigma^{-1} \right) U^T \mathbf{b}$ represents the optimal coefficients for the regression line.