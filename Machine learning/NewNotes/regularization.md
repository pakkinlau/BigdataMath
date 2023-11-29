---
category:
alias:
tags:
---

- related:
	- [[Norm]]

[[Norm]] and regularization is different thing. We can show that by seeing their expressions.
- Norm:
	- In the problem of "finding vector $x$ that minimize the L1-norm of the residual vector $Ax - b$" , we have $\underset{x}{argmin} \, \|Ax - b\|_1$. (Refer to: [[Manhattan norm]])
- Regularization: 
	- $\underset{x}{argmin} \, \left( \|Ax - b\|_2^2 + \lambda \|x\|_1 \right)$

- subset
	- [[Ridge (L2 regularization)]]
	- [[Lasso (L1 regularization)]]

- In linear algebra, it is related to [[over-determined|overdetermined]] system.

Regularization is a fundamental technique in the field of linear algebra, primarily used in the context of solving linear systems of equations and performing various types of data analysis. It plays a crucial role in addressing issues like overfitting in machine learning, stabilizing ill-conditioned matrices, and promoting numerical stability in various computational tasks involving linear algebra.


- Figure: 
	- Adding a regularization can lead to simpler hypothesis, and less prone to overfitting. 
![[Pasted image 20231105023512.png]]
![[Pasted image 20231105023824.png]]
![[Pasted image 20231105023814.png]]

---

**1. Introduction to Regularization:**

   - Regularization is a mathematical approach that aims to prevent overfitting or instability in linear algebra problems. It involves adding a penalty term to the optimization objective or modifying the linear system to make it more well-behaved.

**2. Types of Regularization:**

- [[Lasso (L1 regularization)]]
- [[Ridge (L2 regularization)]]

---
## Revising the preference for L1 / L2 norms

- When we prefer L1 norm / L2 norm
	- When we talk about minimizing L1/L2 norms, it usually refers to solving an optimization problem where the objective function includes the L1 norm of a vector. 
	- Minimizing L1 norm
		- Sparse solution
		- Feature selection
		- Robustness to outliners
		- Computationally efficient
	- Minimizing L2 norm
		- No specific preference for sparsity
		- Data fitting
		- Collinearity handling
		- Unique solution

The preference of L1 (Lasso) / L2 (Ridge) regularization 
- The choice between L1 or L2 in regularization is very close to the choice between L1 and L2 norm minimization. 
	- Lasso
		- Sparse model
		- Interpretable models
	- Ridge
		- Multicolinearity
		- No prior knowledge of sparsity
		- Numerical stability
		- Unique solution 

---

**3. Applications in Linear Systems:**

   - Regularization is often applied when solving systems of linear equations, especially when the coefficient matrix is ill-conditioned (i.e., it has a high condition number). Ill-conditioned matrices can lead to numerical instability, and regularization can mitigate this issue.

**4. Machine Learning and Regularization:**

   - In machine learning, linear algebra is used extensively in algorithms like linear regression and logistic regression. Regularization is applied to these algorithms to prevent overfitting and improve the generalization of the model.

**5. Regularization Parameter:**

   - Regularization strength is controlled by a hyperparameter often denoted as λ (lambda). Tuning this parameter allows practitioners to balance the trade-off between fitting the training data well and preventing overfitting.

**6. Benefits of Regularization:**

   - Regularization techniques help achieve more robust and stable solutions, reducing the sensitivity of linear algebra computations to small changes in input data.

**7. Challenges and Considerations:**

   - The choice of the regularization method (L1 or L2) and the regularization strength should be made carefully, as they impact the final solution.

   - Regularization may introduce bias into the estimation, so it's essential to strike a balance between bias and variance.

In summary, regularization is a crucial concept in linear algebra, especially when dealing with ill-conditioned matrices or machine learning problems. It serves as a powerful tool to enhance the stability and generalization ability of models and solutions in various computational applications. Understanding the principles and techniques of regularization is fundamental for anyone working with linear algebra in practical data analysis or machine learning scenarios.


---
### regularization in machine learning

- Reason:
	- 1. Simplicity
	- 2. Sparsity
		- eg: [[feature crosses]]
			- eg: one of our feature is the words in a search query, one other feature might be unique video we have to look up.
			- we could have millions of possible words, and millions of possible videos -->  we are crossing those, -->  we are going to get a lot of coefficients.
			- A lot of those combinations are going to be super rare. So we just end up with some noisy coefficieints and possibly overfitting. 

![[Pasted image 20221023225809.png|400x200]]
- Fig: R1

---
## L1 regularization 


---
## L2 regularization

---
## Reference

1. [[(Course) google developers - machine learning courses]]