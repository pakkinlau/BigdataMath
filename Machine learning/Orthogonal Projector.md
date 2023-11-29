*Definition:*
- An orthogonal projector $P$ projects vectors from subspace $S_1$ along subspace $S_2$, where $S_1$ and $S_2$ are orthogonal subspaces
- Formally, projectors are classified as orthogonal projectors if it satisfies $\langle Px, y \rangle = \langle Px, Py \rangle = \langle x, Py \rangle$, for all $x, y \in V$.  (referred to Wikipedia)
- Warning: Orthogonal projectors are not orthogonal matrices. 


*Theorem:*
- A projector $P$ is orthogonal if and only if it is Hermitian ($P = P^*$).
	*Proof:*
	*a. $P = P^*$*
	Assuming $P = P^*$, where $P$ projects $\mathbb{C}^m$ onto $S_1 = \text{range}(P)$ along $S_2 = \text{null}(P) = \text{range}(I - P)$:
	- Let $s_1 \in S_1$ and $s_2 \in S_2$. Then $s_1 = Px$ and $s_2 = (I - P)y$.
	- $s_1^* s_2 = (Px)^* (I - P)y = x^*P^* (I - P)y = x^*(P - P^2)y$ (since $P$ is Hermitian) $= x^*(P - P)y = 0$.
	- Thus, $S_1$ and $S_2$ are orthogonal when $P = P^*$.
	*b. $P$ is Orthogonal*
	Assuming $P$ is orthogonal, projecting onto $S_1$ along $S_2$ where $S_1 \perp S_2$:
	- Let $\{q_1, q_2, \dots, q_m\}$ be an orthonormal basis for $\mathbb{C}^m$, with $\{q_1, q_2, \dots, q_n\}$ as the basis for $S_1$ and $\{q_{n+1}, \dots, q_m\}$ as the basis for $S_2$.
	- For $j \leq n$, $Pq_j = q_j$. For $j > n$, $Pq_j = 0$.
	- Let $Q$ be the unitary matrix with columns $q_j$. $PQ = \begin{bmatrix} q_1, \dots, q_n, 0, \dots \end{bmatrix}$.
	- $Q^*PQ$ is a square singular value matrix with its first $n$ diagonal elements as $1$ (since $q_k^*q_k = 1$) and the rest $0$.
	- Rearranging, $P = Q\Sigma Q^*$.
	- Taking the conjugate transpose of $P$, $P^* = (Q\Sigma Q^*)^* = Q \Sigma Q^* = P$.

---
## Observations:

- Projectors sometimes are reducing [[dimension]] of data, sometimes it is not reducing [[dimension]] of data. 
	- Say $P$ is a $m \times n$ matrix 
	- Suppose $S_1 \perp S_2$, where $S_1$ has dimension $n$, which represents the [[column space|range]] of $P$. 
	- Let $\{ q_1, q_2, \dots, q_m \}$ be an [[orthonormal]] basis for $\mathbb{C}^m$, where $\{ q_1, \}$

- We can also describe $P = \hat Q \Sigma \hat Q^*$ 
	- It is based on the [[Singular value decomposition|SVD]] of $P$. 

- How to determine orthogonal projector?
	- $P = \hat Q \Sigma \hat Q^*$ 
	- We can determine $\hat Q$ by considering the orthonormal basis for $range(A)$. So we take independent columns from $A$ and normalize each column to obtain $\hat Q$. 
	- We take conjugate transpose $\hat Q$ to obtain $\hat Q^*$
	- We obtain $P$

- Figure: p.54 pf numerical linear algebra textbook
![[Pasted image 20231025172939.png]]


---
- Properties:
	- 1. The effect of dimensionality reduction depends on the dimension of subspace.
		- The dimension of subspace within the range of a projector $P$ can be determined by finding the rank of the projector. 

- Observations:
	- 1. Proving a claim: If an orthogonal projector is not identity matrix, it reduce the dimension of the data. 
	- Written in 24/10/2023
		- 