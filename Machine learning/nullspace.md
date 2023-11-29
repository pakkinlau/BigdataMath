

**Definition:** 
- The nullspace, also known as the [[Kernel space]], is a fundamental concept in linear algebra. It is a subspace of a vector space associated with a [[linear transformation]] of a matrix.
- Nullspace means the space (that fills up with a combination of specific vectors) that multiple with $A$ would always return 0. ($Ax = 0$) (null).
	- Nullspace of the matrix $A$ can be represented as $N(A) = \{ x |Ax = 0\}$
- In other words, the nullspace $N(A)$ in $\mathbb{R}^n$ contains all solutions $x$ to $Ax =0$. This includes $x = 0$. 
- Nullspace is a [[vector space]]
- Left null space and null space 
	-  Null space is representing all possible column vectors $x_{\text{null}}$ that returns 0 for $Ax = 0$
	- Left null space is representing all possible row vectors $w_{\text{null}}$ that returns 0 for$A^Tw = 0$

- Terms:
	- [[pivot]]: it is crucial in determining various properties of a matrix, including its [[rank]] and its solutions to [[systems of linear equations|systems of linear equation]]. 
	- "free columns": In a rectangular matrix where $m < n$, we call the columns that no pivots involves "free columns" 
	- "free variables": In $Ax = 0$,  some components of $x$ are dependent to others, or they are related to free columns 

- Determining nullspace
	- Case 1: n = m or m > n
		- Step 1: We conduct row operations to eliminate the row space to see how many free variables in the matrix
		- Step 2: For each equations in the row space, putting free variables in the right side, putting non-free variables in the left hand side. 
		- Step 3: Putting arbitrary numbers into free variables to get "special solution" of nullspace
		- Step 4: [[span]] the special solution to obtain nullspace. 
	- Case 2: m < n 
		- Step 1: Same as case 1
		- Step 2: Split a square matrix in the left hand side, the left hand side are called "pivot column", the right hand side are called "free column"
		- Step 3: For the variables that associated with free columns, we make special choices of ones and zeros, such as, if we have 2 free columns, we can pick 1,0 and 0,1.
		- Step 4: Solve $Ax = 0$ to get the non-free variable (basic / leading variables, the variables that associate pivot columns). Say 

---

- Nullspace in context: 

- [[systems of linear equations|solving systems of linear equations]]:
	- If $Ax = 0$, then $\begin{bmatrix} row1 \\ \vdots \\ rowm \end{bmatrix}_{m \times n} \begin{bmatrix} x \end{bmatrix} = \begin{bmatrix} 0 \\ \vdots \\ 0\end{bmatrix}$, where $x$ is a $n$- dimensional vector.
		- Insights
			- 1. Because every row of $A$ times $x$, would return $0$. Therefore every $x$ is [[Orthogonal vector|orthogonal]] to every row of $A$. 
				- which means $row1 [\vec x] = 0$, ... $row_n [\vec x] = 0$. 
			- 2. We cannot express the nullspace of $A$, $Null(A)$, solely with vector $x$. We would express the nullspace of $A$ as: $N(A) = \{ x |Ax = 0\}$.
				- So nullspace contains some dots only?
			- 3. Since any $x$ is [[Orthogonal vector|orthogonal]] to every row of $A$, the [[linear combination]] / [[span]] of the $x$ in the set of $N(A)$ is the nullspace of $A$. i.e. $N(A) = span(\{ x |Ax = 0\})$.
	- Example: 
		- $A = \begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix}$
		- After eliminating linearly dependent equations, there is only 1 equation left. 
		- Special solution
			- We find our "special solution" by choosing some points of the first equation to be some constant that in the line (a.k.a. substitute a random number), until there is $n - r$ free variable left in those equations.
			- Then we can express the nullspace from that. In the above example, if choosing $x_2 = 1$, then the equation return $x_1 = -2$. So the special solution is $\mathbb{R}^1$ and it is located at $(-2,1)$. 
		- Extend it to be $R^1$:
			- The nullspace is the span of all special solutions (for dots) / free variables (for vectors).
			- If we have $(-2,1)$, then the nullspace is the span of it, so $Null(A) = \{ (-2 x_2, x_2) | x_2 \in \mathbb{R} \}$
			- This is a line because it rely on 1 variable only but it also exhibit on 2D space because it is composed by 2 components in coordinate. 

	- [[Linear transformation]]:
		- Say we have a matrix $A \in C^{m \times n}$ takes a vector $x \in C^n$ and outputs a vector $b = Ax \in C^m$. $A: C^n \rightarrow C^m$, $x  \mapsto Ax$ , which $A$ is a function that [[Linear transformation]] the vector from the complex vector space $C^n$ as its input, and maps it to a vector in a complex vector space $C^m$ as its output. 
		- The nullspace of $A$, denoted $null(A)$, is the set $\{ x \in C^n: Ax = 0\} \subset C^n$
---

