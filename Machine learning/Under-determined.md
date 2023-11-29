---
alias: Underdetermined
---

- Related: 
	- [[over-determined]]


- Definition:
	- ( ~ fat and short matrices)
	- For matrix $A$ where $m < n$, we say $Ax = b$ is an under-determined system. 
		- The property of under-determined system manifested in the fact that:
			- $dim(Domain(A)) = dim(C(A^T)) = n$. So that the dimension of input data from $A$ should be $n$. (Recall: [[row space]])
			- $dim(Range(A)) = dim(C(A)) = m$. So that the dimension of output data from $A$ should be $m$.  (Recall: [[column space]])
			- In short, $A$ maps input data that has less dimension ($m$) into a space that has higher dimension ($n$). 

- Property
	- In the context of an underdetermined system, where we have more unknowns than equations, we often represent the problem as an optimization problem.
		- We seek to solve $\underset{x}{argmin} ||x||_2$ subject to $Ax = b$.
		- This can be interpreted as finding the solution 'x' that not only satisfies the equation $Ax = b$, but also has the smallest 2-norm, or in other words, the smallest Euclidean distance from the origin.
		- The optimization term, $\underset{x}{argmin} ||x||_2$, serves as an additional constraint allowing us to select a unique solution from an infinite pool of potential solutions that satisfy $Ax = b$.
		- Without this constraint, the problem would be ill-posed, indicating that solutions could be non-unique, non-existent, or not continuously dependent on the data.
	- This approach to solving underdetermined systems has practical implications, especially in fields like signal processing and statistics. The solution provided by this optimization problem not only satisfies the original system, but also minimizes the 'energy' of the solution, as the L2 norm corresponds to the energy of the signal.

- Example of imposing constraints is important
	- CT scanner acquires X-ray images of a patient from many angles.
	- Each image provides a sort of "projection" of the patient's body
	- Without imposing some kind of regularization, such as minimizing the L2 norm, the problem is ill-posed -- there are many different 3D images that could have produced the same set of 2D x-ray images. 


**Key Characteristics:**
1. **Insufficient Equations:** In an under-determined system, you have fewer equations than unknowns. Mathematically, if you have 'm' equations (m < n) involving 'n' unknown variables, the system is under-determined.

2. **Infinite Solutions:** Because there are not enough equations to uniquely determine the values of all the variables, under-determined systems typically have infinitely many possible solutions. This makes them quite different from over-determined systems, which often have either no solution or a unique solution.

**Applications:**
1. **Signal Processing:** In signal processing, under-determined systems can arise when you have more sensor measurements than independent parameters to estimate. Solving these systems is essential for applications like source separation, where you want to isolate individual signals from a mixture.

2. **Machine Learning:** Under-determined systems are common in machine learning, especially in feature selection and regression problems. For example, in linear regression, if you have more predictors (features) than observations (data points), you're dealing with an under-determined problem.

3. **Optimization:** Many optimization problems involve under-determined systems, particularly in cases where you seek to minimize or maximize a function subject to constraints. Linear programming, for instance, can involve under-determined systems when there are more decision variables than equations defining the problem.

**Solving Under-determined Systems:**
1. **[[Least Squares]]:** One common approach to solving under-determined systems is to use the method of least squares. This method finds the solution that minimizes the sum of the squared differences between the left-hand side (LHS) and right-hand side (RHS) of the equations.

2. **[[Regularization]]:** In machine learning, regularization techniques like [[Lasso (L1 regularization)]] and [[Ridge (L2 regularization)]] are used to handle under-determined systems by adding penalty terms to the [[objective]] function, encouraging sparsity or stability in the solution.
