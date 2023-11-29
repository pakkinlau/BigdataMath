



---
Theorem:


Theorem: Consider the iteration defined in the previous page. Assume that 

1. The first n + 1 eigenvalues are distinct, that is,

$|\lambda_1| > \dots > |\lambda_{n+1}|  \geq \lambda_{n+2}| \geq \dots \geq |\lambda_m|$ 
2. All the leading principal submatrices of $\hat Q^T V^{(0)}$ are nonsingular.

Let $q_j^{(k)}$ be the j-th column of $\hat Qˆ(k)$. Then


$||q_j^{(k)} - \pm q_j|| = O(C^k)$. 

where $C = \underset{1 \leq k \leq n}{max} | \frac{\lambda_{k+1}}{\lambda_k}| < 1$.

![[Pasted image 20231113044409.png]]


---

Prove Simultaneous iterations are [[QR algorithm]]

In particular, $A^k = Q^{(k)}R^{(k)}$, $A^{(k)} = (Q^{(k)})^T A Q^{(k)}$ produced by the two processes are the same. 


