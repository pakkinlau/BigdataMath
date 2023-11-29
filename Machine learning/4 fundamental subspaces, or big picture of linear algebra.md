- Concepts involved:
	- [[rank]] $r$
		- [[invert|invertibility]]
		- [[Rank-Nullity Theorem]]
	- [[nullspace]] / [[left nullspace]]
		- [[subspace]] / [[vector space]]
	- [[Orthogonal vector]]
	- [[matrix]]
		- [[row space]]
		- [[column space]]




- The fundamental theorem connects "[[rank]]" and "dimension". The rank of $A$ reveals the [[dimension]]s of all four fundamental [[subspace]]s. 

- The construction of "big picture":

	- 1. If $Ax = 0$, then $\begin{bmatrix} row1 \\ \vdots \\ rowm \end{bmatrix} \begin{bmatrix} x \end{bmatrix} = \begin{bmatrix} 0 \\ \vdots \\ 0\end{bmatrix}$
		- Insights
			- a. Because every row of $A$ times $x$, would return $0$. Therefore $x$ is [[Orthogonal vector|orthogonal]] to every row of $A$. 
			- b. Extending point 1 would be, every $x$ in the [[nullspace]] of $A$ is [[Orthogonal vector|orthogonal]] to the [[row space]] of $A$.
				- Q: why $x$ are in the nullspace? 
				- A: There could be more than one $x$ satisfies $Ax = 0$.  
			- c. Say we have a new problem $A^T y = 0$. Then every $y$ in the [[nullspace]] of $A^T$ is [[Orthogonal vector|orthogonal]] to the [[column space]] of $A$.
				- Q: why we want to know about there are some  "y" orthogonal to the column space of $A$?
				- A: 
					- a. [[Orthogonal vector|orthogonal]] complement
						- In this case, the orthogonal complement of the column space of $A$ is the set of all vectors $y$ such that $A^Ty = 0$.
					- b. solving homogeneous systems
						- The equation $A^Ty = 0$ represents a homogeneous system of linear equations. Knowing that there are non-trivial solutions (i.e., solutions where $y$ is not the zero vector) to this system means that the columns of $A$ are linearly dependent. In practical terms, this implies that there is redundancy in the information represented by the columns of $A$.
					- c. Least squares solutions
						- In regression analysis and other applications, you often encounter [[over-determined]] systems of linear equations ($Ax = b$ where $A$ has more rows than columns). Finding vectors $y$ [[Orthogonal vector|orthogonal]] to the [[column space]] of $A$ can help you find the least squares solutions, which minimize the sum of squared errors.
					- d. [[Linear independence]] and [[Basis]]
						- If you're working with [[vector space]]s and [[Basis]], understanding the vectors [[Orthogonal vector|orthogonal]] to the [[column space]] can help you determine whether a set of vectors [[span]] the space or is [[Linear independence|linearly independent]].
			- d. With 2 and 3, we know $N(A) \perp C(A^T)$, $N(A^T) \perp C(A)$
				- [[Rank-Nullity Theorem]]
					- The rank of a matrix $A$ is the maximum number of linearly independent columns in $A$. The nullity of $A$ is the [[dimension]] of the [[nullspace]] (the set of all solutions to $Ax = 0$). 
					- The rank-nullity theorem states that the [[rank]] of a matrix plus its nullity equals the number of columns. When you find non-trivial solutions to $A^Ty = 0$, it indicates that the nullity of $A$ is greater than zero, which is related to the linear dependence of columns and can be used to compute the rank.
					- So we have: 
						- $N(A) \perp C(A^T)$
							- $dim(N(A)) = n - r$
							- $dim(C(A^T)) = r$
						- $N(A^T) \perp C(A)$
							- $dim(N(A^T)) = m - r$
							- $dim(C(A)) = r$
	- 2. Orthogonality:
		- Every $x$ in the nullspace of $A$ is orthogonal to the row space of $A$, $N(A) \perp C(A^T)$. 
			- "dot product of 2 vectors = 0" $\leftrightarrow$ "2 vectors are orthogonal" 
		- Every $y$ in the nullspace of $A^T$ is orthogonal to the column space of $A$, $N(A^T) \perp C(A)$
			- same as above 
	- 3. Dimensionality: 
		- Dimensions: $N(A) \perp C(A^T)$ , dimension are $n-r$ and $r$ respectively; $N(A^T) \perp C(A)$, dimension are $m-r$ and $r$ respectively.  
	- 4.[[Rank-Nullity Theorem]]
		- If all rows in row space are independent, then the dimension of nullspace is 0.
	- 5. [[Rank-Nullity Theorem|counting theorem]]: 
		- Row space and column space have the same dimension $r$, which is the rank of the matrix. 


- With the above information, we can come up with this graph:
![[Pasted image 20230913030131.png]]

From the "big picture of linear algebra" graph:
- 1. Row space
	- In the matrix, there could be $n$ rows, but we just put $r$ independent rows into the graph. It's dimension is $\mathbb{R}^n$
- 2. Nullspace
	- We also have a space of vectors that are perpendicular to row space. 
- 3. [[column space]]
	- If we think of a matrix as a function, column space is the [[column space]] of applying matrix A
	- The dimension of column space is $\mathbb{R}^m$. 
	- $Ax_{row} = b$ 
	- which $b$ is a linear combination of the column space of $A$. 