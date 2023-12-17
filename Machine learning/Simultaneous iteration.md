We start with $n$ linearly independent vectors as our guess of eigenvector of $A$: 
- $v_1^{(0)}, \dots, v_n^{(0)}$
- Consider the iteration $A^k v_1^{(0)}, \dots, A^k v_n^{(0)}$
- Under some assumptions, the space spanned by these vectors converges to the space spanned by $q_1, \dots, q_n$, where $q_1, \dots, q_n$ are the eigenvectors corresponding to the $n$ largest eigenvalues. 
- Putting the starting vectors into a matrix: $V^{(0)} = \begin{bmatrix} v_1^{(0)}, \dots, v_n^{(0)} \end{bmatrix}$ 
- Let $V^{(k)}$ be the result after $k$ iterations. We have $V^{(k)} = \begin{bmatrix} v_1^{(k)}, \dots, v_n^{(k)} \end{bmatrix}$ 
- So we will find an orthonormal basis for this space by a reduced QR factorization: $\hat Q^{(k)} \hat R^{(k)} = V^{(k)}$. 
- The columns of $\hat Q^{(k)}$ should converge to the eigenvectors $\pm q_1, \dots \pm q_n$. 

- Idea 2: Stability analysis:
	- $||q_j^{(k)} - \pm q_j|| = O(C^k)$, where where $C = \underset{1 \leq k \leq n}{max} | \frac{\lambda_{k+1}}{\lambda_k}| < 1$.

- The first n + 1 eigenvalues are distinct, that is, $|\lambda_1| > \dots > |\lambda_{n+1}|  \geq \lambda_{n+2}| \geq \dots \geq |\lambda_m|$ 
- All the leading principal submatrices of $\hat Q^T V^{(0)}$ are nonsingular.
- Let $q_j^{(k)}$ be the j-th column of $\hat Qˆ(k)$. Then $||q_j^{(k)} - \pm q_j|| = O(C^k)$. where $C = \underset{1 \leq k \leq n}{max} | \frac{\lambda_{k+1}}{\lambda_k}| < 1$.
s
![[Pasted image 20231113044409.png]]


---

Prove Simultaneous iterations are [[QR algorithm]]

In particular, $A^k = Q^{(k)}R^{(k)}$, $A^{(k)} = (Q^{(k)})^T A Q^{(k)}$ produced by the two processes are the same. 


