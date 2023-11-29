---
alias: unitary matrix
---


- Definition:
	- TD;DL:
		- $Q^* = Q^{-1} \Leftrightarrow$  "Unitary matrix"
			-  where $Q^H$ is the [[conjugate transpose|conjugate transpose]] or [[adjoint|hermitian transpose]] of $U$.
	- Unitary matrix is a complex number version of [[orthogonal matrix]] (refer to p.430 of the book)

---

- Note: $q_i \cdot q_j = \delta_{ij}$, where $\delta_{ij}$ is the Kronecker delta, equal to 1 if $i=j$ and $0$ if $i \neq j$. Hence, the columns $\{ q_i\}$ form an orthonormal basis for $\mathbb{C}^m$. 
	- 1. Kronecker delta:
		- It tells us, the [[dot product]] of any two column vectors from the unitary matrix is equal to the Kronecker delta $\delta_{ij}$. 
	- 2. $\{q_i \}$ form an orthonormal basis for $\mathbb{C}^m$: 
		- This represents a complex vector space of dimension $m$. In other words, it is a space where vectors have $m$ complex components. 
		- Because $q_i$ is in m-dimension and it satisfy $Q^*Q = I$. Thus the columns $\{ q_i\}$ form an orthonormal basis for $\mathbb{C}^m$. 

**Characteristics of Unitary Matrices:**

1. **[[Orthogonal vector]]**: Unitary matrices are known for their orthogonality properties. The columns (or rows) of a unitary matrix form an [[orthonormal]] [[basis]] for the [[vector space]] they operate on. This means that the inner product of any two distinct columns (or rows) is zero, and the inner product of a column (or row) with itself is one.

2. **[[invert|invertibility]]**: Unitary matrices are invertible, and their inverse is equal to their [[conjugate transpose|conjugate transpose]]. If U is a unitary matrix, then U* (conjugate transpose of U) is also a unitary matrix, and $U^*U = I$ (the identity matrix). This property is crucial in various applications, such as solving linear systems and finding the inverse of a matrix.

3. **Preservation of [[Vector Norm]]**: When a unitary matrix operates on a vector, it preserves the norm (magnitude) of the vector. In other words, if v is a vector and U is a unitary matrix, then $||Uv|| = ||v||$. This property is essential in quantum mechanics and signal processing, where the preservation of information is crucial.

4. [[Eigenvalues]] = 1:

    - **Property:** The eigenvalues of a unitary matrix always have a magnitude of 1. This fundamental property arises due to the preservation of norm, making it a pivotal concept in quantum mechanics. Unitary operators in quantum mechanics represent time evolution without altering the probability of observing a specific state.
	    - **Proof:**
	        1. Let $A \mathbf{v} = \lambda \mathbf{v}$.
	        2. Take the conjugate transpose of both sides: $(A\mathbf{v})^* = (\lambda \mathbf{v})^*$.
	        3. Simplifying, we get $\mathbf{v}^* A^* A \mathbf{v} = \bar{\lambda} \mathbf{v}^* \lambda \mathbf{v}$.
	        4. Since $A^* A$ is the identity matrix (due to $A$ being unitary), the equation simplifies further to $\mathbf{v}^* \mathbf{v} = \bar{\lambda} \lambda \mathbf{v}^* \mathbf{v}$.
	        5. Dividing both sides by $\mathbf{v}^* \mathbf{v}$ (assuming $\mathbf{v}$ is nonzero, which is true for eigenvectors), we obtain $1 = \bar{\lambda} \lambda$.
	    - This result confirms that the magnitude of the eigenvalues ($\lambda$) is always 1 for a unitary matrix.




---
- 5. [[invariance under unitary matrix multiplication]]

**Significance of Unitary Matrices:**

1. **Quantum Mechanics**: In quantum mechanics, physical systems evolve over time through unitary operators. Unitary matrices represent these quantum operators, ensuring that the probabilities of different quantum states always sum to one.

2. **Signal Processing**: Unitary transformations are used extensively in signal processing, such as the Discrete Fourier Transform (DFT) and Discrete Cosine Transform (DCT). These transformations help analyze and process signals efficiently.

3. **Error Correction**: In quantum error correction codes, unitary operators are used to correct errors in quantum computations. The preservation of norm is essential in maintaining the integrity of quantum information.

4. **Wave Functions**: In the study of wave functions and wave equations in physics, unitary operators are employed to model the evolution of quantum systems, ensuring the conservation of probability.

In summary, unitary matrices are a fundamental concept in linear algebra with far-reaching applications in various scientific and engineering disciplines. Their unique properties, such as orthogonality, invertibility, and preservation of norm, make them indispensable tools for modeling and solving problems in quantum mechanics, signal processing, and beyond. Understanding unitary matrices is crucial for anyone working in these fields to harness their power effectively.