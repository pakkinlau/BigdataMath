- Idea 1: Schur factorization produce a self-similarity transformation to a matrix which has better representation, and easier to compute the eigenvalues on.
	- What is "self-similarity transformation?"
		- Related: [[Similarity transformation|similar]]
		- It refer to the process of transforming a matrix into a triangular form that retains certain inherent properties of the original matrix, thus exhibiting a form of similarity to itself.
- Idea 2: Schur factorization is seen as a fundamental steps of all algorithms that solves [[Eigenvalue problems]]. There are six reasons.
	- 1. Reduced form
	- 2. Eigenvalue identifications
	- 3. Convergence acceleration
	- 4. Numerical stability
	- 5. Blocking strategies
	- 6. Preconditioning
- Idea 3: Schur factorization is a loosely defined than eigenvalue decomposition.
	- Definition of Schur factorization: $A = QTQ^*$, and eigenvalue decomposition we had $A = X \Lambda X^{-1}$
		- Notations:
			- Where $Q$ is unitary and $T$ is upper-triangular in Schur factorization.
			- The eigenvalues are on the diagonal of $\Lambda$ of eigenvalue decomposition. 
		- Comparison:
			- When $\Lambda$ is diagonal, $T$ is upper triangular. 
			- We don't need to compute inverses of basis matrices $Q$ in Schur factorization. 
- Idea 4: Schur factorization is not exactly the same of [[spectral decomposition]]


Schur factorization in the framework of [[Eigenvalue problems]]:
- Step 1: Schur factorization
- Step 2: Iterate to find eigenvalues





$T$ in Schur factorization is advantageous for finding eigenvalues and eigenvectors. 
- $A = QTQ^*$
	- Once we got this form, we take $T$ matrix, and find an iterative procedure to go find the eigenvalues and eigenvectors. 


What if $A$ is Hermitian?
- If $A$ is Hermitian, then $T$ is also Hermitian. The only way $T$ obtain triangular matrix is to be diagonal matrix. 

What if $A$ has all equal eigenvalues?
- We can write $A$ as similar


How to obtain $T$?
- Similar to LU decomposition, we make elements below diagonal become zero. 
- We try to multiply a series of matrices onto $A$ to get $T$: 
	- $Q_j^* Q_{j-1}^* \dots Q_2^* Q_1^* A Q_1 Q_2 \cdots Q_j = T$
- To achieve this, we have [[Reduction to Hessenberg form]]. 

---

- Theorem: Every square matrix $A$ has a Schur factorization.
