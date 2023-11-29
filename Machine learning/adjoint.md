---
alias: hermitian transpose, adjoint matrix, hermitian transpose, jermitian conjugate, adjugate
---

- In [[Determinant]]
	For a square matrix $A$ of order $n \times n$, the adjoint (also known as the adjugate) matrix, denoted as $\text{adj}(A)$ or $\text{adjoint}(A)$, is a matrix whose elements are the determinants of the minors of matrix $A$, transposed appropriately. Here's how you compute the adjoint matrix for an $n \times n$ matrix:
	
	1. **Minors:** For each element $a_{ij}$ in $A$, where $i$ and $j$ are the row and column indices, respectively, find the minor matrix $M_{ij}$ by removing the $i$th row and $j$th column from $A$.
	
	2. **Determinants:** Calculate the determinant $\text{det}(M_{ij})$ for each minor matrix $M_{ij}$.
	
	3. **Signs:** Assign signs to the determinants based on the indices $i$ and $j$. The rule is $(-1)^{i+j}$. That is, if the sum of the row index $i$ and the column index $j$ is even, the sign is positive; if it's odd, the sign is negative.
	
	4. **Transpose:** Place these determinants in the transpose positions of the original matrix $A$.
	
	To illustrate, consider a 3x3 matrix:
	$$
	A = \begin{bmatrix}
	a_{11} & a_{12} & a_{13} \\
	a_{21} & a_{22} & a_{23} \\
	a_{31} & a_{32} & a_{33} \\
	\end{bmatrix}
	$$
	
	The elements of the adjoint matrix $\text{adj}(A)$ would be calculated as follows:
	$$
	\text{adj}(A) = \begin{bmatrix}
	\text{det}(M_{11}) & -\text{det}(M_{21}) & \text{det}(M_{31}) \\
	-\text{det}(M_{12}) & \text{det}(M_{22}) & -\text{det}(M_{32}) \\
	\text{det}(M_{13}) & -\text{det}(M_{23}) & \text{det}(M_{33}) \\
	\end{bmatrix}
	$$
	
	Where each $M_{ij}$ is a 2x2 minor matrix obtained by removing the $i$th row and $j$th column from matrix $A$.
	
	This process generalizes for square matrices of any size $n \times n$. The adjoint matrix is especially useful in finding the inverse of a matrix using the formula $A^{-1} = \frac{1}{\text{det}(A)} \times \text{adj}(A)$ (if $\text{det}(A)$ is non-zero

---
- In [[complex vector]]
	- While [[conjugate transpose]] is describing vectors, adjoint appears when we are dealing with complex [[Matrix-Vector Multiplication]]. 
		- Say we take inner product of $Au$ with $v$, we have $(Au)^Hv = \bar{Au}^Tv ={\bar u}^T{\bar A}^T v =u^H(A^Hv)$.
		- To be short, $(Au)^Hv = \bar{Au}^Tv ={\bar u}^T{\bar A}^T v =u^H(A^Hv)$
		- And Adjoint matrix is $A^H$. And $A^H = \bar A^T$. 
	- Two kind of matrix is actually describing the same thing: 
		- [[conjugate transpose|conjugate transpose matrix]] = [[adjoint|adjoint matrix]]
	- The hermitian conjugate / adjoint of $A \in C^{m \times n}$, denoted as $A^*$ is the $n \times m$ matrix: $a_{ij}^* = \bar a_{ji}$
	- Graphically,
	![[Pasted image 20230911025536.png|400]]
	- If $A$ is a real matrix, its adjoint is called the [[transpose]], denoted as $A^T$. 
	- If $A$ is also [[conjugate transpose]], then $A$ is called [[symmetric matrix]]

---
- Show two definition are equivalent:
	Certainly, let's establish the equivalence between the two definitions. The first definition I provided, which is also known as the adjoint or conjugate transpose, is denoted as $A^*$ or $A^\dagger$. The second definition you provided is the adjugate matrix, often denoted as $\text{adj}(A)$. Let's denote the adjugate matrix as $B = \text{adj}(A)$. The relationship between these two definitions can be expressed as follows:
	
	1. **First Definition (Conjugate Transpose):**
	$A^* = [(\overline{a_{ji}})]$
	
	2. **Second Definition (Adjugate Matrix):**
	$$B = \begin{bmatrix}
		\text{det}(M_{11}) & -\text{det}(M_{21}) & \text{det}(M_{31}) \\
		-\text{det}(M_{12}) & \text{det}(M_{22}) & -\text{det}(M_{32}) \\
		\text{det}(M_{13}) & -\text{det}(M_{23}) & \text{det}(M_{33}) \\
		\end{bmatrix}
	$$
	
	Now, let's examine whether these two definitions are equivalent. The elements of the matrix $B$ are determinants of submatrices of $A$, and the complex conjugate of $a_{ji}$ from $A$ corresponds to these determinants.
	
	In the context of complex numbers, the determinant of a 1x1 matrix (a single complex number) is the number itself. Therefore, $\text{det}(M_{ij}) = \overline{a_{ij}}$.
	
	By comparing the definitions, it's clear that the elements of the adjugate matrix $B$ are the complex conjugates of the corresponding elements of the matrix $A^*$. Therefore, the two definitions are indeed equivalent, as they represent the same operation of taking the complex conjugate of elements in different ways: one directly in the matrix ($A^*$) and the other in the adjugate matrix ($B$).

---

**Properties:**

1. **[[conjugate transpose]] Property:** In the context of complex numbers and matrices, if A is a matrix with complex entries, the adjoint matrix is often referred to as the "Hermitian transpose." It satisfies the property A^* = A, i.e., the adjoint of A is equal to its conjugate transpose.

2. **[[Orthogonal vector]]:** If A is a square matrix with real or complex entries and is invertible, then A^*A = AA^* = I, where I is the identity matrix. This property is essential in solving systems of linear equations and is linked to the concept of orthogonality in linear algebra.

3. **[[Determinant]] Relation:** The determinant of the adjoint matrix is related to the determinant of the original matrix A. Specifically, det(adj(A)) = (det(A))^(n-1), where n is the size of the square matrix A.

4. **[[Eigenvalues and Eigenvectors]]:** The eigenvalues and eigenvectors of A and its adjoint A^* share many properties. In particular, they have the same eigenvalues, and if A is a Hermitian matrix (A = A^*), its eigenvectors are orthogonal.

**Importance:**

1. **Solving Linear Systems:** The adjoint matrix is crucial in solving systems of linear equations using techniques like the Cramer's rule, especially when dealing with complex numbers and square matrices.

2. **Orthogonal Matrices:** In the context of orthogonal matrices, which play a vital role in applications like rotations and transformations, the adjoint matrix is used to determine if a matrix is orthogonal.

3. **Hermitian Matrices:** Hermitian matrices, which have real eigenvalues and orthogonal eigenvectors, find applications in quantum mechanics, signal processing, and more. The adjoint matrix is employed to identify and analyze these matrices.

4. **Determinants and Inverses:** The properties of adjoint matrices provide insights into the determinants and inverses of matrices, simplifying various calculations and proofs in linear algebra.

In conclusion, the adjoint matrix is a fundamental concept in linear algebra with significant applications in various mathematical and scientific fields. Its properties and relationships with other matrix operations make it a valuable tool for solving equations, analyzing transformations, and understanding the properties of square matrices.