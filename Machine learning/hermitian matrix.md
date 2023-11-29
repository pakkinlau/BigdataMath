---
alias: self-adjoint
---

- Related: [[adjoint]], [[symmetric matrix]]

- Definition:
	- TD;DL: $A^* = A \Leftrightarrow$ Hermitian matrix
	- While [[symmetric matrix]] is $S = S^T$ for real matrices, we have $S = \bar S^T = S^*$ for complex matrices. 
		- $\bar a_{ij}$ denotes [[complex conjugate]] of $a_{ij}$.

**Definition:**
	A Hermitian matrix, also known as a self-adjoint matrix, is a complex square matrix that is equal to its own conjugate transpose. 
	In other words, a matrix $A$ is Hermitian if and only if $A^{\dagger} = A$, where $A^{\dagger}$ denotes the conjugate transpose of matrix $A$. 
	A Hermitian matrix is a square matrix $A$ that satisfies the following condition:
	$A^{\dagger} = A$
	In this context, $A^{\dagger}$ represents the conjugate transpose of matrix $A$. To understand this condition better, let's break it down into its elements. Suppose $A$ is a Hermitian matrix with elements $a_{ij}$, where $i$ and $j$ are row and column indices, respectively. The condition $A^{\dagger} = A$ implies that the elements of the matrix $A^{\dagger}$ are obtained by taking the complex conjugate of the elements of $A$ and then transposing the resulting matrix.
	Therefore, the elements of $A^{\dagger}$ are given by:
	$a_{ij} = (A^{\dagger})_{ij} = \overline{a_{ji}}$
	Here, $\overline{a_{ji}}$ represents the complex conjugate of the element $a_{ji}$ of matrix $A$. The Hermitian property ensures that the original matrix $A$ is equal to its conjugate transpose $A^{\dagger}$ with respect to all elements, i.e., $a_{ij} = (A^{\dagger})_{ij}$ for all $i$ and $j$.
	- Graphically,
	![[Pasted image 20230911025536.png|400]]
	- If $A$ is a real matrix, its adjoint is called the [[transpose]], denoted as $A^T$. 
	- If $A$ is also [[conjugate transpose]], then $A$ is called [[symmetric matrix]]


**Notation**:
There are two ways of expressing Hermitian matrix. $A^*$, or $A^\dagger$. 

**Key Properties:**

1. **Conjugate Transpose:** If $A$ is a Hermitian matrix, then its conjugate transpose $A^{\dagger}$ is equal to $A$. Mathematically, $(A^{\dagger})^{\dagger} = A$.

2. **Real Eigenvalues:** All eigenvalues of a Hermitian matrix are real numbers. This property is crucial in various applications, especially in quantum mechanics.

3. **Orthogonal Eigenvectors:** Eigenvectors corresponding to distinct eigenvalues of a Hermitian matrix are orthogonal to each other. This orthogonal property simplifies diagonalization and has important implications in quantum mechanics and signal processing.

4. **Diagonalization:** Hermitian matrices can be diagonalized by a unitary transformation. This means there exists a unitary matrix $U$ such that $A = UDU^{\dagger}$, where $D$ is a diagonal matrix containing the eigenvalues of $A$.

5. **Positive Definiteness:** Hermitian matrices have positive eigenvalues if and only if they are positive definite. This property is fundamental in optimization problems and the study of quadratic forms.

**Applications:**

1. **Quantum Mechanics:** Hermitian operators represent physical observables in quantum mechanics. The eigenvalues of these operators correspond to possible measurement outcomes, and the eigenvectors represent the states of the system.

2. **Signal Processing:** Hermitian matrices are used in various signal processing applications, such as spectral analysis and filtering. In these contexts, the Hermitian property ensures real-valued results.

3. **Statistics:** Hermitian matrices are employed in multivariate statistics, especially in techniques like Principal Component Analysis (PCA) and covariance matrix analysis.

4. **Optimization:** Hermitian matrices play a significant role in convex optimization problems, particularly in the formulation of quadratic optimization tasks.

Understanding Hermitian matrices and their properties is essential in various fields, especially in quantum mechanics and data analysis, where these matrices provide valuable insights and solutions to complex problems.