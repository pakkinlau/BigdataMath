
- subset:
	- [[Orthogonal eigenvectors]] 

Eigenvectors are fundamental concepts in linear algebra with a wide range of applications in various fields, including physics, engineering, computer science, and data analysis. They play a crucial role in understanding linear transformations and diagonalization of matrices.

**Definition:**
An eigenvector of a square matrix A is a non-zero vector v that, when multiplied by A, results in a scaled version of itself. Mathematically, if Av = λv, where λ is a scalar (known as the eigenvalue), then v is an eigenvector of A.

**Key Properties and Characteristics:**

1. [[eigenvalues]]: Every eigenvector is associated with a corresponding eigenvalue. Multiple eigenvectors can have the same eigenvalue.

2. **Linear Independence:** Eigenvectors corresponding to distinct eigenvalues are linearly independent, which makes them useful for diagonalization and simplification of matrix operations.

3. **Diagonalization:** If a square matrix A has a complete set of linearly independent eigenvectors, it can be diagonalized. Diagonalization transforms A into a diagonal matrix D with eigenvalues on the main diagonal and their corresponding eigenvectors as columns of a matrix P. This is expressed as A = PDP⁻¹, where P is the matrix of eigenvectors, and D is the diagonal matrix of eigenvalues.

---



---
4. **Applications:**

   - **Principal Component Analysis (PCA):** Eigenvectors are used to transform data into a new coordinate system that maximizes variance, aiding in dimensionality reduction and feature extraction.
   
   - **Quantum Mechanics:** In quantum mechanics, eigenvectors of the Hamiltonian operator correspond to the allowed energy states of a quantum system.

   - **Vibration Analysis:** In mechanical engineering, eigenvectors are used to analyze the modes of vibration in structures and systems.

   - **Data Analysis:** Eigenvectors are employed in techniques like singular value decomposition (SVD) and the covariance matrix for data analysis and machine learning.

**Calculation of Eigenvectors and Eigenvalues:**

To find eigenvectors and eigenvalues for a matrix A, one typically solves the characteristic equation: det(A - λI) = 0, where λ is an eigenvalue and I is the identity matrix. Once eigenvalues are found, you can find eigenvectors by solving the equation (A - λI)v = 0.

