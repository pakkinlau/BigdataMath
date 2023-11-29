---
alias: [invertible, invertibility, inverting, inverse, inverse matrix, inversion, matrix inversion]
---

- Definition:
	- An invertible matrix is a square matrix that possesses unique and essential properties, making it a cornerstone of linear algebra and many other fields.
- Characteristic
	- Square matrix:
		- An invertible matrix is always a square $n \times n$ matrix
	- Full [[rank]]:
		- An invertible matrix must have full rank, meaning all its rows and columns are [[Linear independence|linearly independent]]. This property ensures that the matrix can be completely inverted.
	- [[invert|inverse]] existence:
		- The defining characteristic of an invertible matrix is that it has an inverse, denoted as A^(-1). When an invertible matrix is multiplied by its inverse, the result is the identity matrix (I). In mathematical notation, if A is invertible, then A * A^(-1) = I.
	- [[determinant]] non-zero:
		- $Det(A) \neq 0$ (we shouldn't use determinant to explain invertibility

---
## Inverse matrix


- Definition:
	- There is an inverse matrix $A^{-1}$ such that $A^{-1}A = I$. Whatever $A$ does, $A^{-1}$ undoes. Their product is the identity matrix, which does nothing to a vector.
		- The inverse exists if and only if elimination produces $n$ pivots. 
		- The matrix $A$ cannot have 2 different inverses. 
- Properties:
	- 1. A matrix is invertible if there exists an $n \times n$ square matrix $B$ such that $AB = BA = I_n$.
	- 2. The inverse of $AB$ is $B^{-1}A^{-1}$
		- The elementary values of the inverse matrix of $A$ can be determined by something like Cramer's rule. 
		- If $Ax = 0$ for a nonzero vector $x$, then $A$ has no inverse.  
		- If the determinant of $A$ is zero, then $A$ has no inverse.
	- 3. $(A^T)^{-1} = (A^{-1})^T$
		- Proof
	- 4. $\text{det}A^{-1}=(\text{det}A)^{-1}$
		- Proof
	- 5. $A$ is row-equivalent and column-equivalent to the $n \times n$ identity matrix $I_n$. 
		- That means you can diagonalize that matrix, and then scale each element to one. 
- Theorems:
	- $(AB)^{-1} = B^{-1}A^{-1}$
	- Proof:
		- Show $(AB)^{-1}(AB) = I$
			- $(AB)^{-1}(AB) = B^{-1}A^{-1}AB = B^{-1}IB = B^{-1}B = I$



