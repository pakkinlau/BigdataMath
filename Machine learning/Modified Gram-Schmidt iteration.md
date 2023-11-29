
It is a of a type of [[Triangular orthogonalization]]. 


notations and steps involved:

- $v_j = P_j a_j$ 
- $q_j = \frac{v_j}{||v_j||}$
- $P_j = P_{\perp_{qj-1}} \dots  P_{\perp_{q2}} P_{\perp_{q1}}$
	- Recall that $P_{\perp}$ is the orthogonal projector onto the space orthogonal to $q$. 
- $P_1 = I$

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

