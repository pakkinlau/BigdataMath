---
alias: orthogonal matrices

---

- Application:
	- physics, computer graphics, and signal processing. 
	- plays a crucial role in preserving geometric properties, such as angles and lengths, during linear transformations.

**1. Definition:**
- An $n \times n$  [[square matrix]] $A$ is considered orthogonal if its transpose ($A^T$) is equal to its inverse $A^{-1}$. In mathematical terms, if A is an orthogonal matrix, then $A^T = A^{-1}$.
	- From orthogonality, dot product $A$ and $A$, we have $A^TA = I$
	- From Inverse matrix definition, we know the $A^{-1}A = I$ 
	- Comparing terms we have $A^T = A^{-1}$
- An orthogonal matrix is a [[square matrix]]
	- Therefore invertible
- The rows and columns vectors are orthogonal [[unit vectors]]. 
	- One of the key of orthogonal matrices is that when you multiply a vector or matrix by an orthogonal matrix, the length or magnitude of the vector is preserved. 
	- If the vectors making up the columns of the matrix are not of unit length, the multiplication would change the length of the vector. 
- The [[invert|inverse]] of an orthogonal matrix is its [[transpose]], and this property has various applications in [[systems of linear equations]] and in rotations.
- From $Q^TQ = I$, we know that [[Vector Norm]] of the columns and rows of orthogonal matrix $Q$ are orthonormal vectors, meaning that each column has a length of $1$. 

Properties
- $Q^TQ = I_n$ 
	- Note that the dot product return $1$ where $i = j$, it is called [[Kronecker]]
	- Here we get identity matrix I, assuming that Q is a full-rank orthogonal matrix.
- $QQ^T = I_n$
	- It will also return n by n identity matrix.
- $||Qx||^2$ $= x^TQ^TQx = x^Tx = ||x||^2$ 
	- Length is preserved. 
	- While we rotate the $x$, the length is preserved.
- Order of eigenvalues: If we have $S =  Q \Lambda Q^T$, then the largest eigenvector associated with the largest eigenvalue of $S$ would be $q_1$. 
- All orthogonal matrices are [[unitary matrices|unitary matrix]]
- Eigenvalues of $Q$: 
	- $Qx = \lambda x$ 
	- $||Qx||^2 = |\lambda|^2 ||x||^2$ 
	- $|\lambda|^2 = 1$

**2. Geometric Interpretation:**
   Orthogonal matrices are closely related to [[linear transformation]] that represent rotations, reflections, and combinations of these transformations in Euclidean space. 
   - [[Matrix-Vector Multiplication]]
	   - When you multiply a vector by an orthogonal matrix, it preserves the length (norm) of the vector and maintains the angles between vectors.

**3. Key Properties:**
   - 1. Orthogonal matrices have [[determinant]] values of ±1. If $det(A) = 1$, it represents a proper (rotation) orthogonal matrix, while $det(A) = -1$ corresponds to an improper (reflection) orthogonal matrix.
	   - Proof:
		1. **Definition of Orthogonal Matrix:**
		   By definition, an orthogonal matrix satisfies $A^T = A^{-1}$.
		2. **Determinant Properties:**
		   - *Determinant of Transpose:* The determinant of a transpose of a matrix is equal to the determinant of the original matrix, i.e., $\text{det}(A^T) = \text{det}(A)$.
		   - *Determinant of the Inverse:* The determinant of the inverse of a matrix is the reciprocal of the determinant of the original matrix, i.e., $\text{det}(A^{-1}) = \frac{1}{\text{det}(A)}$.
		3. **Analysis of $A^T A$ and Identity Matrix $I$:**
		   Considering $A^T A$, we find:
		$$
		   \begin{align*}
		   \text{det}(A^T A) &= \text{det}(A^T) \times \text{det}(A) \quad \text{(Using determinant of a product property)} \\
		   &= \text{det}(A) \times \text{det}(A) \quad \text{(Since $\text{det}(A^T) = \text{det}(A)$)} \\
		   &= (\text{det}(A))^2.
		   \end{align*}
		$$
		4. **Identity Matrix and Determinant:**
		   As orthogonal matrices satisfy $A^T = A^{-1}$, $A^T A$ is the identity matrix $I$. Therefore, $\text{det}(I) = \text{det}(A^T A)$. Since $\text{det}(I) = 1$, we have $1 = (\text{det}(A))^2$.
		5. **Conclusion:**
		   Taking the square root of both sides, we find $\text{det}(A) = \pm 1$. This proves that orthogonal matrices indeed have determinant values of ±1.