-  **Basic Properties:**
	- 1. Nullspace is always a [[subspace]] of the domain of the [[linear transformation]] represented by the matrix A.
		- Q: what is the meaning of "domain of the linear transformation"?
	- 2. Nullspace of $A$ is the solution of $Ax = 0$. 
	- 3. Nullspace is non-empty because it always contains at least the [[zero vector]].
	- 4. Nullspace and [[invert|invertible]] matrix
		- If $Null(A)$ contains only the zero vector, then the matrix A is said to have full column [[rank]], meaning all its columns are [[Linear independence|linearly independent]], and that matrix $A$ is [[invert|invertible]].
	- 5. The nullspace of a [[matrix]] always perpendicular to the [[row space]] of the matrix.
		- Every $x$ in the nullspace of $A$ is orthogonal to the row space of $A$; every $y$ in the nullspace of $A^T$ is orthogonal to the [[column space]] of $A$.  i.e. ($N(A) \perp C(A^T)$ , $(N(A^T \perp C(A))$)
		- EG1: Null space contains only zero vector for some full [[rank]] matrix $A$. 
			- The [[Kernel space]] of $A$ is trivial, that is, it contains only the null vector as an element. $\text{ker}(A) = 0$
			- Then, $A$ is invertible. 
	- 6. We can express line/plane/space of nullspace with either: (multiplying free variables on those vectors (if it is a line) / linear combinations of those vectors)
		- EG: the matrix with free variables. (There are a 1-D straight line satisfies $Ax = 0$)
			- For the example in the blackboard, we have 3 unknowns and 2 equations, so we have a line as the solution. 
			- Some $v$ gives $Av=0$ 
			- by reasoning, we have $\begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}$ as one of the solution, and all linear multiples of this one will all be the solution. The line / space is the nullspace for $Av = 0$, which is perpendicular to the row space. 
			- Formally: the null space can be expressed as: $N(A \cdot w) = N(A^Tw) = w\begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}$
	7. nullspace and left nullspace are orthogonal to each other 
	- EG: Show $x^T(A^Ty) = 0$ 
	- This is a key property that relates the nullspace and the left nullspace of a matrix. It demonstrates that vectors in the nullspace are [[Orthogonal vector|orthogonal]] to vectors in the [[left nullspace]].
	- $x$ taking [[dot product]] $A^Ty$ effectively checks how much of [[left nullspace]] vectors $A^Ty$ remains in the [[nullspace]]. 
	- This property is significant because it establishes a connection between the nullspace and the left nullspace of a matrix. It shows that vectors in the nullspace are orthogonal to vectors in the left nullspace. Orthogonality is often an important property in linear algebra and can simplify various mathematical and computational tasks.
	- Steps: 
		- 1.Taking [[dot product]] for (row space AND nullspace), and taking dot product for (column space AND left nullspace).
			- Here, $x$ is in the nullspace of $A$, which means that $Ax = 0$. 
			- $x^T(A^Ty) = (Ax)^Ty = 0^Ty=0$.
				- in the context of [[Matrix-Vector Multiplication]] $Ax = 0$,
					- $A$ represents [[row space]] of $A$, 
					- $x$ represents [[nullspace]] of $A$
				- In the context of [[Matrix-Vector Multiplication]] $A^T y = 0$, 
					- $A^T$ represents [[column space]] of $A$
					- $y$ represents [[left nullspace ]]of $A$
			- By this property, we know nullspace and left nullspace of $A$ is orthogonal to each others. 
		- 2. $\text{dim}(N(A))$ has dimension $n - r$. $\text{dim}(N(A^T))$ has dimension $m - r$. 
		- 3. $C(A^T)$ is orthogonal complement of $N(A)$, $C(A)$ is orthogonal complement of $N(A^T)$.
			- So $\text{dim}(C(A^T)) + \text{dim}(N(A)) = n$
			- $\text{dim}(C(A)) + \text{dim}(N(A^T)) = m$


---

1. **Geometric Interpretation:** Geometrically, the nullspace corresponds to all vectors that get mapped to the origin ([[zero vector]]) under the linear transformation represented by the matrix A. In 2D and 3D spaces, this can be thought of as the "directions" in which the transformation collapses or squishes vectors to zero.

2. **Application:** Understanding the nullspace is crucial in [[systems of linear equations]], finding the basis for a subspace, and studying the properties of linear transformations. It's also important in fields like computer graphics, data analysis, and machine learning, where linear algebra plays a fundamental role.

3. **Basis of Nullspace:** Just like any subspace, the nullspace can have a [[basis]], which is a set of linearly independent vectors that span the entire nullspace. These basis vectors help us understand the [[dimension|dimensionality]] of the nullspace.

4. **[[Dimension]]:** The dimension of the nullspace, denoted as $dim(Null(A))$, is also known as the nullity of the matrix A. It provides information about the "degrees of freedom" or the number of solutions to the homogeneous equation Ax = 0.

5. **Relation to Rank:** There is an important relationship between the nullspace and the rank of a matrix A. The rank-nullity theorem states that the sum of the rank of A (the dimension of its column space) and the nullity of A (the dimension of its nullspace) is equal to the number of columns in A.

6. [[Rank-Nullity Theorem]]:
	- The rank-nullity theorem states that for any matrix A, the sum of the rank of $A$ (the maximum number of linearly independent columns) and the nullity of A (the dimension of the nullspace) is equal to the number of columns in A, i.e., $rank(A) + dim(Null(A)) = n$, where $n$ is the number of columns in $A$.

---
