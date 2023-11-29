**Concept: Gradient of Rayleigh Quotient**
**Context: Linear Algebra**


- Rayleigh quotient is a fundamental concept used to approximate eigenvalues of a matrix. 

---

Setting:

Say we have Hermitian matrix $A \in \mathbb{m \times m}$ 
- We have a set of eigenvalues: $\lambda_1, \lambda_2, \dots, \lambda_m$ are real and distinct
- We have a set of orthonormal basis $q_1, q_2, \dots, q_m$ 

---


Definition 
- Assume we are given a real symmetric matrix $A$ and a non-zero vector $x$, then Rayleigh quotient of a non-zero vector $x \in \mathbb{R}^m$ is defined as:
- $R(x) = \frac{x^T A x}{x^T x}$
	- where the numerator is sort of like "quadratic" in $x$ on the top
	- where the $x^Tx$ is just the norm of $x$. [[dot product|inner product]]
	- where $x \in \mathbb{R}^{m \times 1}$

- Say we plugs in $x = q_j$ into Rayleigh quotient, then
	- $r(q_j) = \frac{q_j^T A q_j}{q_j^T q_j} = \lambda_j \frac{q_j^T q_j}{q_j^T q_j} = \lambda_j$
		- We used $Aq_j = \lambda_j q_j$ in the process. 
	- From this, we can see Rayleigh quotient is a function that when we put int every eigenvectors of $A$, it produces the corresponding eigenvalue. 

Significance:
- Rayleigh quotient is significant because for any unit eigenvector $x$ corresponding to the eigenvalue $\lambda$, $R(x)$ equals $\lambda$. This property forms the basis for eigenvalue approximation methods.

----

- What happens if we but any $x$ (in general not eigenvector), what scalar $\alpha$ is act most like a $\lambda_j$.
- $\underset{\alpha}{min} ||Ax - \alpha x ||_2 \rightarrow Ax \approx \alpha x$. 

- How can we minimize? taking derivative. 

---

*Gradient of Rayleigh Quotient:*
The gradient of the Rayleigh quotient with respect to vector $x$ provides valuable information about the rate of change of the Rayleigh quotient concerning perturbations in the vector space. The gradient vector $\nabla R(x)$ is calculated as follows:
- $R(x) = \frac{x^T A x}{x^T x}$
- $\frac{\partial}{\partial x_j} r(x)$ = $\frac{\frac{\partial}{\partial x_j}(x^TAx)}{x^Tx} - \frac{(x^TAx)\frac{\partial}{\partial x_j}(x^TAx)}{(x^Tx)^2}$
- $\nabla R(x) = \frac{2(Ax - R(x)x)}{x^Tx}$
- In this, $r(x) = \alpha$, how to pick $\alpha$ to make $\nabla r(x)$ as small as possible. 

where quotient rule of calculus was:
- $\frac{d}{dx} \left( \frac{u}{v} \right) = \frac{v \cdot \frac{du}{dx} - u \cdot \frac{dv}{dx}}{v^2}$

The way of computing this is [[Power iteration]].

---

*Significance of Gradient:*
1. **Eigenvalue Approximation:** By analyzing the gradient, iterative methods can be designed to approximate the dominant eigenpair of a matrix.
2. **Optimization:** In optimization problems involving symmetric matrices, the gradient of the Rayleigh quotient is utilized in algorithms for constrained optimization.

*Applications:*
1. **Quantum Mechanics:** In quantum mechanics, the Rayleigh quotient and its gradient are used in computational methods for approximating molecular electronic structures.
2. **Structural Engineering:** Eigenvalues and the Rayleigh quotient find applications in the analysis of structural systems, especially in understanding natural frequencies and mode shapes.
3. **Machine Learning:** Principal Component Analysis (PCA) involves eigenvalues and eigenvectors, making the Rayleigh quotient and its gradient relevant in certain machine learning algorithms.

*Conclusion:*
Understanding the Rayleigh quotient and its gradient is crucial for a broad spectrum of applications in linear algebra, optimization, and various scientific disciplines. It provides powerful tools for solving problems related to eigenvalues and eigenvectors, making it an indispensable concept in the field of mathematics and its applications.

---

## Gradient of Rayleigh Quotient

The Rayleigh quotient and its gradient are often discussed together because the gradient of the Rayleigh quotient plays a crucial role in optimization problems. When you're dealing with optimization tasks, especially in the context of eigenvalue problems or problems involving symmetric matrices, you're often interested in finding the minimum or maximum values of the Rayleigh quotient. The gradient provides information about the rate of change of the Rayleigh quotient concerning changes in the input vector \(x\). Understanding this gradient is essential for iterative optimization algorithms like gradient descent, which are widely used in numerical optimization.

Here's why the gradient of the Rayleigh quotient is important:

1. **Optimization:** In optimization problems, you seek to find the values of \(x\) that minimize or maximize the Rayleigh quotient. The gradient (which is essentially the derivative in this context) points in the direction of the steepest ascent. Therefore, moving in the opposite direction of the gradient allows you to iteratively approach the optimal solution.

2. **Eigenvalue Problems:** For a symmetric matrix \(A\), the stationary points of the Rayleigh quotient correspond to the eigenvectors of \(A\). The gradient at these points is zero, indicating that the rate of change of the Rayleigh quotient is flat. This property is fundamental to algorithms used for finding eigenvalues and eigenvectors.

3. **Numerical Methods:** Numerical algorithms for finding eigenvalues often rely on iterative techniques. By understanding the gradient of the Rayleigh quotient, these methods can converge more quickly and accurately to the desired eigenvalues and eigenvectors.

4. **Symmetric Matrices:** In the context of symmetric matrices, the Rayleigh quotient provides a powerful way to approximate eigenvalues. The gradient information aids in devising efficient algorithms for eigenvalue decomposition, which is crucial in various scientific and engineering applications.

In summary, the gradient of the Rayleigh quotient is intimately connected to optimization strategies and numerical methods for solving eigenvalue problems. It provides essential information about the direction in which to adjust the input vector \(x\) to improve or optimize the Rayleigh quotient. Hence, it is frequently discussed alongside the Rayleigh quotient, especially in the context of practical applications and numerical computations.