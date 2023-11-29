---
category: []
alias: []
tags :[]
---

- 24-10-2022 19:27: created

- subset:
	- [[Euclidean norm]]
	- [[Euclidean distance]]
	- Manhattan norm

- Related:
	- [[Induced matrix norm]]
---


- What is Norm?
	- a norm is a mathematical function $|| \cdot ||: \mathbb{C}^m \rightarrow \mathbb{R}$ used to measure the "size"/real-valued length to a vector. 
	- It provides a way to quantify the distance of a vector from the origin (0,0) in an n-dimensional space. Norms are fundamental in various areas of mathematics and have wide-ranging applications in fields such as physics, engineering, and computer science.

- Properties of vector norms: 
	- To prove something is a vector norm, there are 3 properties to follow: 
		- Non-negativity
			- $||x|| \geq 0$, and $f(x)=0 \Rightarrow x=0$
		- Triangular inequality
			- $f(x+y) \leq f(x)+f(y)$ (Triangle inequality)
		- Scalar multiplication
			- $\forall \alpha \in R, f(\alpha x)=|\alpha|f(x)$ (Linearity)


- Types of norms:
	- p-norm
		- $||x||_p = (\sum_{i=1}^n |x_i|^p)^{1/p}$
	- L0 norm
		- For $p = 0$, the p-norm formula becomes $||x||_0 = (\sum_{i=1}^n |x_i|^0)^{1/0}$. 
			- the outermost power 1/0 represents an operation that is not well-defined in standard mathematics.
		- The correct definition of the L0 norm is: $||x||_0 = \sum_{i=1}^n |x_i|^0$
		- It simplifies to count the number of non-zero elements in the nonzero elements in the vector $x$. 
	- Manhattan norm (L1 norm)
	- Euclidean norm (L2 norm)
		- $||v||_2$ = $\sqrt{\sum{v_i^2}}$ , for $i = 1$ to $n$
		- It measure vector $v$ in n-dimensional space
		- It is familiar because it corresponds to the length of a vector in Cartesian coordinates. 
	- Infinity norm (L $\infty$ norm)
	- Frobenius norm
		- $||A||_F = \sqrt{\sum|a_{ij}|^2}$
		-  Say we have a matrix $A$, Euclidean norm is defined as the square root of the sum of the absolute squares of its elements: $$||A_F||=\sqrt{\sum_{i=1}^m \sum_{j=1}^n|a_{ij}|^2}$$
		- The difference between Frobenius norm and Euclidean norm is, the former one is counting the element of a matrix, the latter one is counting the elements of vectors. 

---
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
		- Collinearity handling (which means handling highly correlated features)
		- Unique solution

Figure: solving L1/L2 norm minimization problem, subject to $Ax - b$. We can see the distribution of the values obtained from L1 norm minimization is much sparse. Which means more entries the value are close to zero. 
- The plot could be found on `BigDataMath` package. 
![[Pasted image 20231106233848.png]]

---

- Q: why there are so many norms?
	- A: Different norms correspond to different geometric interpretations of what it means for a vector to have a "size" or "length."
		- Discuss on application o each norm
		- Euclidean norm corresponds to the usual notion of distance in Euclidean space
			- linear regression, vector spaces, and signal processing.
			- Geometric interpretation:
				- It corresponds to the Euclidean distance between vectors and encourages all components to be balanced.
		- Manhattan norm corresponds to distance traveled along gridlines.
			- Commonly used in optimization problems and machine learning for feature selection and sparsity-inducing regularization.
			- Geometric interpretation:
				- It corresponds to the "city block" distance and encourages sparsity in solutions.
		- [[Frobenius norm]]:


- How to find norm?
	- Geometrically
		- We draw the norm geometrically, and then enlarge the shape from the origin until it hits the vector, or a list of vectors inside the vector / induced matrix norm. 
	- Analytical calculation
		- Using the function in the definition of norms. 
	- Optimization techniques
		- L1 and L2 regularization, involving finding norms of vectors that optimize specific objectives. 
	- Norm inequalities
		- There are several inequalities related to norms, such as the Triangle Inequality and Hölder's Inequality. These inequalities provide useful relationships between different norms and can be used to calculate or estimate norms in certain situations.

---

- "Norm" in mathematics:
	- We can define many functions satisfies these conditions.
		- Vector norms:
			- A norm $|| \cdot || : C^m \rightarrow R$ is a function satisfying:
				- $||x|| \geq 0$ and $||x|| = 0$, if and only if $x = 0$.
				- $|| \alpha x || = |\alpha| ||x||$ for all $\alpha \in \mathbb{C}$. 
				- $|| x + y || \leq ||x|| + ||y||$ (triangle inequality)
			- Euclidean norm: 
				- [[dot product]]: $x \cdot x$
				- $||v||_p= \sqrt{x \cdot x} = (|v_1|^2+|v_2|^2+\dots+|v_n|^2)^{1 \over 2}$
			- 1-norm: $||v||_1=|v_1|+|v_2|+\dots+|v_n|$
			- p-norm: 
				- For $1 \leq p \leq \infty$, p-norm is defined as 
					- $||x||_p = ( \sum_{i=1}^m |x_i|^p)^{1/p}$
				- For $p = \infty$, the $\infty$-norm is defined as:
					- $||x||_p = (\underset{a \leq i \leq m}{max} |x_i|)$
				- Property: for $1 \leq p \leq q \leq \infty$, it holds for any $x \in C^m$, $||x||_\infty \leq ||x||_q \leq ||x||_p \leq ||x||_1 \leq m||x||_\infty$, meaning all p-norms are equivalent. 
			- infinite-norm: $||v||_\infty=max(|v_1|,|v_2|,\dots,|v_n|)$


	- Application
		- 1. Calculate the "size" of a vector. 
		- 2. Calculate the distance between two tensors.
		- 3. Error measurement:
			- In numerical analysis, norms are used to quantify the error between approximate and exact solutions.
		- 4. Machine learning: 
			- Regularization techniques in machine learning, such as L1 and L2 regularization, rely on norms to penalize large parameter values.
		- 5. Signal processing:
			- In signal processing, norms are used to measure the magnitude of signals and filter coefficients.
		- 6. Geometry:
			- Norms are fundamental in geometry for defining distances between points and lengths of vectors.
	- In machine learning, everything are represented as vectors. Such as feature $X=\{X_1, X_2\}$, we can represent it to be $a = \begin{bmatrix}x_1\\x_2\end{bmatrix}$


---
## Reference

1. [[(Course) NLP  Natural Language Processing with Classification and Vector Spaces]]