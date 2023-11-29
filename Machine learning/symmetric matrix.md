- **Definition:**
	- A is symmetric if and only if for every $i,j$, $a_{ji} = a_{ij}$.  
	- Appreciate the beauty the factorization of $S = Q \Lambda Q^{-1} = Q \Lambda Q^T$ . 
		- which $Q$ is [[orthogonal matrix]]
		-  A symmetric matrix is a [[square matrix]] that is equal to its transpose. ($A = A^T$)
		- which $\Lambda$ is eigenvalue matrix
		- Which, any inner or outer product of a matrix, such as $AA^T$, are automatically symmetric. This expression links such fact, and also all components of $Q$ has length = 1. And then. the length component of $S$ is stored within $\Lambda$.  
	- The eigenvalues of $S$ are real
		- Proof:
			- Suppose we have $Sx = \lambda x$.  --- equation 1
			- Hermitianizing (= Taking conjugate + taking transpose) for both sides we have:  
				- $(Sx)^H = (\lambda x)^H$  -->  ${\bar x}^T S = {\bar x}^T \bar \lambda$--- equation 2
				- Note: hermitianizing is a normal operation for transposing a complex matrix.
			- To compare equation 1 and 2, we do two inner product separately such that two LHS of the equations will be equal. We multiply equation 1 with $\bar x^T$ and equation 2 with $x$. 
				- $\bar x^T S x = \bar x^T \lambda x$ --- equation3
				- $\bar x^T S x = \bar x^T \bar \lambda x$ --- equation 4.
			- Combining equation 3 and 4 we get $\lambda = \bar \lambda$. Recall $\lambda = a + bi$, It means it could only be $\lambda = a \in \mathbb{R}$, and $b = 0$.  
			- QED.
	- The eigenvectors of $S$ are perpendicular to each others. 
		- Proof of "eigenvectors are perpendicular"
			- That means proofing $x^Ty = 0$, where $x$ and $y$ are distinct eigenvector of the symmetric matrix. 
			- Start from these facts:
				- $Sx = \lambda x$
				- $Sy = \alpha y$. $\lambda \neq \alpha$
				- $S^T = S$
			- a. We transpose $Sx$, into $x^TS^T = \lambda x^T$, and use $S^T = S$ and multiplying $y$, we get $x^TSy = \lambda x^Ty$. 
			- b. we multiply $x^T$ on $Sy = \alpha y$, we get $x^TSy = \alpha x^Ty$
			- combining the result from a and b, we get $\lambda x^T y = \alpha x^T y$
			- Since $\lambda \neq \alpha$, $x^T y$ must be zero. 
		- In the proof, we made assumption of $\lambda$ and $\alpha$ were equal, to simplify the proof. The eigenvectors of symmetric matrix is true, no matter the eigenvalues are distinct or not.
	- A square matrix $S$ that is equal to its transpose. 
		- i.e. $S = S^T$. 

Famous formula
- $A = X \Lambda X^{-1}$ and therefore $S = X \Lambda X^{-1}$ is also true
	- $X$: eigenvector matrix
	- $\Lambda$: eigenvalue matrix
- $S = Q \Lambda Q^T$
	- where
		- $Q$: orthogonal matrix
		- $\Lambda$: real eigenvalue matrix
	- The form means "a symmetric matrix can be broken up into its eigenvectors"


**Properties and Characteristics:**

1. Geometrical properties:
	- **Diagonal Elements:** The diagonal elements of a symmetric matrix are always real numbers.
	-  **Off-Diagonal Elements:** The off-diagonal elements (elements not on the main diagonal) are symmetric with respect to the main diagonal. In other words, if A[i][j] is an element in the matrix, then A[j][i] will have the same value.
	- **Symmetry About the Main Diagonal:** Geometrically, you can think of a symmetric matrix as a mirror image of itself across its main diagonal. This symmetry has important mathematical implications.