---
   - 2. The columns of an orthogonal matrix form an [[orthonormal]] [[basis]], meaning they are orthogonal to each other and have unit length.
	   - Proof:
		1. **Orthogonality of Columns:**
		   - Consider an $n \times n$ orthogonal matrix $A$ with columns $A_1, A_2, ..., A_n$.
		   - For any two columns $A_i$ and $A_j$ (where $i$ and $j$ are indices between 1 and $n$), their dot product is $(A_i)^T \cdot A_j$.
		   - Since $A$ is orthogonal, $A^T \cdot A = I$ (the identity matrix).
		   - Therefore, $(A_i)^T \cdot A_j = ((A^T \cdot A)_{ij})$, which equals 1 if $i = j$ and 0 if $i \neq j$.
		   - This proves that columns $A_i$ and $A_j$ are orthogonal for all $i \neq j$.
		2. **Unit Length of Columns:**
		   - To show the columns have unit length, we need to prove $||A_i|| = 1$ for each column $A_i$, where $||A_i||$ represents the Euclidean norm of $A_i$.
		   - The norm of a column $A_i$ is calculated as $||A_i|| = \sqrt{(A_i)^T \cdot A_i}$.
		   - Using the orthogonality property, $(A_i)^T \cdot A_i = 1$ (diagonal elements of the identity matrix).
		   - Hence, $||A_i|| = \sqrt{1} = 1$.

   - 3. The rows of an orthogonal matrix also form an [[orthonormal]] [[basis]].
	   - Proof:
		   - Combine property 1 and 2, we can prove property 3. 

**4. Applications:**
   - **Rotation:** In computer graphics, orthogonal matrices are used to rotate objects in three-dimensional space without distortion.
   - **Change of [[Basis]]:** In linear transformations, orthogonal matrices are employed to change the basis of a vector space while preserving its properties.
   - **Signal Processing:** Orthogonal matrices are essential in algorithms like the Fast Fourier Transform (FFT) and discrete cosine transform (DCT), where preserving the energy and orthogonality of basis functions is crucial.
   - **[[Reduced QR decomposition]]:** [[orthogonal matrix]] are employed in the [[Reduced QR decomposition]] method to factorize a matrix into an orthogonal matrix (Q) and an [[triangular matrix]] (R).

**5. Orthogonal Matrix Examples:**
   - The identity matrix is an orthogonal matrix because its transpose is itself, and its determinant is 1.
   - Rotational matrices, like those used in 2D and 3D transformations, are orthogonal matrices.
   - Householder reflections, which are used in numerical algorithms, are also orthogonal matrices.

**6. Properties of Orthogonal Matrices:**
   - Orthogonal matrices are always invertible, and their inverse is also orthogonal.
   - The product of two orthogonal matrices is again an orthogonal matrix.
   - The transpose of an orthogonal matrix is orthogonal.
   - Orthogonal matrices form a group known as the orthogonal group, denoted as O(n).

In summary, orthogonal matrices are a fundamental concept in linear algebra with a wide range of applications due to their ability to preserve geometric properties during linear transformations. They are a cornerstone in fields where preserving angles and lengths is critical, making them a powerful tool in various mathematical and scientific disciplines.