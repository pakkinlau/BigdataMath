**Concept:** Row Space

**Context:** Linear Algebra

Row space is a fundamental concept in linear algebra that plays a crucial role in understanding the properties and relationships of [[matrix|matrices]] and [[systems of linear equations]]. It is closely related to the concept of column space and is a key component of the theory of [[vector space]]s.

- Definition:
	- say we have a $m \times n$ matrix $A$. 
	- $dim(Domain(A)) = dim(C(A^T)) = m$. So that the dimension of input data from $A$ should be $n$. 


**Key Points:**

1. **Definition:** The row space of a matrix is the [[subspace]] of the vector space spanned by the rows of the matrix. In other words, it is the set of all [[linear combination]]s of the rows of the matrix.

2. **Matrix Representation:** Let's consider an m x n matrix A, where each row has n elements. The row space of A, denoted as $Row(A)$, is the subspace of the n-dimensional vector space $R^n$ spanned by the rows of A.

3. **[[Dimension]]:** The dimension of the row space of a matrix A is also known as the [[rank]] of A, denoted as rank(A). It represents the maximum number of [[Linear independence|linearly independent]] rows in the matrix. The rank of a matrix provides essential information about its properties and solutions to linear systems.

4. **Relationship with Column Space:** There is a fundamental relationship between the row space and the column space of a matrix. 
	- The row space of A is equal to the column space of the transpose of A (Row(A) = Col(A^T)). 
	- This relationship is known as the [[row-column theorem]].

5. **Gaussian Elimination:** 
	- Row space is closely tied to the process of Gaussian elimination. During Gaussian elimination, the rows of a matrix are transformed to [[row echelon form]] or [[Reduced Row Echelon Form]]. The nonzero rows in the reduced row-echelon form of a matrix form a basis for the row space of that matrix.
	- In [[Column-row decomposition -- $A = CR$]], the row matrix $R$ is actually [[Reduced Row Echelon Form|Reduced Row-Echelon Form (RREF)]]. 

6. **Applications:** Row space is essential in [[systems of linear equations|solving systems of linear equations]], finding solutions to homogeneous equations, and understanding the linear independence of vectors. It also plays a role in various areas of science and engineering, including computer graphics, control theory, and data analysis.

7. **Subspace:** Row space is a subspace of the vector space associated with the matrix. This means that it is a set of vectors that is itself a vector space, satisfying the properties of closure under addition and scalar multiplication.

---
- Row space of a matrix is the subspace of $R^n$ spanned by the rows. 
- It is called $C(A^T)$ of a matrix $A$. 
- Row space and column space has a lot of commonalities. Use $C(A^T)$ so that we don't need to introduce a new letter for the row space. 
- Properties:
	- For $Ax = b$, $x \in R^m$ ($x$ could be represented by a linear combination or rows of $A$. )
		- Proof: 
			- Because $A$ is $(m \times n)$, $x$ must be $(n \times k)$. k could be any numbers. 
		- Examples:
			- Formally, the row space can be expressed as:  $A^Tw = w_1 \begin{bmatrix}1 \\ 2 \\ 3\end{bmatrix} + w_2 \begin{bmatrix}4 \\ 5 \\ 6\end{bmatrix}$

