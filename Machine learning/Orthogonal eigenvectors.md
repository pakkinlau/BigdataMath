---
alias: orthonormal eigenvectors
---

**Definition:**
In linear algebra, orthogonal eigenvectors are a special set of eigenvectors associated with a square matrix. [[Eigenvectors]] are vectors that remain in the same direction (up to scaling) when a matrix is applied to them. When these eigenvectors are also orthogonal to each other, they possess several important properties and applications.

**Key Points:**

1. **Eigenvectors:** Eigenvectors of a matrix A are non-zero vectors x such that A*x = λ*x, where λ is a scalar known as the eigenvalue associated with that eigenvector. Eigenvectors capture the essential transformation characteristics of a matrix.

2. **[[Orthogonality]]:** Two vectors are orthogonal if their dot product is zero. For eigenvectors to be orthogonal, it means that the angle between them is 90 degrees, and they are linearly independent. Orthogonal eigenvectors are fundamental in many mathematical and practical applications.

3. **Orthogonal Matrices:** Orthogonal matrices are square matrices whose columns (and rows) form an orthonormal basis. This means that the columns are orthogonal to each other and have a magnitude of 1. Orthogonal matrices have the property A^T * A = I, where A^T is the transpose of the matrix and I is the identity matrix.

4. **Diagonalization:** When a matrix A has a set of orthogonal eigenvectors, it can be diagonalized. Diagonalization involves finding a diagonal matrix D and an invertible matrix P such that P^(-1) * A * P = D. The diagonal matrix D contains the eigenvalues, and the columns of P are the orthogonal eigenvectors of A.

5. **Applications:** Orthogonal eigenvectors have significant applications in various fields, including physics, computer graphics, signal processing, and quantum mechanics. They simplify the analysis of complex systems and enable efficient computations.

6. [[Spectral theorem]]: The spectral theorem is a fundamental result in linear algebra that states that for a symmetric (or Hermitian) matrix, there exists an orthonormal basis of eigenvectors. This theorem is essential in understanding the properties of such matrices.

**Importance:**
Orthogonal eigenvectors simplify the analysis and manipulation of matrices by providing an orthonormal basis that diagonalizes the matrix. This diagonalization process can reveal critical information about the matrix's behavior, such as its eigenvalues and their associated transformations. The orthogonality property also ensures that the matrix's transformation properties are well-behaved.

Understanding orthogonal eigenvectors is a key concept in linear algebra, enabling the decomposition of matrices into simpler forms for more straightforward calculations and insights into the systems they represent.