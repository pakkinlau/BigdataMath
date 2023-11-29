
- Q: why we call it eigenvalue problems, instead of eigenvectors problem?
	- It is always first finding eigenvalues, then solve the eigenvectors. That is why we call them "eigenvalue problems"
		- 1. For a given linear transformation, the eigenvalues are unique and give us important information about the transformation. 
		- 2. Once we have eigenvalues, we can fine the eigenvectors by substituting each eigenvalue back into $Ax = \lambda x$. 
- Characteristic equation 
	- To find eigenvalues, we solve the characteristic equation $det(A - \lambda I) = 0$ where the roots of this equation are the eigenvalues. 
	- Related: [[characteristic polynomial]]

In [[Eigenvalue Decomposition]]: 
- From $Ax = \lambda x$, we got $A X = X \Lambda$
- With $AX = X \Lambda$, we have $A = X \Lambda X^{-1}$
- $Ax = b$ becomes $X \Lambda X^{-1} x = b$. 
- We rewrite it as $\Lambda X^{-1} x = X^{-1} b$. and we introduce new variable $X^{-1} x = \tilde X$ and $X^{-1}b = \tilde b$, then we have $\Lambda \tilde x = \tilde b$, which is trivial to solve in row-by-row, in $O(m)$ operations. And that is the power of diagonalization. In physics, usually the problem is about turning the coordinate systems to diagonal direction. 

Similarly, in [[Singular value decomposition|SVD]], say $Ax = b$ and $A$ is not square matrix. 
- $U \Sigma V^* x = b$
- $\Sigma V^* x = U^* b$
- We rewrite $V^*x = \tilde X$, and $U^*b = \tilde b$, we have $\Sigma \tilde x = \tilde b$.
- So we also turn the problem into diagonalized version. Which we just need $O(m)$ operations to compute the solution. 