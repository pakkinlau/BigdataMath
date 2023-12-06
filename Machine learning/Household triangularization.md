
---
## Orthogonal triangularization

In [[Modified Gram-Schmidt iteration]] and [[Triangular orthogonalization]], we have $AR_1 R_2 \dots R_n = \hat Q$ or $A \hat R^{-1} = \hat Q$. We applied a set of triangular matrices to orthogonalize our matrix $A$. 

On the other hand, the Householder applies a succession of [[unitary matrices]] $Q_k$ on the left of $A$, such that $Q_n \dots Q_2 Q_1 A = R$, or $Q^* A = R$, so that the result is upper triangular. 

The product $Q = Q_1^* \dots Q_n^*$ is also unitary. 

Hence, $A = QR$ is the required QR factorization. So, we call this orthogonal triangularization. 

---
Input: Any matrix $A$

Output: upper triangular matrix $R$

We want to obtain an unitary matrix $Q_k$ such that $Q_k$ could turns the $k$th column of $A$ to be zero except the first $k$th row element remain unchanged. 
![[Pasted image 20231112181026.png]]

In general, the matrix $Q_k$ is defined to make the entries below the $k$th diagonal element zero, and it does not change the first $k-1$ columns. 


---
## Construction of $Q_k$

- Recall the matrix $Q_k$ is defined to make the entries below the $k$th diagonal element zero, and it does not change the first $k-1$ columns.  '
- So $Q_k$ is chosen to have the form $\begin{pmatrix} I & 0 \\ 0 & F\end{pmatrix}$, 
	- where $I$ is the $(k-1) \times (k-1)$ identity matrix, 
	- where $F$ is an $(m - k + 1) \times (m - k + 1)$ unitary matrix. 
- A requirement for $F$ is that it will create zero below the $k^{th}$ diagonal element. 
- The matrix $F$ will be chosen as the [[Householder reflector]]

---
- So, in the basic form, $Q_k$ is transforming the first column of $A$, and making $m-k$ element in column $k$ to be zero. 
- But when we convert matrix into upper Hessenberg matrix, we will use Householder reflector to make tri-diagonal matrix in the upper part of the matrix. How it works?

