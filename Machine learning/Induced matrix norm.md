
- the meaning of "induced"
	- The term "induced" refers to a particular way of defining a norm for matrices based on vector norms.

- Induced matrix norms:
	- The most common way of defining a matrix norm, is to relate the norm of a matrix to the norms of vectors. 
	- Another common choice is the induced matrix norms:
		- Let $|| \cdot ||_{(n)}$ and $|| \cdot ||_{(m)}$ be norms on the domain of $A \in C^n$ and range of $A \in C^m$. 
		- The induced matrix norm $||A||_{(m,n)}$ is the smallest number $C$ such that the following holds:  
			- $||Ax||_{(m)} \leq C||x||_{(n)}$, for all $x \in \mathbb{C}^n$, where $C$ is our induced matrix norm. 
			- Then $||A||_{(m,n)} = C \geq \frac{||Ax||_{(m)}}{||x||_{(n)}}$
			- In the context of defining matrix, norms, the goal is to find a constant $C$ that provides a meaningful bound for the transformation induced by the matrix $A$. By finding the smallest $C$, you are essentially determining the tightest bound that hods for all vectors in the domain space. 
			- In other words, $||A||_{(m,n)}$ is the supremum of the ratios $\frac{||Ax||_{(m)}}{||x||_{(n)}}$
		- Equivalently, $$||A||_{(m,n)} = \underset{x \in C^n , x \neq 0}{sup} \frac{||Ax||_{m}}{||x||_{(n)}} = \underset{x \in C^n, ||x||_{(n)}=1}{sup} ||Ax||_{(m)}$$
			- where we have chosen unit vectors ($||x||_n = 1$) in the last expression, simplifies the expression. By setting $||x||_n$ to 1 focuses on finding the supremum of the transformed vector's norm over all unit vectors in the domain space. 
		- How to execute this equation?
			- We draw the norm geometrically, and then enlarge the shape from the origin until it hits the vector, or a list of vectors inside the vector / induced matrix norm. 

- Properties of general matrix norm
	- In general, a matrix norm must satisfy the following conditions:
		- $||A|| \geq 0$, and $||A|| = 0$ if and only if $A = 0$
		- $||A + B|| \leq ||A|| + ||B||$
		- $|| \alpha A || = |\alpha| ||A||$

- Matrices norm:
	- Matrix norm is a vector norm in a vector space whose elements (vectors) are matrices (of given dimensions).
	- Frobenius norm:
		- In other words, A matrix $A \in C^{m \times n}$ can be regarded as a vector in $C^{mn}$, so one example of a norm is the Frobenius norm $|| \cdot ||_F$:
			- $||A||_F = (\sum_{i=1}^m\sum_{i=1}^n|a_{ij}|^2)^{1/2}$
	- The following 2 norms focus on the magnitude of the individual columns / rows of the matrix
	- Matrix 1-norm (Column sum norm)
		- The 1-norm of a matrix measures the maximum absolute column sum of the matrix. It aggregates the absolute values of the elements in each column separately and then takes the maximum of these sums.
		- It is primarily concerned with how "large" the columns of the matrix are in isolation.
		- $||A||_1 = max(Σ |a_{ij}|)$, where the maximum is taken over all columns of A.
	- Matrix $\infty$-norm (Row sum norm)
		- $||A||_∞ = max(Σ |a_{ij}|)$, where the maximum is taken over all rows of A.

- Example:
	- 1-norm of a matrix
		- Let $A \in \mathbb{C}^{m \times n}$, consider the set $\{ x \in \mathbb{C}^n: ||x||_1 = 1 \}$
		- Step 1: showing $||A||_1 = \underset{\ \leq j \leq n}{max}||a_j||_1$
			- $||Ax||_1 = || \sum_{j=1}^n x_j a_j ||_1 \leq \sum_{j=1}^n |x_j| ||a_j||_1 \leq (\underset{\ \leq j \leq n}{max}||a_j||_1) \sum_{j=1}^n |x_j| = \underset{\ \leq j \leq n}{max} ||a_j||_1$
		- Step 2: Showing $||A||_1 = \underset{\ \leq j \leq n}{max}||a_j||_1$
			- To show this, we need to show 2 things:
				- $||A||_1 \geq \underset{\ \leq j \leq n}{max}||a_j||_1$
					- This inequality holds because $||Ax||_1$ is less than or equal to $\underset{\ \leq j \leq n}{max}||a_j||_1$ for any $x$ in the set under consideration. Hence, the supremum (or maximum) of $||Ax||_1$ is also less than or equal to $\underset{\ \leq j \leq n}{max}||a_j||_1$.
				- $||A||_1 \leq \underset{\ \leq j \leq n}{max}||a_j||_1$
					- This is proven by considering the vector $x$ that achieves the supremum in the definition of $||A||_1$. This vector $x$ has 1-norm equal to 1 and $||Ax||_1$ achieves the supremum. Since $||Ax||_1$ is less than or equal to $\underset{\ \leq j \leq n}{max}||a_j||_1$ for any $x$ in the set, it must also hold for the vector $x$ that achieves the supremum.


