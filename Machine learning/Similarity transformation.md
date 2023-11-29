---
alias: similar
---

$A \mapsto X^{-1}AX$

- Idea 1: Similar matrix
	- $A$ and $B$ are similar if there is a nonsingular $X$ such that $B = X^{-1}AX$. That is, they are similarity transformation of each other. 
	- Note that $A$ and $B$ is not necessarily exactly the same matrix.
- Idea 2: Properties of similar matrices:
	- 1. Same rank:
		- In $A \mapsto X^{-1}AX$, $X$ is invertible means it is full-rank. So it does not change the dimensionality of the space spanned by $A$. Therefore, rank of the matrix does not change under similarity transformation. 
	- 2. Same determinant, eigenvalues, same characteristic polynomial:
		- It came from the theorem we proved below: $p_{X^{-1}AX}(z) = p_A(z)$. 
	- More possible properties but we don't discuss further. 

---

Theorem: 
- If $X$ is nonsingular, then $A$ and $X^{-1}AX$ have the same characteristic polynomial, eigenvalues and algebraic and geometric multiplicities. 
- $A$ and $X^{-1}AX$ have the same [[characteristic polynomial]], $p_A(\lambda) = p_B(\lambda)$. 


Proof:
$$\begin{align*}
    p_{X^{-1}A X}(z) & = \text{det}(z \mathbb{I}-X^{-1}A X) \\
                     & = \text{det}(X^{-1}(z \mathbb{I}-A)X) \\
                     & = \text{det}(X^{-1})\,\text{det}(z \mathbb{I}-A)\text{det}(X) \\
                     & = \text{det}(z \mathbb{I}-A) \\
                     & = p_{A}(z).
\end{align*}$$
	- In the second step, we had $zI = zX^{-1}IX$, so that we can factor out $X^{-1}$. We only can do such thing when there is scalar times identity matrix $I$. 
	- In the third step, we had $det(AB) = det(A)det(B)$, which is a fundamental property of determinant of a product of matrices. 
	- In the fourth step, we had $det(X)det(X^{-1}) = 1$. Determinants are scalar so we can change their positions. 


