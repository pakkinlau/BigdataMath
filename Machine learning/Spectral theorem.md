Related:
- [[spectral decomposition]]
- [[Koopman spectral analysis]]

- Idea of "Spectrum" in the name of the theorem
	- "Spectrum" is a set of eigenvalues of a matrix. Which comes from the idea of the spectrum of light as a combination of pure things, our matrix is broken down into pure eigenvalues and eigenvectors. 
	- It is also called "principal axis theorem"  in geometry or in physics. It means if I look at the right axis, it becomes diagonal. The directions don't couple together. 

- Definition
	- (From Gilbert Strang's book) Every symmetric matrix has a factorization $S = Q\Lambda Q^T$ with real eigenvalues in $\Lambda$ and [[Orthogonal eigenvectors|orthonormal eigenvectors]] in the columns of $Q$. 
		- $Q$ is the matrix of orthonormal eigenvectors associated with [[symmetric matrix]] $S$. 
		- To find $Q$ and $\Lambda$, you perform an [[Eigenvalue Decomposition]] of the symmetric matrix $S$. 
	- While [[Eigenvalue Decomposition]], $A = X \Lambda X^{-1}$, the eigenvector matrix $X$ is not necessarily [[orthogonal matrix]], in spectral theorem $S = Q\Lambda Q^T$, the eigenvector matrix $Q$ is also carries the properties of [[orthonormal]] eigenvector matrix.

- Background (wiki): 
	- In linear algebra and functional analysis, spectral theorem is a result about when a linear operator or matrix can be diagonalized (that is, represented as a diagonal matrix in some basis). This is extremely useful because computations involving a diagonalizable matrix can often be reduced to much simpler computations involving the corresponding diagonal matrix. 
	- It is a theorem that is specifically applicable to [[hermitian matrix]] (or [[hermitian matrix|self-adjoint]]) matrices and real [[symmetric matrix]]. For non-Hermitian matrices, a similar diagonalization is not guaranteed through the spectral theorem. 

- Properties: 
	- Prove $S = Q\Lambda Q^T = Q\Lambda Q^{-1}$ 
	- 1. The eigenvectors of $S$ can be chosen orthogonal, for $S = X\Lambda X^{-1}$, the pair of $X$ and $X^{-1}$ could be expressed as $Q$ and $Q^T$. 
		- Proof:
			- The rough idea of this proof is, to manifest the symmetricity $A$ in dot product example. To equate $\langle Ax,y \rangle = \langle x,A^Ty \rangle$, Two scalars $\lambda$ and $\mu$ are involved. And $\lambda$ usually independent to $\mu$ because they are related to distinct variable $x$ and $y$. 
			- Recall $X$ is eigenvector matrix which $X = \begin{bmatrix} x_1, \dots, x_n \end{bmatrix}$
			- For distinct vectors (i.e. $x \neq y$) :
				- 1.  We are looking at the orthogonality between $x$ and $y$, so we do $\langle Ax,y \rangle = \langle x,A^Ty \rangle$, this formula works for all vectors $A$. 
				- 2. $\lambda \langle x,y \rangle = \langle \lambda x,y\rangle = \langle Ax,y \rangle = \langle Ax,y \rangle = \langle x,A^Ty \rangle = \langle x,Ay\rangle = \langle x, \mu y \rangle = \mu \langle x,y \rangle$
					- Only if $A$ is symmetric could pass $\langle x,A^Ty \rangle = \langle x,Ay\rangle$
					- Because $x$ and $y$ are distinct eigenvectors,  $(\lambda - \mu) \neq 0$, $\langle x,y \rangle = 0$, therefore $x \perp y$. 
			- For  $x = y$, $x$ is not perpendicular to $y$. 
	- 2. The eigenvectors of $S$ can be chosen orthonormal as well. 
		- Proof:
			- For $A = Q \Lambda Q^{-1}$, the lengths of eigenvectors are disposable. If we choose eigenvectors of length one. The multipliers would pass into $\Lambda$. 
			- QED.


**Key Ideas:**

1. **Self-Adjoint (Hermitian) Operators:** The Spectral Theorem primarily applies to self-adjoint operators, which are linear transformations on an inner product space that are equal to their adjoint (conjugate transpose). In real vector spaces, these operators are referred to as symmetric matrices, and in complex vector spaces, they are Hermitian matrices.

2. **Diagonalization:** One of the central results of the Spectral Theorem is that self-adjoint operators can be diagonalized. This means that they can be represented as a diagonal matrix concerning an appropriate orthonormal basis of the vector space. Diagonal matrices are particularly easy to work with, as they provide a clear understanding of the eigenvalues and eigenvectors of the operator.

3. [[Eigenvalues and eigenvectors]]: In the context of the Spectral Theorem, the eigenvalues of a self-adjoint operator represent observable quantities or measurements in various applications. These eigenvalues correspond to the possible outcomes of measurements, and the associated eigenvectors represent the states or configurations in which these measurements yield the corresponding eigenvalues.

4. [[diagonalization]]: The Spectral Theorem goes beyond the diagonalization of self-adjoint operators; it guarantees an orthogonal diagonalization. This means that the basis of eigenvectors that diagonalize the operator is orthogonal, which simplifies computations and has important geometric implications.

5. **[[Projection]] Operators:** The Spectral Theorem enables us to express a self-adjoint operator as a sum of projection operators onto the eigenspaces associated with its eigenvalues. These projection operators are idempotent (applying them twice doesn't change the result) and play a significant role in various applications, including quantum mechanics.

**Applications:**

1. **Quantum Mechanics:** In quantum mechanics, the Spectral Theorem is crucial for understanding the measurable quantities (observables) of quantum systems. Self-adjoint operators correspond to observables, and their eigenvalues represent possible measurement outcomes.

2. **Signal Processing:** The Spectral Theorem is applied in signal processing to analyze and manipulate signals using techniques like Fourier analysis and the discrete cosine transform (DCT).

3. **Statistics:** In statistics, the Spectral Theorem is used in principal component analysis (PCA) to find the orthogonal eigenvectors and eigenvalues of a covariance matrix, reducing the dimensionality of data while preserving its variability.

4. **Differential Equations:** The Spectral Theorem is employed in solving partial differential equations, particularly in the separation of variables technique, where it simplifies the problem by diagonalizing operators.