2. [[eigenvalues]]: Symmetric matrices have real eigenvalues 
3. [[eigenvectors]]: Symmetric matrices have a complete set of orthogonal eigenvectors ($q_1, \dots, q_n$) in an [[orthogonal matrix]] $Q$. This property makes them valuable in various applications, including [[systems of linear equations]] and [[principal component analysis]] (PCA).

Property 4 and 5 are "spectral theorem" in mathematics. See the entity "Spectral theorem" for the details. 
- 4. The eigenvector of diagonalized $S$,  $S = X\Lambda X^{-1}$ can be chosen orthogonal.
	- Proof: Spectral theorem
- 5. The length of diagonalized $S$,  $S = Q\Lambda Q^T$ can be unit length.
	- Proof: Spectral theorem.

- 6. Every symmetric matrices $S$ break up into  $S = Q\Lambda Q^{-1} = Q\Lambda Q^T = \lambda_1q_1q_1^T + \dots + \lambda_nq_nq_n^T$, which shows $S$ is a sum of rank one matrices, $\lambda_k q_k q_k^T$. 
	- Where $Q$ is orthonormal eigenvectors (from property )
	- Where the set of  $q_1q_1^T , \dots , q_nq_n^T$ are a combination of perpendicular projection matrix. 
	- Where each $qq^T$ are projection matrices. 
	- Proof (of breaking down terms):
		- $A = Q \Lambda Q^T = \begin{bmatrix} q_1&q_2&\dots&q_n\end{bmatrix}\begin{bmatrix}\lambda_1&&& \\ &\lambda_2&&\\&&\ddots&\\&&&\lambda_n\end{bmatrix}\begin{bmatrix}q_1^T \\ q_2^T \\ \vdots \\ q_n^T\end{bmatrix} = \lambda_1q_1q_1^T + \dots + \lambda_nq_nq_n^T$
			- Importance of break up a matrix into n-terms:
				- 1. It highlights the relationship between eigenvalues $\lambda_i$ and eigenvectors $q_i$.
				- 2. Shows $A$ can be [[diagonalization|diagonalize]]d using its [[eigenvectors]] and [[eigenvalues]].
				- 3. [[Projection]]: Each term can be thought of as a projection operator. 
				- 4. [[Spectral theorem]]: It is a way to express a matrix as a sum of scaled projection operator of its eigenvectors and eigenvalues.
				- 5. Computing: This form can simplify the computation of matrix powers and functions. 
		- Dimensional analysis (of why the rightmost expression is a scalar): 
			- First 2 terms: (1 x n) (n x n) --> (1 x n)
			- Then multiply with the last term: (1 x n)(n x 1) = 1
	- Proof (of $qq^T$ are projection matrices)
		- $qq^T = \begin{bmatrix}e_1 \\ e_2 \\ \vdots \\ e_n \end{bmatrix} \begin{bmatrix}e_1 & e_2 & \dots & e_n \end{bmatrix} = \begin{bmatrix}e_1^2 &&& \\ &e_2^2&& \\ &&\ddots& \\ &&&e_n^2\end{bmatrix} = I_n$

	- 5. $X^HX = \bar X^T X = |X|^2$ for complex number, $X^T X = |X|^2$ for real number 
		- (important!) $X = \begin{bmatrix} x_1 & x_2 & \dots & x_n \end{bmatrix} \in R^{m \times n}$, $x_i \in R^{m \times 1}$ 
		- Proof:
			- Trial 1 (Wrong):
				- $X^HX = \bar X^T X = \begin{bmatrix} \bar x_1 & \bar x_2 &\dots & \bar x_n \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n  \end{bmatrix} = \bar x_1 x_1 + \bar x_2 x_2 + \dots + \bar x_n x_n =  |x_1|^2 + |x_2|^2 + \dots + |x_n|^2  = |X|^2$
			- Trial 2: For the product of  $X^HX$,  $a_{ij} = \sum x_i^H x_j$
				- If $i = j$, $a_{ij} = |x_i|^2$ (Already proved $\bar z z = |z|^2$ in the property of modulus. )
				- If $i \neq j$, $a_{ij} = 0$
			- Therefore $X^HX = \begin{bmatrix}  |x_1|^2 &&& \\ & |x_2|^2 && \\ && \ddots & \\ &&& |x_n|^2\end{bmatrix} = |X|^2$
			- QED. 
	- 
	- 6. Symmetric matrices $S$ has $n$ orthonormal eigenvectors $q_1, \cdots, q_n$.
		 - Proof:
			 - 1. From property 1c, we have $S = Q\Lambda Q^{-1} = Q\Lambda Q^T$.
			- 2. We have $(Q^{-1})^T\Lambda Q^T = Q\Lambda Q^{-1}$. By comparing terms, we have:
				- $Q^T = Q^{-1}$, which means $Q$ fits the properties of orthonormal eigenvectors. 
	- 7. Orthonormality $x_i = q_i$ gives $X = Q$
	- 8. The eigenvectors can be chosen orthonormal, and orthogonal matrices have $Q^{-1} = Q^T$. 
	- 9. Easy to see $Q \Lambda Q^{-1}$ is symmetric, by taking transpose of it. 
	- 10. The sum and difference of two symmetric matrices is symmetric
	- 11. $A^n$ is symmetric if $A$ is symmetric
	- 12. If $A^{-1}$ exists, it is symmetric if and only if $A$ is symmetric.
	- 13. Rank of a symmetric matrix $A$ is equal to the number of non-zero eigenvalues of $A$. 
		- Rank is the number of pivots in a matrix
		- Eigenvalues are located on the pivots
		- So this property is true. 
	- 14. $AA^T$ and $A^TA$ are automatically symmetric, nonnegative definite and square matrix. 
		- Proof of square:
			- $(n \times m)(m \times n) \rightarrow (n \times n)$
		- Proof of symmetric:
			- method 1: $(A^TA)^T = A^TA$, $(AA^T)^T = AA^T$ 
			- method 2: $\begin{bmatrix} a&b \\ c&d \end{bmatrix} \begin{bmatrix} a&c \\ b&d \end{bmatrix} = \begin{bmatrix} a^2+b^2 & ac+bd \\ ac+bd & c^2 + d^2 \end{bmatrix}$


