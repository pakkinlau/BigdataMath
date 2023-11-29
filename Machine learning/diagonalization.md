---
alias: diagonalizable, diagonalize
---

- subset:
	- [[unitarily diagonalization]]

- Theorem:
	- An $m \times m$ matrix $A$ is non-defective if and only if it has an eigenvalue decomposition $A = X \Lambda X^{-1}$

---
### diagonalizable

---

- Criteria of determining diagonalizability of a matrix:
    - 1. The matrix $A$ must be a [[square matrix]]. Only square matrices are eligible for diagonalization.
    - 2. A matrix is diagonalizable if, and only if, it is similar to a diagonal matrix $\Lambda$. This means there exists an invertible matrix $P$ (composed of the eigenvectors of $A$) such that $P^{-1}AP = \Lambda$. 
        - **Matrix A**: The original square matrix.
        - **Matrix P**: An invertible matrix whose columns are the eigenvectors of $A$.
        - **Matrix $\Lambda$**: A diagonal matrix whose entries are the eigenvalues of $A$.
            - $\Lambda = \begin{bmatrix}d_1 & 0 &0 & \dots & 0 \\ 0 & d_2 & 0 & \dots & 0 \\ 0 & 0 & d_3 & \dots & 0 \\ 0 & 0 & 0 & \dots & d_n  \end{bmatrix}$, where $d_1, d_2, d_3, \dots, d_n$ are the eigenvalues of the original matrix $A$. These values are typically arranged in ascending or descending order. 
            - Q: How to check there is an invertible matrix $P$ for any matrix $A$ in general?
            - A: Determine if there are as many linearly independent eigenvectors as the dimension of $A$. The ways of determining eigenvectors set is discussed in [[characteristic polynomial]] section. 
    - 3. The [[geometric multiplicity]] of each eigenvalue must equal its [[algebraic multiplicity]] for matrix $A$. 
        - This requirement stems from the need to have a complete set of eigenvectors to form matrix $P$ (complete dimensionality of [[eigenspace]]. 
        - When the algebraic multiplicity of an eigenvalue (its multiplicity as a root of the characteristic polynomial) exceeds its geometric multiplicity (the dimension of the corresponding eigenspace), there are not enough independent eigenvectors available to form a basis for the eigenspace. This leads to the impossibility of constructing a full-rank matrix $P$, hence preventing diagonalization.
        - Quick check on point 3:
            - Case 1: Matrix with zero columns 
                - It implies that there will be free variables when solving for the eigenvectors, which can lead the insufficiency of independent eigenvectors to form a complete basis for diagonalization.


---
- Criteria of determining diagonalizability of a matrix:
	- 1. The matrix $A$ have to be a [[square matrix]]
	- 2. A matrix is diagonalizable if it is similar to a diagonal matrix $\Lambda$. 
		- If we expand it, it means the $A$ is diagonalizable if there exists an [[invert|invertible]] eigenvector matrix $X$ and a [[diagonal matrix]] $\Lambda$ such that: $X^{-1}AX = \Lambda$
	   - **Matrix A**: The original square matrix.
	   - **Matrix P**: An [[invert|invertible]] matrix composed of eigenvectors of A.
	   - **Matrix $\Lambda$**: A diagonal matrix containing eigenvalues of A.
		   - $\Lambda = \begin{bmatrix}d_1 & 0 &0 & \dots & 0 \\ 0 & d_2 & 0 & \dots & 0 \\ 0 & 0 & d_3 & \dots & 0 \\ 0 & 0 & 0 & \dots & d_n  \end{bmatrix}$, the $d_1, d_2, d_3, \dots, d_n$ values are the eigenvalues of the original matrix $A$ and are typically arranged in ascending or descending order. 
   - 3. The [[geometric multiplicity]] should be equal to [[algebraic multiplicity]] of a matrix $A$. 
	   - This concept is related to the dimensionality of [[eigenspace]].
	   - while invertibility concerns eigenvalues, diagonalibility concerns with the eigenvectors. $P$ is a matrix composed of eigenvectors, thus $A$ need to have $m$ independent eigenvector to span the entire space. 
	   - Quick check on point 3:
		   - Cases 1: Matrix with zero columns 
			   - When computing for eigenvector, we deal with the matrix $A - \lambda I$. If there are any columns filled with zeros, it implies that there will be free variables when solving for eigenvectors. 
		   - The algebraic multiplicity is greater than geometric multiplicity, leading to insufficient of eigenvectors to form a complete basis for diagonalization. 

- [[unitary diagonalizable]]


2. **[[Eigenvalues and Eigenvectors]]**:

- Multiplying $P$ on the both sides on the previous equation $P^{-1}AP = D$, we have $AP = PD$. 

   Eigenvalues (λ) and eigenvectors (v) of matrix A are defined as follows:

   - An eigenvalue λ of A is a scalar such that there exists a nonzero vector v, known as the eigenvector, satisfying the equation:

     \[Av = λv\]

---

- Diagonalization:
	- Suppose the $n$ by $n$ matrix $A$ has $n$ linearly indepedent eigenvectors $x_1, \dots, x_n$. Put them into the columns of an eigenvector matrix $X$. Then $X^{-1}AX$ is the eigenvalue matrix $\Lambda$. 
	- $X^{-1}AX = \Lambda = \begin{bmatrix} \lambda_1 & & \\ & \ddots & \\ & & \lambda_n \end{bmatrix}$
		- This stems from $AX = X \Lambda$
		- Proof:
			- $AX = A \begin{bmatrix} x_1, \dots, x_n \end{bmatrix}$
			- = $\begin{bmatrix} \lambda_1 x_1, \dots, \lambda_n x_n \end{bmatrix}$ (Since $Ax = \lambda x$)
			- = $\begin{bmatrix} x_1, \dots, x_n\end{bmatrix} \begin{bmatrix} \lambda_1 & & \\ & \ddots & \\ & & \lambda_n \end{bmatrix}$
			- $= X \Lambda$  

---

**Significance of Diagonalizability**:

Diagonalizability is significant for several reasons:

- **Simplification**: Diagonal matrices are easy to work with, and many matrix operations become simpler when dealing with diagonalized matrices.
	- It allow us to easier to compute powers of the matrix. 
	- Such as $A^k = X \Lambda^k X^{-1}$ 

- **Eigenvalues and Eigenvectors**: Diagonalization allows us to easily find eigenvalues and eigenvectors of a matrix, which are crucial in various mathematical and scientific applications.

- **Analyzing Linear Transformations**: Diagonalizability provides insight into the behavior of linear transformations represented by matrices. It allows us to understand how a transformation stretches or compresses space along its eigenvectors.

---


**Conditions for Diagonalizability**:

A matrix A is diagonalizable if and only if it meets the following conditions:

1. **Algebraic Multiplicity Equals Geometric Multiplicity**:

   For each eigenvalue λ of A, its algebraic multiplicity (the number of times it appears as a root of the characteristic polynomial of A) must be equal to its geometric multiplicity (the number of linearly independent eigenvectors associated with it).

2. **Full Set of Linearly Independent Eigenvectors**:

   There must be a sufficient number of linearly independent eigenvectors to form the matrix P. In other words, the eigenvectors must span the vector space.

3. **P is Invertible**:

   The matrix P formed by the eigenvectors of A must be invertible.

---


**Applications of Diagonalizability**:

Diagonalizability finds applications in various fields, including physics, engineering, and computer science:

- **Quantum Mechanics**: Diagonalization is used to simplify the Schrödinger equation and find energy eigenvalues in quantum mechanics.

- **Control Theory**: In control systems engineering, diagonalization helps analyze the stability and behavior of dynamic systems.

- **Data Compression**: In data science, diagonalization is employed in techniques like Principal Component Analysis (PCA) for dimensionality reduction and data compression.

- **Graph Theory**: Diagonalization of adjacency matrices is used to study the properties of graphs and networks.

In summary, diagonalizability is a crucial concept in linear algebra, with well-defined formal definitions, that enables us to simplify matrices, analyze linear transformations, and extract valuable information about their eigenvalues and eigenvectors. It has widespread applications in various fields, making it an essential topic for anyone studying mathematics or related disciplines.



---
### Diagonalization

Diagonalization is a fundamental concept in linear algebra that plays a crucial role in various mathematical and practical applications. It involves transforming a [[square matrix]] into a diagonal matrix.
- That is the process of creating [[diagonal matrix]]


1. **[[Eigenvalues and Eigenvectors]]**: Diagonalization relies on the properties of eigenvalues and eigenvectors. An eigenvalue (λ) of a square matrix A is a scalar that represents the scaling factor of an eigenvector (v) when A is applied to it, i.e., Av = λv. Eigenvectors associated with different eigenvalues are linearly independent.

2. **[[Diagonal Matrix]]**: The main goal of diagonalization is to express a given square matrix A as a product of three matrices: P, D, and P^(-1), where D is a diagonal matrix containing the eigenvalues of A, and P is a matrix whose columns are the corresponding eigenvectors. The diagonal matrix D allows for straightforward computation of powers of A.

3. **Conditions for Diagonalization**:
   - A square matrix A is diagonalizable if and only if it has n linearly independent eigenvectors, where n is the size of the matrix.
   - A matrix with distinct eigenvalues is always diagonalizable.
   - In some cases, even if A is not diagonalizable, it can be brought to a similar form using a Jordan decomposition.

4. **Applications**:
   - **Solving Linear Systems**: Diagonalization simplifies the computation of A^n, making it easier to find solutions to linear systems of the form x(t+1) = Ax(t).
   - **Stability Analysis**: In dynamical systems and control theory, diagonalization helps analyze the stability of linear systems.
   - **Quantum Mechanics**: Diagonalization is essential in quantum mechanics for finding the energy eigenstates and corresponding eigenvalues of Hamiltonian operators.
   - **Principal Component Analysis (PCA)**: In data analysis and machine learning, PCA uses diagonalization to find the principal components of a dataset.

5. **Procedure for Diagonalization**:
   - Find the eigenvalues of the matrix A by solving the characteristic equation det(A - λI) = 0, where I is the identity matrix.
   - For each eigenvalue, find its corresponding eigenvector(s) by solving the equation (A - λI)v = 0.
   - Construct the matrix P using the eigenvectors as columns.
   - Construct the diagonal matrix D with the eigenvalues on the main diagonal.
   - If P is invertible, then A can be diagonalized as A = PDP^(-1).

6. **Non-Diagonalizable Matrices**: Some matrices cannot be diagonalized, particularly those with repeated eigenvalues that lack a sufficient number of linearly independent eigenvectors. In such cases, a Jordan decomposition can be used to obtain a similar but not diagonal form.

In summary, diagonalization is a powerful technique in linear algebra that simplifies the analysis of square matrices by transforming them into a diagonal form through eigenvectors and eigenvalues. This process finds applications in various fields and is a crucial tool for understanding linear systems and solving related problems.