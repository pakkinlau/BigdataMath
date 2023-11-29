---
alias: Dimension theorem, counting theorem
---


- Favors:
	- Gilbert Strang: Dimension theorem / Counting theorem
	- ChatGPT: Rank-nullity theorem
- Definition:
	- It provides important insights into the relationship between the [[dimension]]s of the [[vector space]]s involved in a [[linear transformation]]. This theorem is a powerful tool for understanding the structure of [[linearity]]s and plays a crucial role in various areas of mathematics and engineering.
- Theorem:
	- Suppose we have a linear transformation $T: V \rightarrow W$ between two vector spaces, where $V$ and $W$ are finite-dimensional vector space
	- The dimension theorem states that $dim(V) = rank(T) + nullity(T)$
		- $dim(V)$:
			- This represents the dimension of the domain vector space V, which is the number of linearly independent vectors in V.
		- $rank(T)$
			- his is the rank of the linear transformation T, which is the dimension of the image (or range) of T.  In other words, it is the maximum number of linearly independent vectors that can be obtained by applying T to vectors in V.
		- $nullity(T)$
			- The nullity of T is the dimension of the kernel (null space) of T, which consists of all vectors in V that map to the zero vector in W under T.

- Example: 
	- Counting theorem:
		- Say we have $n \times n$ matrix $A$, and its dimension is $r$. There are $n - r$ independent solutions to $Ax = 0$.
	
	- Say $A$ is a $3 \times 3$ matrix.
	- $A$ has rank $r = 2$. So dimension of [[nullspace]] is $1$. 
	- $n - r = 3 - 2 = 1$
	- So $Ax = 0$ has one solution for $x$. 

- Interpretation and implications:
	- It establishes a relationship between the dimensions of the domain, range, and null space of a linear transformation. This relationship is fundamental for understanding the structure of linear mappings.
	- It implies that the sum of the dimensions of the range and null space of T is equal to the dimension of the domain V. In other words, it tells us that no information is lost when we apply T. 
	- The rank of T gives us insight into the "output space" of the transformation, while the nullity of T tells us about the "input space" that gets mapped to zero.
	- This theorem is widely used in solving systems of linear equations, finding bases for vector spaces, and determining the invertibility of linear transformations.
- Applications:
	- Computer Graphics: In computer graphics and computer vision, the Dimension Theorem is used for transformations and projections.
	- Control Theory: It is used in control systems engineering to analyze and design controllers for dynamic systems.
	- Statistics: In multivariate statistics, the theorem is applied to understand the dimensionality of data and reduce its complexity.
	- Machine Learning: In machine learning, linear transformations are often used in feature engineering and dimensionality reduction techniques.
	- Quantum Mechanics: In quantum mechanics, linear operators are used to represent physical observables, and the Dimension Theorem helps understand the relationships between different quantum states.

- Related concepts:
	- [[dimension]]
	- [[rank]]
	- [[null]]