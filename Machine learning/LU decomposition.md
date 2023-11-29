---
alias
---

- Related:
	- [[Elimination using matrices]]

A = LU decomposition, also known as LU [[Matrix factorization]], is a fundamental technique in linear algebra used to factorize a [[square matrix]] A into the product of two lower and upper [[triangular matrix|triangular matrices]] L and U, respectively. This decomposition plays a crucial role in various numerical algorithms and applications, such as [[systems of linear equations|solving systems of linear equations]], calculating [[Determinant]], and performing [[invert|matrix inversion]]

**The Decomposition:**

- $A = LU$: 
	1. **Matrix A:** A is an n x n [[square matrix]]  that you want to factorize into LU form.
	2. **Lower Triangular Matrix (L):** L is also an n x n square matrix that is lower triangular, meaning all elements above the main [[diagonal matrix|diagonal]] are zero. The diagonal elements of L are all 1's.
	3. **Upper Triangular Matrix (U):** U is an n x n square matrix that is upper triangular, meaning all elements below the main diagonal are zero.
	    


**Purpose and Applications:**

1. **Solving Linear Systems:** LU decomposition is often used to solve systems of linear equations (Ax = b) efficiently. Once A is decomposed into LU form, solving for x becomes simpler and faster.
    
2. **[[invert|matrix inversion]]:** LU decomposition is useful for finding the inverse of a matrix. If A = LU, then A⁻¹ = U⁻¹L⁻¹, which can be easier to compute.
    
3. **[[Determinant]]:** The determinant of a matrix can be calculated more easily from its LU decomposition. The determinant of A is the product of the diagonal elements of U.
    
4. **[[Matrix factorization]]:** LU decomposition is a crucial step in many matrix factorization methods used in machine learning and data analysis, such as [[singular value decomposition]] (SVD) and [[Reduced QR decomposition]].

### Step of getting $A = LU$ decomposition

- How to obtain $L_{ij}$? 
	- That means we gonna review Chapter 2.3 (Elimination using matrices)
	- To begin with, we put an identity matrix on both side of the equation.
	- Then we start to eliminate $l_{ij}$ from the matrix $A$ from the bottom left.
	- $L_{ij}$ is the identity matrix, minus the multiplier $l_{i1} \over l_{11}$ in row $i$, column $1$. 
- Factorizing 1 entry from a matrix: 
	- 1. Multiplying an identity matrix at the beginning of A. 
	- 2. Execute row operation. The row multiplier $l_{ij}$ will be recorded in the identity matrix, 
	- 3. This produces $L_{ij}$ , which is a diagonal matrix, with an additional multiplier that keeps the information of the multiplier involved to cause that entry to be 0.


**Computational Complexity:** The LU decomposition of an n x n matrix A has a computational complexity of $O(n^3)$. However, once the decomposition is computed, solving linear systems and performing other operations become more efficient.
	- The cost of computation:
		- Elimination of $A$ requires about ${1 \over 3} n^3$ multiplications and $n^2$ subtractions



**Numerical Stability:** LU decomposition can be sensitive to the choice of pivoting strategy to handle potentially [[singular matrix]] or ill-conditioned matrices. Techniques like partial pivoting or full pivoting are often used to enhance numerical stability.



---
Old notes:

### See elimination as factorization: $A = LU$ or $A = LDU$ (lower triangular)(upper triangular)
- Many ideas of linear algebra, when you look at them closely, are really factorization of a matrix
	- $L$: 
		- The whole forward elimination process (with no exchanges is inverted by $L$, $L = (L_{21}L_{31} \dots L_{n1})(L_{32} \dots L_{n2}) \dots (L_{n} L_{n-1})$.
		- $L_{ij}$:
			- The sequence of elimination is important. So the sequence of $Lij$ cannot be changed. 
			- The number of terms depends on....  the size of the matrix A.
			- Because $L$ contains the information of elimination for each entry, It must be a lower triangular matrix. 
		- The low triangular L has all 1 on its diagonal. The multipliers $i_{ij}$ are below the diagonal of L.
	- $\text{det} L$:
		- related to Chapter 5.2
	- We could claims "No row exchange is involved.". Because each matrix E is just considering one off-diagonal entry $i_{ij}$ of A. S
		- This is elimination without row exchanges. 
	- $U$:
		- The upper triangular U has the pivots on its diagonal. 
		- We define $U$ is the matrix which is already able to solve $Ax = LUx = Lb$.
		- The original $A$ is recovered from $U$ by $A = LU$ (lower triangular)(upper triangular)
	- More characteristics (p.99 of the book)
		- When a row of $A$ starts with zeros, so does rows of L.      --- why?
		- When a column of $A$ starts with zeros, so does that column of U.     --- why?
	- $\text{det} U$:
		- 
	- Better balance from LU to LDU
		- LU is unsymmetric because U has pivots on its diagonal, while L has 1 on its diagonal. 
		- Divide U by a diagonal matrix D that contains the pivots. That leaves a new triangular matrix with 1 on the diagonal. 


