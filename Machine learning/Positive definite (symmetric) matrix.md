- Definite matrix is a property of a mathematical matrix which states that the determinant of the matrix is greater than zero, which is important for many applications.
- Positive definite (symmetric) matrices are subset of symmetric matrices. 
- Considering complex space would be a general situation for positive definite matrix. a Hermitian matrix (that is, a complex matrix equal to its conjugate transpose) is 
- Requirements:
	- 1. All eigenvalues are positive
	- 2. All pivots are positive
	- 3. All sub-determinants are positive
		- sub-determinants = determinant of the submatrix of $A$. 
	- 4. The matrix have to be symmetric (also it is a square matrix otherwise it is not symmetric)
- Slow test:
	- Find all eigenvalues and test it is positive (We want to avoid) 
		- Solving $n^{th}$ order polynomial is computationally costly for large size matrices
- Quick tests for recognizing positive definite matrices
	- 1. For a n by n matrix which n = 2, checking whether the pivots (main diagonal entries of upper triangular form) of the matrices are positive: 
		- $\begin{bmatrix} a&b \\ c&d \end{bmatrix} \rightarrow \begin{bmatrix} a&b \\ 0&c-{b\over a}b\end{bmatrix}$, and then check $a > 0$ and $c-{b\over a}b >0$.
	- 2. For a n by n matrix which n > 2, checking whether a > 0 and the determinant of submatrices of a > 0.
	- 3. Strang's favorite: $x^TAx > 0$
- Properties:
	- 1. It always has positive determinant
		- Proof:
			- $\text{det}A =$ $\prod \lambda_i$. All eigenvalues are positive, thus the determinant is positive. 
			- $\text{det}A = \prod a_{ii}$. All pivots are positive, thus the determinant is positive.
	   - 2. By knowing it is positive definite matrices, we know its stability.
- Applications: 
	- The idea of "positive definiteness of a matrix" connects the whole course.
		- eg:
			- Positive pivots
			- Positive determinants
			- Positive eigenvalues
			- Positive energy
	- 2. It has implications for optimization problems, where it can be used to determine whether a given solution is optimal or not. 
	- 3. The information of "positive definite" of a matrix can helps to simplifies, clarifies the properties and interpretations of [[singular value decomposition]]
- Examples:
	- $\begin{bmatrix} 5&2 \\ 2&3 \end{bmatrix}$
		- Pivots: 5, ${11 \over 5}$ (comes from $\text{det}A = \lambda_1 \lambda_2)$
		- Eigenvalues: $(5-lambda)(3-\lambda)-4$, $\lambda=4 \pm \sqrt5$ 
	- $\begin{bmatrix} -1&0 \\ 0&-3 \end{bmatrix}$
		- 