1. . **Positive Definiteness:** Symmetric matrices are often encountered in positive definiteness problems. A symmetric matrix A is positive definite if x^T * A * x > 0 for any non-zero vector x. Positive definite matrices have all positive eigenvalues.
2. Every real symmetric matrix can be [[diagonalization|diagonalizable]], and be written as $S = Q \Lambda Q^{-1}$ and also $S = Q\Lambda Q^T$. (Because $Q^{-1} = Q^T$). All this follows from $S^T = S$, when $S$ is real. 
3. [[antisymmetric matrix]]

**Applications:**

1. **Solving Linear Systems:** Symmetric matrices are often used in solving systems of linear equations. Algorithms like Cholesky decomposition and conjugate gradient descent work efficiently with symmetric matrices.

2. **Principal Component Analysis (PCA):** PCA is a dimensionality reduction technique that utilizes the eigenvectors of the covariance matrix, which is symmetric, to find the principal components of data.

3. **Quadratic Forms:** Symmetric matrices are used in quadratic forms, which are essential in optimization problems and statistics.

4. **Physics and Engineering:** Symmetric matrices find applications in various branches of physics and engineering, such as stress analysis, quantum mechanics, and vibration analysis.

**Examples:**
1. The identity matrix is symmetric since it is equal to its transpose.
   ```
   I = [1 0]
       [0 1]
   ```

2. A symmetric 2x2 matrix:
   ```
   A = [a b]
       [b c]
   ```

3. The covariance matrix in statistics is often symmetric, as it represents the pairwise covariances between variables.

In summary, symmetric matrices are a fundamental concept in linear algebra with numerous applications in mathematics, science, and engineering due to their unique properties and mathematical significance.



---

- Definition:

- Properties:
	- 1.  

	- 4.  Eigenvalues of $S$, i.e. :  ($\lambda_1 , \dots, , \lambda_n$) are real


- Applications:
	- $S$ could be the most important matrices the world will ever see. (Why?)
