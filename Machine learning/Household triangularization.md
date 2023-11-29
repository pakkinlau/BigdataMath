In [[Modified Gram-Schmidt iteration]] and [[Triangular orthogonalization]], we have $AR_1 R_2 \dots R_n = \hat Q$ or $A \hat R^{-1} = \hat Q$. We applied a set of triangular matrices to orthogonalize our matrix $A$. 

On the other hand, the Householder applies a succession of [[unitary matrices]] $Q_k$ on the left of $A$, such that $Q_n \dots Q_2 Q_1 A = R$, or $Q^* A = R$, so that the result is upper triangular. 

The product $Q = Q_1^* \dots Q_n^*$ is also unitary. 

Hence, $A = QR$ is the required QR factorization. So, we call this orthogonal triangularization. 

---
Input: Any matrix $A$

Output: upper triangular matrix $R$

We want to obtain an unitary matrix $Q_k$ such that $Q_k$ could turns the $k$th column of $A$ to be zero except the first $k$th row element remain unchanged. 

![[Pasted image 20231125203157.png]]

Goal: how to construct $Q_k$?
- We have already talked [[Orthogonal Projector]]



---

Householder triangularization, also known as Householder transformation or Householder reduction, is a fundamental technique in linear algebra used to reduce a matrix to upper or lower triangular form. 
This process is valuable in solving systems of linear equations, eigenvalue computations, and various numerical algorithms.

1. **Definition**:
   - Householder triangularization is a method for transforming a given matrix into a triangular form, typically upper triangular. The transformation is accomplished through a series of orthogonal reflections known as Householder reflections.

2. **Householder Reflection**:
   - A Householder reflection is an orthogonal matrix that reflects a vector about a hyperplane defined by a unit vector. It is designed to annihilate all elements of a vector except the first element, making it zero.

3. **Procedure**:
   - To perform Householder triangularization on a matrix A, the process usually involves a series of Householder reflections. The reflections are applied successively to eliminate the subdiagonal elements, making the matrix upper triangular.
   - At each step, a Householder vector (a vector that defines the reflection) is calculated to zero out the appropriate subdiagonal elements.

4. **Benefits**:
   - Householder triangularization preserves the row space of the original matrix, which means it doesn't change the solution to the system of linear equations. This is useful for solving such systems.
   - It provides a convenient way to compute the eigenvalues of a matrix since triangular matrices have easily identifiable eigenvalues.

5. **Numerical [[Stability]]**:
   - Householder transformations are numerically stable, making them suitable for numerical computations, including solving ill-conditioned systems of equations.

6. **Applications**:
   - Householder triangularization is used in various numerical methods, including the QR decomposition, least squares solutions, and the computation of eigenvalues and singular values.

7. **Complexity**:
   - The computational complexity of Householder triangularization is about O(n^3), making it a feasible method for moderate-sized matrices.
---
## Overview of the algorithm

Say $A$ is a $5 \times 3$ matrix. We will find $Q_1, Q_2, Q_3$ so that $Q_3 Q_2 Q_1 A$ is upper triangular. 

![[Pasted image 20231112181026.png]]

In general, the matrix $Q_k$ is defined to make the entries below the $k$th diagonal element zero, and it does not change the first $k-1$ columns. 


---
## Construction of $Q_k$

- Recall the matrix $Q_k$ is defined to make the entries below the $k$th diagonal element zero, and it does not change the first $k-1$ columns.  '
- So $Q_k$ is chosen to have the form $\begin{pmatrix} I & 0 \\ 0 & F\end{pmatrix}$, where $I$ is the $(k-1) \times (k-1)$ identity matrix, and $F$ is an $(m - k + 1) \times (m - k + 1)$ unitary matrix. 
- A requirement for $F$ is that it will create zero below the $k$th diagonal element. 
- The matrix $F$ will be chosen as the [[Householder reflector]]
