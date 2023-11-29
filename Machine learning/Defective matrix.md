1/11/2023

- Definition
	- An [[eigenvalues]] whose [[algebraic multiplicity]] is larger than its [[geometric multiplicity]] is a defective eigenvalue. 
	- A matrix that has one or more defective eigenvalues is a defective matrix

- Discussion on why Defective matrix appears 
	- When you use SVD, you are using 2 different basis.
	- When you are doing [[Eigenvalue Decomposition]]. The problem of using one basis is, when you have a defective matrix, you actually can't provide an eigen-decomposition of this form. 
	

---
Example of defective matrix 

Say $A = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2  \end{bmatrix}$
- Then $\lambda = 2$ and its algebraic multiplicity is 3.
- With $Ax = \lambda x$, $e_1, e_2, e_3 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$
- It has degeneracy there, 3 eigenvalues, but each eigenvalue has a different direction. So the geometric multiplicity is 3, and each direction in some sense is independent of the others. 

Another example, 

Say $A = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2  \end{bmatrix}$
- In this case, $\lambda = 2$, and its algebraic multiplicity is 3. 
- But this time the geometric multiplicity is 1. 
	- It is because when you solve for eigenvectors, there is only one linearly independent eigenvector corresponding to this eigenvalue 


Defective matrix. 
- When algebraic multiplicity is not equal to geometric multiplicity, it is called "defective" matrix.

