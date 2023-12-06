
It is a of a type of [[Triangular orthogonalization]]. 

Vector normalization: - $q_j = \frac{v_i}{||v_i||}$

In modified Gram-Schmidt, we use the following to establish:
- $v_j = P_j a_j$
- $P_1 = I$ 
- $P_j = I - Q_{j-1} Q_{j-1}^*$, where $Q_{j-1}$ is $m \times (j-1)$ matrix containing the first $j-1$ columns of $Q$.
	- Related: 
		- [projection operator (QQT)](projection%20operator%20(QQT).md)
		- [outer product](outer%20product.md)

How we have: 
- $P_j = P_{\perp q_{j-1}} \dots P_{\perp q_2} P_{\perp q_1}$ from above formulas 

### To see how this chain projection formula stands: 

We can derive the equation using induction. The base case ($j=1$) is trivial because $P_1 = I$ by definition and there are no $q_k$ vectors to project onto yet, so the equation holds.

Assume it holds for $P_j = P_{\perp q_{j-1}} \dots P_{\perp q_2} P_{\perp q_1}$ for some $j>1$.

Now consider $P_{j+1} = I - Q_j Q_j^*$, where $Q_j$ is the $m \times j$ matrix containing the first $j$ columns of $Q$. We can write $Q_j$ as $[Q_{j-1}, q_j]$, where $Q_{j-1}$ is the $m \times (j-1)$ matrix containing the first $j-1$ columns of $Q$ and $q_j$ is the $j$-th column vector. 

Then, $Q_j Q_j^* = [Q_{j-1}, q_j] [Q_{j-1}, q_j]^* = Q_{j-1} Q_{j-1}^* + q_j q_j^*$.

Substituting into $P_{j+1} = I - Q_j Q_j^*$, we get $P_{j+1} = I - (Q_{j-1} Q_{j-1}^* + q_j q_j^*) = (I - Q_{j-1} Q_{j-1}^*) - q_j q_j^* = P_j - q_j q_j^*$.

Since $q_j$ is orthogonal to the subspace spanned by $Q_{j-1}$ (by the definition of the Gram-Schmidt process), $q_j q_j^*$ can be thought of as a projection onto the orthogonal complement of $q_j$, so $P_{j+1} = P_j P_{\perp q_j}$. 

Substituting the induction assumption $P_j = P_{\perp q_{j-1}} \dots P_{\perp q_2} P_{\perp q_1}$, we get $P_{j+1} = P_{\perp q_{j-1}} \dots P_{\perp q_2} P_{\perp q_1} P_{\perp q_j}$, completing the induction step.

So, by induction, we have $P_j = P_{\perp q_{j-1}} \dots P_{\perp q_2} P_{\perp q_1}$ for all $j$.

---

- We need to compute $v_j = P_{\perp_{q_{j-1}}} \dots P_{\perp_{q_{2}}} P_{\perp_{q_{1}}} a_j$. 
	- $v_j^{(1)} = a_j$
	- $v_j = v_j^{(j)} = P_{\perp_{q_{j-1}}} v_j^{(j-1)} = v_j^{(j-1)} - q_1 q_1^*v_j^{(1)}$
	- This is the modified Gram-Schmidt iteration.

---
## Gram-Schmidt as [[Triangular orthogonalization]]

Each outer step of the [[Modified Gram-Schmidt iteration]] can be interpreted as a right-multiplication by a squared upper-triangular matrix.

$\begin{bmatrix} v_1 & v_2 & \dots & v_n \end{bmatrix} \begin{bmatrix} \frac{1}{r_{11}} &\frac{-r_{12}}{r_{11}} & \frac{-r_{13}}{r_{11}} & \dots \\ & 1 & & \\ & & 1 & \\ & & & \ddots \end{bmatrix} = \begin{bmatrix} q_1 & v_2^{(2)} & \dots & v_n^{(2)} \end{bmatrix}$

- Idea 1: Matrix as a projection transformation

- Idea 2: 

This operation is part of the Gram-Schmidt process, specifically the 'modified' Gram-Schmidt algorithm (MGS) which is essentially a triangular orthogonalization process.

In the equation you've presented, we're trying to orthogonalize the column vectors $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n$ of the matrix $\mathbf{A}$ to get the orthogonal vectors $\mathbf{q}_1, \mathbf{v}_2^{(2)}, \dots, \mathbf{v}_n^{(2)}$.

The first step in the Gram-Schmidt process is to take the first vector $\mathbf{v}_1$ and normalize it to get the first orthogonal vector $\mathbf{q}_1$. This is why the first row of the matrix on the right-hand side of the equation is divided by $r_{11}$, which is just the norm of the vector $\mathbf{v}_1$.

The operation of subtracting the scaled projection of $\mathbf{v}_1$ on $\mathbf{v}_2, \dots, \mathbf{v}_n$ to get $\mathbf{v}_2^{(2)}, \dots, \mathbf{v}_n^{(2)}$ is represented by the negative terms $-\frac{r_{12}}{r_{11}}, -\frac{r_{13}}{r_{11}}, \dots$ in the first row of the right-hand matrix. This operation is essentially a kind of row operation, where the first row is subtracted from the other rows after being scaled by the appropriate factor.

The reason we can perform this operation for 'free' is because it's a straightforward matrix multiplication operation, which is computationally efficient to perform. The complexity of this operation is essentially linear in the number of elements in the matrix.

However, note that this operation is not truly 'free': it still requires computational resources, and more importantly, it can lead to a loss of numerical precision due to subtraction of nearly equal numbers (also known as catastrophic cancellation). This is why the MGS algorithm often includes a re-orthogonalization step, which helps to correct for these numerical errors.


---
## Algorithm

![[Pasted image 20231112153338.png]]
![[Pasted image 20231112153354.png]]

