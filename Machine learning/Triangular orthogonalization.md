
- superset:
	- [[Orthogonalization]]

- When people mention "triangular orthogonalization", they are often referring to either the [[Modified Gram-Schmidt iteration]] or [[Household triangularization]]. 

- It is a broad concept that describing "orthogonalizing a matrix, in triangular manner".
- [[Reduced QR decomposition|Gram-Schmidt orthogonalization]] falls into the category of triangular orthogonalization 

---

Triangular orthogonalization is a fundamental technique in linear algebra used to transform a given set of vectors into an orthogonal or orthonormal set. In the context of linear algebra, vectors are often represented as columns of a matrix, and triangular orthogonalization is a method to simplify these vectors, making them easier to work with in various mathematical computations, such as solving systems of linear equations, computing determinants, or finding eigenvalues and eigenvectors.

**Key Steps in Triangular Orthogonalization:**

1. **Gram-Schmidt Process:**
   - Given a set of vectors $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$, the Gram-Schmidt process starts by creating an orthogonal set from these vectors.
   - The first vector $\mathbf{u}_1$ in the orthogonal set is the same as $\mathbf{v}_1$.
   - For $i = 2$ to $n$, the orthogonalized vectors $\mathbf{u}_i$ are computed as:
$$
     \mathbf{u}_i = \mathbf{v}_i - \sum_{j=1}^{i-1} \frac{\langle \mathbf{v}_i, \mathbf{u}_j \rangle}{\|\mathbf{u}_j\|^2} \mathbf{u}_j
$$
     where $\langle \cdot, \cdot \rangle$ represents the dot product of vectors, and $\|\cdot\|$ denotes the Euclidean norm.

2. **Normalization (Optional):**
   - If orthonormal vectors are desired, each vector $\mathbf{u}_i$ is divided by its norm $\|\mathbf{u}_i\|$ to obtain unit vectors.
   - In [[Reduced QR decomposition|QR factorization]], orthonormal vector is chosen.

---
## Steps of working on triangular orthogonalization

Each step of the modified Gram-Schmidt algorithm can be interpreted as a right-multiplication by a square upper-triangular matrix. 

Step 1: Recall [[Modified Gram-Schmidt iteration]], we have 
- $v_j = P_j a_j$ 
- $q_j = \frac{v_j}{||v_j||}$
- $P_j = P_{\perp_{qj-1}} \dots  P_{\perp_{q2}} P_{\perp_{q1}}$
- $P_1 = I$

Triangular orthogonalization:

In the step 1, we multiply the first column $a_1$ by $\frac{1}{r_{11}}$, and then subtract $r_{1j}$ times the result from each of the remaining columns $a_j$. 
- $r_{11}$ is the norm of the vector $v_1$, which is the projection of the projection of the first column vector $a_1$ of the original matrix $A$. 
- for the second part "subtract $r_{1j}$ times the result from each of the remaining columns $a_j$". This is part of the Gram-Schmidt process where you remove the component of the remaining vectors that is in the direction of $q_1$.
	- In this case, $r_{1j}$ is the dot product of $q_1$ and $a_j$, i.e., $r_{1j} = q_1^T a_j$. This is the component of $a_j$ that is in the direction of $q_1$. By subtracting $r_{1j}q_1$ from $a_j$, we are effectively removing the part of $a_j$ that lies in the direction of $q_1$, leaving us with a vector that is orthogonal to $q_1$.
- This completes the first step of the process, resulting in the first orthonormal vector $q_1$ and a set of vectors orthogonal to $q_1$. Further steps of the process would continue in a similar manner to orthogonalize and normalize the remaining vectors.

That matrix is equivalent to right multiplication by a matrix $R$. 


$\begin{bmatrix} v_1 & v_2 & \dots & v_n \end{bmatrix} \begin{bmatrix} \frac{1}{r_{11}} & \frac{-r_{12}}{r_{11}} & \frac{-r_{13}}{r_{11}} & \dots \\ & 1 & & \\ & & 1 & \\ & & & \ddots \end{bmatrix} = \begin{bmatrix} q_1 & v_2^{(2)} & \dots & v_n^{(2)} \end{bmatrix}$

This is equivalent to right multiplication by a matrix $R_1$ 

Step 2: 

$\begin{bmatrix} v_1 & v_2 & \dots & v_n \end{bmatrix} \begin{bmatrix} \frac{1}{r_{11}} & \frac{-r_{12}}{r_{11}} & \frac{-r_{13}}{r_{11}} & \dots \\ & 1 & & \\ & & 1 & \\ & & & \ddots \end{bmatrix} \begin{bmatrix} 1 & & & \\ & \frac{1}{r_{22}} & \frac{-r{23}}{r_{22}} & \dots \\ & & 1 & \\ & & & \ddots \end{bmatrix} = \begin{bmatrix} q_1 & q_2 & v_3^{(3)}\dots & v_n^{(3)} \end{bmatrix}$

This is equivalent to right multiplication by a matrix $R_1$ and $R_2$.

Step $i$:

The $i$th column is divided by $r_{ii}$, and then subtract $r_{ij}$ times the result from each of the remaining columns, for $j>i$. 

Finally, we have $AR_1 R_2 \dots R_n = \hat Q$, 
or $A \hat R^{-1} = \hat Q$

This shows [[Modified Gram-Schmidt iteration]] is a method of triangular orthogonalization.








