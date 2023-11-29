---
alias: diagonal
---


Diagonal matrices are a fundamental concept in linear algebra, playing a crucial role in various mathematical and practical applications. A diagonal matrix is a special type of [[square matrix]] in which all off-diagonal elements are zero. In other words, it is a matrix where only the elements on the main diagonal, running from the top-left to the bottom-right, are non-zero.

Here are some key characteristics and properties of diagonal matrices in the context of linear algebra:

1. **Definition**: A square matrix \(D\) with dimensions $(n \times n)$ is considered diagonal if and only if $(d_{ij} = 0)$ for all $(i \neq j)$, where $(d_{ij})$ represents the elements of the matrix $(D)$.

2. **Notation**: Diagonal matrices are often represented using square brackets or diag() notation, where the diagonal elements are enclosed within square brackets or specified using the diag() function.

   Example:
  $$ \[
   D = \begin{bmatrix}
   d_{11} & 0 & 0 & \cdots & 0 \\
   0 & d_{22} & 0 & \cdots & 0 \\
   0 & 0 & d_{33} & \cdots & 0 \\
   \vdots & \vdots & \vdots & \ddots & \vdots \\
   0 & 0 & 0 & \cdots & d_{nn}
   \end{bmatrix}
   \]$$

3. **Scalar Multiplication**: Multiplying a diagonal matrix by a scalar simply involves multiplying each diagonal element by that scalar.

4. [[Matrix-matrix multiplication]] When multiplying a diagonal matrix by another matrix, the result is obtained by performing element-wise multiplication between the diagonal matrix and the other matrix. This operation is computationally efficient because all off-diagonal multiplications are zero.

5. **[[invert|inverse]]**: A diagonal matrix is invertible if and only if all its diagonal elements are non-zero. The inverse of a diagonal matrix is obtained by taking the reciprocal of each non-zero diagonal element.

6. **[[Eigenvalues and Eigenvectors]]**: Diagonal matrices are closely related to the concept of eigenvalues and eigenvectors. The eigenvalues of a diagonal matrix are simply its diagonal elements, and the eigenvectors are the standard basis vectors (vectors with a single non-zero entry corresponding to the diagonal element).

7. **Applications**: Diagonal matrices are frequently used in various applications, including [[systems of linear equations]], [[diagonalization]] of matrices, and [[Linear transformation]] in linear algebra.

8. **Spectral Decomposition**: Diagonal matrices play a central role in the [[Eigenvalue Decomposition]] of matrices, where a matrix can be expressed as a product of diagonal matrices and their corresponding transformations.

