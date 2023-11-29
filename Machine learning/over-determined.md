---
alias: overdetermined
---

- related:
	- [[Under-determined|Underdetermined]]
	- [[regularization]]

In an over-determined system, we have more number of equations than the number of variables.

To define our Ax = b, we have to take care about the dimensions of each objects.
- dim(A): n \times m
- dim(x): m \times p
	- Row: The number of rows of $x$ ($m$) should match the number of columns of $A$ ($m$) ensuring $Ax$ is valid. 
	- Column: The number of column of $x$ ($p$) can be greater than $1$ if we are solving a system with multiple sets of variables. 
- dim(b): n \times p
	- It is determined by the dimension of $A$ and $x$. Nothing special here. 

![[Pasted image 20231107022834.png|300]]

---

- Definition:
	- ( ~ fat and short matrices)
	- For matrix $A$ where $m > n$, we say $Ax = b$ is an over-determined system. 
		- The property of under-determined system manifested in the fact that:
			- $dim(Domain(A)) = dim(C(A^T)) = n$. So that the dimension of input data from $A$ should be $n$. 
			- $dim(Range(A)) = dim(C(A)) = m$. So that the dimension of output data from $A$ should be $m$.  
			- In short, $A$ maps input data that has less dimension ($m$) into a space that has higher dimension ($n$). 

- Property
	- 1. Without regularization, minimizing the residual error on the training data does not give us a good solution to the actual problem. 
		- It is because the model was overfitting the training data, i.e. it was too tailored to the specific noise and patterns in the training data and does not generalize well to new data. S
		- Overdetermined linear systems refer to systems where the number of equations exceeds the number of unknowns. In such cases, it's common to find "no exact solution" that satisfies all the equations. 
		- To address this, we minimize the residual error between the left and right sides of the equations using techniques like least squares.
		- The regularization technique is often added to the problem to avoid solutions with excessively large unknowns and to prevent overfitting. The regularized problem is defined as: $\underset{x}{argmin} ||Ax - b||_2 + \lambda_1 ||x||_2 + \lambda_2 ||x||_1$.
			- The first term $\underset{x}{min} ||Ax - b||_2$ attempts to find a solution that minimizes the residual error, providing as small a solution as possible.
			- The L2 [[regularization]] term, $\lambda_1 ||x||_2$, makes the values of unknowns small and spread out, resulting in a dense solution.
			- The L1 regularization term, $\lambda_2 ||x||_1$, encourages the values of unknowns to be small but also sparse, leading to a solution where many unknowns will have a value of zero. This property is useful for feature selection in high-dimensional problems.
			- $\lambda_1$ and $\lambda_2$ are hyperparameters that control the amount of regularization. Setting these values is a delicate balance, and is typically determined through a process called hyperparameter tuning.
		- There are a variety of solvers to address these regularized problems, including analytical methods, gradient-based optimization methods, and coordinate descent methods.
		- The concept of sparsity is related to L1 regularization. A sparse solution is one in which many of the coefficients are zero. This leads to simpler and more interpretable models.
- 
	- Example:
		- House price
			- Problem of overfitting
				- Predict house price based on various features, such as rooms, footage square, age of the house, location etc. 
				- You set up a linear regression model to predict the house prices. 
				- If the number of features (predictors) is very large and especially when it is close to or exceed the number of observations, the linear regression can perfectly fit the training data, resulting in very low residual error on the training data. 
				- However, when you try to use this model to predict the prices of new jouses (test data), the performance is often poor, i.e. too tailored to the specific noise and patterns in the training data and does not generalize well to new data. 
			- Reducing overfit
				- By adding a regularization term to the problem, we can control the complexity of the model, preventing it from fitting the noise in the training data and helping it to generalize better to new data. 
				-  The regularization term does this by penalizing large coefficients in the model, effectively reducing the number of features the model relies on, making the model simpler and more robust to noise.
	- Example 2: [[linear regression]]
	- Example 3: Calibration problem
		- See the 
---

**Key Points:**

1. **System of Linear Equations:** A system of linear equations consists of multiple equations, each representing a linear relationship between variables. The general form of a linear equation is often written as:
	- $a₁x₁ + a₂x₂ + ... + aₙxₙ = b$
	- Here, `a₁, a₂, ..., aₙ` are coefficients, `x₁, x₂, ..., xₙ` are unknown variables, and `b` is a constant.

2. **Over-Determined System:** 
	- An over-determined system occurs when there are more equations in the system than there are unknown variables (`n` equations with `n` unknowns is a properly determined system). 
	- In mathematical terms, if `m > n`, where `m` is the number of equations and `n` is the number of unknowns, then the system is over-determined.

3. **No Exact Solution:** Over-determined systems often do not have an exact solution. This is because the extra equations introduce redundancy or conflicting information into the system, making it impossible to find a set of values for the unknown variables that satisfy all equations simultaneously.

4. **[[Least Squares]] Solution:** To address the lack of an exact solution in over-determined systems, one common approach is to seek a "least squares" solution. The least squares solution minimizes the sum of the squares of the differences between the left-hand sides of the equations and the right-hand sides. This method is widely used in regression analysis and data fitting.

5. **Applications:** Over-determined systems are prevalent in real-world applications. For example, in data analysis, you might have more data points (equations) than model parameters (unknowns). In such cases, you can use least squares regression to find the best-fitting line or curve.

6. **Matrix Formulation:** Over-determined systems are often expressed in matrix form using the coefficient matrix `A`, the vector of unknowns `x`, and the vector of constants `b`. The least squares solution can be obtained using techniques like the Moore-Penrose pseudoinverse.
